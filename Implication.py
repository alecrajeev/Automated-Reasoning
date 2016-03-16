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

        indexL = SymbolTable.get(self.sentenceLHS.atom.name)
        indexR = SymbolTable.get(self.sentenceRHS.atom.name)

        whereL = np.where(model == indexL)[0][0]
        valueL = model[whereL][1]

        whereR = np.where(model == indexR)[0][0]
        valueR = model[whereR][1]

        if valueL == 0 or valueR == 1:
            return True
        return False
