from Symbol import Symbol
from Sentence import Sentence
import numpy as np

class Implication(Sentence):
    """
    This Sentence consists of two atoms. lhs -> rhs
    """

    def __init__(self, lhs, rhs):
        self.sentenceLHS = Sentence(lhs)
        self.sentenceRHS = Sentence(rhs)
        self.connective = 2 # connective of 2 corresponds to implies

    def isSatisfiedBy(self, model, SymbolTable):

        valueL = self.sentenceLHS.isSatisfiedBy(model, SymbolTable)
        valueR = self.sentenceRHS.isSatisfiedBy(model, SymbolTable)

        if valueL == 0 or valueR == 1:
            return True
        return False
