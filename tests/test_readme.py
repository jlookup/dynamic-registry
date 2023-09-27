"""Test the tutorial in readme.md.
"""

import pytest


def test_readme():

    from dynamic_registry import ClassRegistry
    from characters.character import Character

    class_registry = ClassRegistry(Character) 

    # class_registry.register_directory('your_other_subclass_directory')

    your_subclass = class_registry.get_class('Knight')
    if your_subclass is not None:
        your_subclass_instance = your_subclass('Arthur', 100)   
    assert your_subclass is not None 

    your_subclass_instance = class_registry.Knight('Arthur', 100)

    with pytest.raises(AttributeError):
        your_subclass_instance = class_registry.UnregisteredClass('Arthur', 100)

    class_registry_dict = class_registry.registry
    your_subclass_instance = class_registry_dict['Knight']('Arthur', 100) 

if __name__ == '__main__':
    pytest.main([__file__])
