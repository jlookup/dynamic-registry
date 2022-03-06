"""
Test the Registry class in the dynamic_registry package.
Must install the package locally in development mode prior to running tests:
    $ pip install -e .
"""

import pytest

from characters.character import Character 
from dynamic_registry import Registry


def test_registry_init():
    """Verify that a registry object is created"""
    reg = Registry(Character)
    assert (reg is not None)
    assert isinstance(reg, object)


@pytest.fixture(scope='module')
def reg():
    """Instantiate the Registry object for the Character parent class"""
    return Registry(Character)  

@pytest.fixture(scope='module')
def reg2():
    """Instantiate the Registry object for the Character parent class, with an alias"""
    return Registry(Character, ['species'])  


def test_registry_contains_subclasses(reg, reg2):
    """Verfiy that the registry dict exists and contains subclasses of the parent class"""
    assert (reg.registry is not None)

    # Knight, Orc, Elf
    assert (len(reg.registry) == 3)

    # Reg2 includes an alias, 'species'.
    # Knight will have the alias Human. 
    # Orcs' and Elves' species is the same as the character name
    # so they will still only have one entry.
    # Total of 4 entries in the registry.
    assert (len(reg2.registry) == 4)

    assert (issubclass(reg.registry['Knight'], Character))
    assert (issubclass(reg.registry['Knight'], reg.parent))


def test_init_subclass_via_registry(reg2):
    """Instantiate a subclass from the registry using a few different methods"""
    from characters.character import Knight

    def assertions(k):
        assert(k is not None)
        assert(isinstance(k, Knight))
        assert(isinstance(k, Character)) 
        assert(k.is_mortal == True)
        assert(k.name == 'knight')
        assert(k.level == 1)       

    k = reg2.Knight(name='knight', level=1)
    assertions(k)

    k = reg2.registry['Knight'](name='knight', level=1)
    assertions(k)

    k = reg2.get_class('Human')(name='knight', level=1)
    assertions(k)


def test_init_sublcass_not_in_registry(reg):
    """Behavior when trying to access a subclass that doesn't exist"""

    w = reg.get_class('Wizard')
    assert (w is None)
    
    with pytest.raises(KeyError):
        reg.registry['Wizard']

    with pytest.raises(AttributeError):
        reg.Wizard




if __name__ == '__main__':
    reg = Registry(Character)
    reg2 = Registry(Character, ['species'])
    k = reg.Knight(name='knight', level='1')
    _ = ''
    