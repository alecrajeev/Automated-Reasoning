from Symbol import Symbol
from HashTable import HashTable
import numpy as np

class Model(object):
    """
    This will represent one specific model
    """

    def __init__(self, model_input):
        self.model_input = model_input
        self.model = np.zeros((np.size(model_input)/2, 2), dtype=np.int32)
        for i in xrange(0, np.size(model_input)/2):
            self.model[i][0] = model_input[i]
            self.model[i][1] = model_input[i + np.size(model_input)/2]


