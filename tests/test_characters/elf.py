"""A new character that extends the characters collection."""

from .character import Character, Life


class Immortal(Life):
    def is_mortal(self):
        return False


class Elf(Character):
    """Elf character type"""
    species = 'Elf'
    life = Immortal()


