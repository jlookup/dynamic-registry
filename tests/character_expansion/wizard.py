"""A new character that extends the characters collection."""

from characters.character import Character

class Wizard(Character):
    """Wizard character type"""
    species = 'Human'
    is_mortal = True
