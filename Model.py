from Symbol import Symbol
from HashTable import HashTable
import numpy as np

class Model(object):
    """
    There will be multiple models.
    The first column of is 2^SymbolCount number of models
    The second column will represent that symbol's id number
    The third column will represent that symbol's assigned value for that particular model
    """

    def __init__(self, SymbolCount, symbol_int_list):
        self.models_count = 2**SymbolCount
        self.ModelTable = np.zeros((self.models_count,SymbolCount*2), dtype=np.int16)
        self.symbol_int_list = symbol_int_list
        for i in xrange(0, np.size(symbol_int_list)):
            self.ModelTable[:, i] = symbol_int_list[i]

        for i in xrange(0, self.models_count):
            for j in xrange(0, SymbolCount):
                if i % 2**(j+1) < 2**j:
                    self.ModelTable[i, SymbolCount+j] = 1
                else:
                    self.ModelTable[i, SymbolCount+j] = 0


        # for i in xrange(0, self.models_count):
        #     for j in xrange(0, SymbolCount):
        #         if i % 2**(j+1) < 2**j:
        #             self.ModelTable[i, SymbolCount+((j+2) % 3)] = 1
        #         else:
        #             self.ModelTable[i, SymbolCount+((j+2) % 3)] = 0

        # for i in xrange(0, self.models_count):
        #     if i % 8 < 4:
        #         self.ModelTable[i, SymbolCount] = 1
        #     else:
        #         self.ModelTable[i, SymbolCount] = 0
        #     if i % 4 < 2:
        #         self.ModelTable[i, SymbolCount+1] = 1
        #     else:
        #         self.ModelTable[i, SymbolCount+1] = 0
        #     if i % 2 < 1:
        #         self.ModelTable[i, SymbolCount+2] = 1
        #     else:
        #         self.ModelTable[i, SymbolCount+2] = 0

        # for i in xrange(0, self.models_count):
        #     if i / 2 == 0:
        #         self.ModelTable[i, 2] = 1
        #     else:
        #         self.ModelTable[i, 2] = 0
        #     if i % 2 == 0:
        #         self.ModelTable[i, 3] = 1
        #     else:
        #         self.ModelTable[i, 3] = 0


