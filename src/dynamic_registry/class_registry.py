""" 
Dynamically finds and registers all subclasses of a parent or abstract class. 
"""

import pkgutil
import inspect
import sys
from pathlib import Path
from importlib import import_module
from typing import Dict

from dynamic_registry.registry import Registry

class ClassRegistry(Registry):
    """ 
    Dynamically finds and registers all subclasses of a parent or abstract class. 
    """

    def __init__(self, parent_class, alias_attrs=None, 
                 register_parent_directory=True):
        self._parent: object = parent_class
        self.alias_attrs = alias_attrs        
        self.registry: Dict = {}
        if register_parent_directory: 
            self._register_parent_directory()
        self._set_registry_alias()


    def _register_parent_directory(self):
        """
        Register all subclasses in the same directory as the parent class.
        Called during init.
        Normally this will be the only regsitration needed.
        """
        parent_module = self._parent.__module__
        parent_file = sys.modules[parent_module].__file__
        parent_directory = Path(parent_file).resolve().parent
        self.register_directory(parent_directory)
        pass


    def _validate_attr_for_registry(self, attribute):
        """
        Validator to check if an attribute (class, function, or variable) of a module
        meets the criteria for inclusion in the registry.
        """
        # subclass registry
        # Check if the attribute is a subclass of the parent class but is not the parent class itself.
        if inspect.isclass(attribute) and issubclass(attribute, self._parent) and not attribute == self._parent: 
            return True
        return False


    def _set_registry_alias(self):
        """Alias the registry dict with a plural of the parent class name"""
        parent_name = self._parent.__name__.lower()
        registry_alias = f'{parent_name}es' if parent_name.endswith('s') else f'{parent_name}s'
        self.__setattr__(registry_alias, self.registry)


    @property
    def parent(self):
        """The parent/superclass/abstract class of the classes in the regsitry."""
        return self._parent
    
    @parent.setter
    def parent(self):
        """The registry parent class cannot be changed."""
        print('Parent class cannot be changed')
        return False

    @parent.deleter
    def parent(self):
        """The registry parent class cannot be changed."""
        print('Parent class cannot be changed')
        return False


    def get_class(self, subclass: str):
        """Returns a pointer to a registered class."""
        try:
            return self.registry[subclass]
        except KeyError as e:
            print(f"""Error: {e} not found in the registry.""")
            return None


    def list_registry(self):
        """Return a list of regsitry keys"""
        return sorted(self.registry.keys())


    def print_registry(self):
        """Print the regsitry keys"""
        subclass_list_sorted = sorted(self.registry.keys())
        print(f'Available options:')
        for key in subclass_list_sorted:
            print(f'    {key}')

