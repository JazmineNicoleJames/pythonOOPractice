"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """ Find random words from a words file. """
    file = open("words.txt", "r")
    random_line = file.readlines()
    three_lines = random_line[400:403]
    def __init__(self):
   
        print(f"{len(self.three_lines)} words read")
   
    def random(self):
        lines = [w.strip() for w in self.three_lines]
        return random.choice(lines)

        
class SpecialWordFinder:
    """Find special word that does not contain a blank-space nor a #"""
    new_file = open("subclassRandomWord.txt","r")
    
    def random(self):
        new_line = [w.strip() for w in self.new_file if w.strip() and not w.startswith('#')]
        return new_line
        return random.choice(new_line)


        

