""" 
Dynamically finds and registers all subclasses of a parent or abstract class. 
"""

from abc import ABC, abstractmethod

import pkgutil
import inspect
import sys
from pathlib import Path
from importlib import import_module
from typing import Dict


class Registry(ABC):
    """ 
    Dynamically finds and registers all subclasses of a parent or abstract class. 
    """

    def register_directory(self, directory=None):
        """
        Register all subclasses of the parent class
        located in the given directory.
        """
        # If no directory is passed we default to the directory 
        # where the calling function is located
        if directory is None:
            caller_file = inspect.stack()[1].filename
            directory = Path(caller_file).resolve().parent
        else:
            directory = Path(directory).resolve()

        for (_, module_name, ispkg) in pkgutil.iter_modules([directory.__str__()]):
            # import the module and iterate through its attributes
            if not ispkg:
                package_module = f"{directory.stem}.{module_name}"
                module = import_module(package_module)

            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)

                # the validation function is defined by the registry subclass
                if self._validate_attr_for_registry(attribute):
                    self.register_attribute(attribute)


    @abstractmethod
    def _validate_attr_for_registry(self, attribute):
        """
        Validator to check if an attribute (class, function, or variable) of a module
        meets the criteria for inclusion in the registry.
        Abstract method. 
        """


    def register_attribute(self, attribute):
        """Register a single class, using its class name and any aliases"""
        pointer = attribute.__name__
        self._set_registry_item(attribute, pointer)

        # Optional aliases to add to the regsitry
        if self.alias_attrs is not None:
            for attr in self.alias_attrs:
                if hasattr(attribute, attr) \
                and getattr(attribute, attr) is not None: 
                    pointer = getattr(attribute, attr)
                    self._set_registry_item(attribute, pointer)


    def _set_registry_item(self, attribute, pointer):
        """ 
        Set the name or alias as an attribute of the Regsitry object 
        and as an element of the registry dict.
        Child of self.register_class()
        """
        # Set the subclass as an attribute of the registry object
        # so it can be called using dot notation.
        self.__setattr__(pointer, attribute) 

        # Add the subclass to the registry dictionary
        # so it can be called using r.registry['subclass_name']       
        self.registry[pointer] = attribute


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

