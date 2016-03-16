from Symbol import Symbol
from Sentence import Sentence

class Implication(Sentence):
    """
    This basic Sentence just consists of a single atom
    """

    def __init__(self, lhs, rhs):
        self.sentenceLHS = Sentence(lhs)
        self.sentenceRHS = Sentence(rhs)
        self.connective = 2 # connective of 2 corresponds to implies

    def isSatisfiedBy(self, model):
        return true
