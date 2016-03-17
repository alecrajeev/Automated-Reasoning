from Symbol import Symbol
from HashTable import HashTable
import numpy as np

class ModelTable(object):
    """
    There will be 2^n models.
    The first SymbolCount number of columns is that symbol's id.
    The second set of SymbolCount columns is that symbol's value for a specific id.
    Essentially each row in Table is a separate model, so 2^n rows.
    """

    def __init__(self, SymbolCount, symbol_int_list):
        self.models_count = 2**SymbolCount
        self.Table = np.zeros((self.models_count,SymbolCount*2), dtype=np.int16)
        self.symbol_int_list = symbol_int_list
        for i in xrange(0, np.size(symbol_int_list)):
            self.Table[:, i] = symbol_int_list[i]

        for i in xrange(0, self.models_count):
            for j in xrange(0, SymbolCount):
                if i % 2**(j+1) < 2**j:
                    self.Table[i, SymbolCount+j] = 1
                else:
                    self.Table[i, SymbolCount+j] = 0


