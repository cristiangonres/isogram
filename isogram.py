"""Verify isogram"""
from string import ascii_lowercase

def is_isogram(string: str) -> bool:
    """check if any letter is repeat"""
    world = [letter for letter in string.lower() if letter in ascii_lowercase]
    return len(set(world)) == len(world)
