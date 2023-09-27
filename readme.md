# Python Dynamic Registry

Creates a registry of subclasses of a parent or abstract class at runtime.

New subclasses can be imported and made available _without changes to application code_. New subclasses are added to a new or existing module in a predifined directory. At runtime the new subclass will be discovered, registered, and imported.

Dynamic Registry is a way to implement the [Liskov Substitution Principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle) and the [Dependency Inversion Priciple](https://en.wikipedia.org/wiki/Dependency_inversion_principle) of Robert Martin's [SOLID](https://en.wikipedia.org/wiki/SOLID).

**Future Expansion:** also adding the ability to register functions. 



## Installation 

    $ pip install git+ssh://git@github.com/jlookup/dynamic-registry.git@main


## Usage - ClassRegistry

Imagine a game with multiple character types. We want the ability to add new characters via expansion packs without altering the game code. 

### Initialization
A registry must have a type. The type is the parent or abstract class, which is passed at initialzation. We'll pass it the `Character` abstract class.

    from dynamic_registry import ClassRegistry    
    from characters.character import Character

    character_registry = ClassRegistry(Character)

### Registration
To register child classes we call `register_directory()` and pass the directory where they are found as a `str` or a `pathlib.Path`.

    character_registry.register_directory('expansion_packs')

This is done at the directory level for maximum flexibility. Only the directories where child classes are currently located or could be added have to be hardcoded at compile time. Within those directories new modules can be added or existing ones modified, and the changes will be picked up at runtime. 

**Note:** for thoroughness the registration search is **recursive**; it evaluates all classes in all python modules in the given directory, and could be slow. 

By default, at init the registry will call `register_directory()` on the directory where the parent class is located. You can override this by passing `register_parent_directory=False` when creating the registry. In our example, any child classes defined in the `characters` dir will be registered automatically. That includes subclasses located in the same module as the parent class.

### Referencing Objects in the Registry

There are multiple ways to reference a register class.

### Option 1 - get_class()
Calling `get_class()` will return `None` if the subclass is not in the registry.

    my_character = character_registry.get_class('Elf')
    if my_character is not None:
        your_subclass_instance = my_character()


### Option 2 - dot notation
Each subclass and alias is an attribute of the `Registry` object. 

    my_character = character_registry.Elf()

Calling an unregistered class will raise `AttributeError`.

    my_character = character_registry.ThisCharacterDoesNotExist()


### Option 3 - registry dictionary
Each subclass and alias is contained in the `registry` dict of the Registry object. Calling an unregistered class will raise a `KeyError`.

    my_character = character_registry.registry['YourSubClass']() 

