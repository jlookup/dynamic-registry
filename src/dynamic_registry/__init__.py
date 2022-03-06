""" 
Dynamically finds and registers all subclasses of a parent or abstract class. 

Usage:
    from your_class_directory.your_parent_class_module import YourParentClass
    from dynamic_registry import Registry

    # option 1
    class_registry = Registry(YourParentClass)
    your_subclass_instance = class_registry.YourSubClass()

    # option 2
    class_registry = Registry(YourParentClass).registry
    your_subclass_instance = class_registry['YourSubClass']()    
"""

__version__ = "0.1.0"

from .registry import Registry
__all__ = [Registry]