from Symbol import Symbol
from HashTable import HashTable

class Model(object):
    """
    There will be multiple models.
    2^(SymbolCount) number of models.
    """

    def __init__(self, SymbolCount):
        self.SymbolList = np.zeros((SymbolCount,2))
        """
        Will be a 2d array where the left column is the index or key (haven't decided) of the symbol
        The right column will be it's assigned value, 1 being True, 0 being False.
        """
