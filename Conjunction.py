from Symbol import Symbol
from Sentence import Sentence
import numpy as np

class Conjunction(Sentence):
    """
    This Sentence consists of two atoms. lhs and rhs
    """

    def __init__(self, lhs, rhs):
        self.sentenceLHS = Sentence(lhs)
        self.sentenceRHS = Sentence(rhs)
        self.connective = 0 # connective of 2 corresponds to implies

    def isSatisfiedBy(self, model, SymbolTable):

        valueL = self.sentenceLHS.isSatisfiedBy(model, SymbolTable)
        valueR = self.sentenceRHS.isSatisfiedBy(model, SymbolTable)

        if valueL == 1 and valueR == 1:
            return True
        return False
