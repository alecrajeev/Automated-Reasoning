from Symbol import Symbol
import numpy as np

class Sentence(object):
    """
    This basic Sentence just consists of a single atom
    """

    def __init__(self, atom):
        self.atom = atom

    def isSatisfiedBy(self, model, SymbolTable):
        print model
        print self.atom.name
        index = SymbolTable.get(self.atom.name)

        where = np.where(model == index)[0][0]
        value = model[where][1]
        print value
        
        if value == 1:
            return True
        else:
            return False
