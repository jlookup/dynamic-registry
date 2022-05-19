
from os import path 

from dynamic_registry.registry import Registry 

class FunctionRegistry(Registry):

    def __init__(self, directory=None, attrs=None, 
                 register_whole_directory=False):
        assert self._validate_init(directory, attrs, register_whole_directory)
        


        pass

    def _validate_init(self, directory=None, attrs=None, 
                       register_whole_directory=False):
        
        if not attrs and not register_whole_directory:
            raise Exception("Must either pass attrs or specify a whole directory") 
        elif attrs and register_whole_directory:
            raise Exception("Must either pass attrs or specify a whole directory, not both")
        else:
            from pathlib import Path
            dir = Path(directory)
            if not dir.is_dir():
                raise Exception(f"{dir.resolve()} is not an existing directory")

        return True




    def _validate_attr_for_registry(self, attribute):
        """
        Validator to check if an attribute (class, function, or variable) of a module
        meets the criteria for inclusion in the registry.
        """
        # function registry
        # Check if the attribute is callable
        # If we have attrs check if the callable has them.
        # if inspect.isclass(attribute) and issubclass(attribute, self._parent) and not attribute == self._parent: 
        #     return True
        # return False



# def register_functions(tags, directory=None) -> dict:
#     pass