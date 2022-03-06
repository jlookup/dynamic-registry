# Python Dynamic Registry

Dynamically finds and registers all subclasses of a parent or abstract class. 



## Installation 

    $ pip install https://git.innova-partners.com/jason-thomas/dynamic-registry


## Usage

Initialization:
A parent or abstract class is passed to initialize the Registry object. On init it will search the 
parent class's directory and import all subclasses into the registry. If there are subclasses contained 
in a different directory you will need to call `register_directory()` after init and pass the directory path.

    from your_class_directory.your_parent_class_module import YourParentClass
    from dynamic_registry import Registry
    class_registry = Registry(YourParentClass)


Usage Option 1 - safest
Calling `get_class()` on the Registry object will return `None` 
if the subclass is not found in the registry.

    your_subclass = class_registry.get_class('YourSubClass')
    if your_subclass is not None:
        your_subclass_instance = your_subclass()


Option 2
Each subclass (and any aliases) is an attribute of the Registry object.
Calling an unregistered class will raise an `AttributeError`.

    your_subclass_instance = class_registry.YourSubClass()


Option 3
Each subclass (and any aliases) is contained in the registry dict of the Registry object.
Calling an unregistered class will raise a `KeyError`.

    class_registry_dict = class_registry.registry
    your_subclass_instance = class_registry_dict['YourSubClass']() 



## Examples 

See https://git.innova-partners.com/jason-thomas/extensibility-demo
