# Python Dynamic Registry

Registers subclasses of a parent or abstract class at runtime.

Coming soon: also adding the ability to register functions.



## Installation 

    $ pip install git+ssh://git@github.com/jlookup/dynamic-registry.git@main


## Usage

## ClassRegistry

### Initialization:
A registry must have a type. The type is the parent or abstract class, which is passed at initialzation. By default, the registry will search the parent class's directory and import all subclasses into the registry. 

    from your_class_directory.your_parent_class_module import YourParentClass
    from dynamic_registry import ClassRegistry

    class_registry = ClassRegistry(YourParentClass)

For thoroughness the search is **recursive**. For large directories this could be slow. 

If there are subclasses contained in a different directory you can call `register_directory()` and pass the directory as a `str` or a `pathlib.Path`.

    class_registry.register_directory('your_other_subclass_directory')

### Referencing Objects in the Registry
### Option 1 - Safest
Calling `get_class()` will return `None` if the subclass is not in the registry.

    your_subclass = class_registry.get_class('YourSubClass')
    if your_subclass is not None:
        your_subclass_instance = your_subclass()


### Option 2
Each subclass and alias is an attribute of the `Registry` object. 

    your_subclass_instance = class_registry.YourSubClass()

Calling an unregistered class will raise `AttributeError`.

    your_subclass_instance = class_registry.UnregisteredSubClass()


### Option 3
Each subclass and alias is contained in the `registry` dict of the Registry object. Calling an unregistered class will raise a `KeyError`.

    class_registry_dict = class_registry.registry
    your_subclass_instance = class_registry_dict['YourSubClass']() 



## Examples 

Coming soon
