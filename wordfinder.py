"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """ Find random words from a words file.
        >>> wf = WordFinder("words.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, filepath):
        """Opens a file, reads, and returns a string of the total words read"""
        file = open(filepath)
        self.random_line = file.readlines()
        print(f"{len(self.random_line)} words read")
    
    def random(self):
        """ Strips any blank-space from words, and returns a random word"""
        lines = [w.strip() for w in self.random_line]
        return random.choice(lines)

        
class SpecialWordFinder(WordFinder):
    """Find special word that does not contain a blank-space nor a #"""

    def random(self):
        new_line = [w.strip() for w in self.random_line if w.strip() and not w.startswith('#')]
        return random.choice(new_line)


        

