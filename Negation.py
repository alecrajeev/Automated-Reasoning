from Symbol import Symbol
import numpy as np

class Negation(object):
    """
    This basic Sentence just consists of a single atom
    """

    def __init__(self, atom):
        self.atom = atom

    def isSatisfiedBy(self, model, SymbolTable):
        index = SymbolTable.get(self.atom.name)

        where = np.where(model == index)[0][0]
        value = model[where][1]
        
        if value == 0:
            return True
        else:
            return False
