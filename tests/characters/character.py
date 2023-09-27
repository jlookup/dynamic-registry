"""
Game characters.
Defines the Character abstract class
and the built-in characters.
"""

import abc 

class Character(abc.ABC):
    """Abstract class for characters"""

    def __init__(self, name, level):
        self.name = name 
        self.level = level

    def __repr__(self):
        """String representation of the character"""
        return f"""{self.name}: A {self.species} of level {self.level}."""

    @property
    @abc.abstractmethod 
    def species(self): 
        """Gives the character's species""" 

    @property
    @abc.abstractmethod 
    def is_mortal(self):
        """Is the character mortal"""

    def life(self): 
        """Gives the character's life duration, either mortal or immortal""" 
        return "Mortal" if self.is_mortal else "Immortal"

    def fight(self, other):
        """One character fights another. Whoever has the higher power level wins."""

        if self.level > other.level:
            self.level += 1
            other.level -= 1            
            print(f'{self.name} has defeated the {other.species} {other.name}')

        else: 
            self.level -= 1
            other.level += 1             
            print(f'{self.name} has lost to the {other.species} {other.name}')


class Knight(Character):
    """Human character type"""
    species = 'Human'
    is_mortal = True


class Orc(Character):
    """Orc character type"""
    species = 'Orc'
    is_mortal = True
