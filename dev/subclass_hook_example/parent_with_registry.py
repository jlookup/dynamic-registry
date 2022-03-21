


from abc import ABC, abstractmethod
import sys 
from pathlib import Path
import pkgutil
from importlib import import_module

class ParentWithRegistry(ABC):

    # TODO: the _registry dict is global, 
    # shared across all children and grandchildren of ParentWithRegistry.
    # need to figure out how to instantiate it at the "parent" level
    # ("parent" meaning the child of ParentWithRegistry 
    # that will have its own children in its registry) 
    _registry = {}

    def __init_subclass__(cls, lookup) -> None:
        cls.__bases__[0]._registry[lookup] = cls
        _ = ''

    def __new__(cls, lookup, *args, **kwargs):
        subclass = cls._registry[lookup]
        obj = object.__new__(subclass)
        return obj

    @staticmethod
    def register_subclasses(directory=None):
        """
        Import all modules in the given directory.
        All subclasses with automatically be registered on import.
        Static method. Parent class does not need to be instantiated.
        """
        # If no directory is passed we default to the directory 
        # where the parent is located
        if directory is None:
            directory = Path(__file__).resolve().parent
            if not Path(directory).resolve().parent in sys.path:
                sys.path.append(str(Path(directory).resolve().parent))

        # import all modules. 
        # If they contain children of the parent class, those will be registered        
        for (_, module_name, _) in pkgutil.iter_modules([directory]):
            module = import_module(f"{directory.stem}.{module_name}")

