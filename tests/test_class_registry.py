"""
Test the ClassRegistry class in the dynamic_registry package.
Must install the package locally in development mode prior to running tests:
    $ pip install -e .
"""

import pytest

import testing_utils as u
from characters.character import Character 
from dynamic_registry import ClassRegistry


@pytest.fixture(scope='module')
def reg():
    """Instantiate the Registry object for the Character parent class"""
    return ClassRegistry(Character)  

@pytest.fixture(scope='module')
def reg2():
    """Instantiate the Registry object for the Character parent class, with an alias"""
    return ClassRegistry(Character, ['species']) 


def test_registry_init():
    """Verify that a registry object is created"""
    reg = ClassRegistry(Character)
    assert (reg is not None)
    assert isinstance(reg, object)


def test_registry_contains_subclasses(reg):
    """Verfiy that the registry dict exists and contains subclasses of the parent class"""
    assert (reg.registry is not None)

    # Knight, Orc, Elf
    assert (len(reg.registry) == 3)

    assert (issubclass(reg.registry['Knight'], Character))
    assert (issubclass(reg.registry['Knight'], reg.parent))    


def test_registry_alias(reg2):
    """Verify that the registry loads and uses aliases."""
    # Reg2 includes an alias, 'species'.
    # Knight will have the alias Human.
    # The registry will contain both 'Knight' and 'Human'. 
    # Orcs' and Elves' species is the same as the character name
    # so they will still only have one entry.
    # Total of 4 entries in the registry.
    assert (len(reg2.registry) == 4)

    assert (issubclass(reg2.registry['Knight'], Character))
    assert (issubclass(reg2.registry['Human'], Character))    


def test_init_subclass_via_registry(reg2):
    """Instantiate a subclass from the registry using a few different methods"""
    from characters.character import Knight

    def assertions(char):
        assert(char is not None)
        assert(isinstance(char, Knight))
        assert(isinstance(char, Character)) 
        assert(char.is_mortal == True)
        assert(char.name == 'knight')
        assert(char.level == 1)       

    k = reg2.Knight(name='knight', level=1)
    assertions(k)

    k = reg2.registry['Knight'](name='knight', level=1)
    assertions(k)

    k = reg2.get_class('Human')(name='knight', level=1)
    assertions(k)


def test_init_sublcass_not_in_registry(reg):
    """Behavior when trying to access a subclass that doesn't exist"""

    w = reg.get_class('Dragon')
    assert (w is None)
    
    with pytest.raises(KeyError):
        reg.registry['Dragon']

    with pytest.raises(AttributeError):
        reg.Wizard


def test_registry_init_without_register_parent_dir():
    """
    Instantiate the Registry 
    but don't automatically regsiter
    from the parent class's directory
    """
    reg = ClassRegistry(Character, register_parent_directory=False)
    assert reg.registry == {}


def test_registry_init_without_register_parent_dir_then_register():
    """
    Instantiate the Registry 
    but don't automatically regsiter
    from the parent class's directory
    """
    reg = ClassRegistry(Character, register_parent_directory=False)
    reg.register_directory(u.TEST_DIR / 'characters')

    # Knight, Orc, Elf
    assert (len(reg.registry) == 3)


def test_register_other_dir():
    """Register a subclass from a different directory"""

    reg = ClassRegistry(Character)
    # Knight, Orc, Elf
    assert (len(reg.registry) == 3) 

    reg.register_directory(u.TEST_DIR / 'character_expansion')
    # Knight, Orc, Elf, Wizard
    assert (len(reg.registry) == 4)
    assert 'Wizard' in reg.registry


if __name__ == '__main__': 
    pytest.main([__file__])
