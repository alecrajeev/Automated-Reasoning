from Symbol import Symbol
from Sentence import Sentence
import numpy as np

class Disjunction(Sentence):
    """
    This Sentence consists of two atoms. lhs or rhs
    """

    def __init__(self, lhs, rhs):
        self.sentenceLHS = Sentence(lhs)
        self.sentenceRHS = Sentence(rhs)
        self.connective = 1 # connective of 2 corresponds to implies

    def isSatisfiedBy(self, model, SymbolTable):

        valueL = self.sentenceLHS.isSatisfiedBy(model, SymbolTable)
        valueR = self.sentenceRHS.isSatisfiedBy(model, SymbolTable)

        if valueL == 1 or valueR == 1:
            return True
        return False
