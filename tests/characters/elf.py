"""A new character that extends the characters collection."""

from .character import Character

class Elf(Character):
    """Elf character type"""
    species = 'Elf'
    is_mortal = False
