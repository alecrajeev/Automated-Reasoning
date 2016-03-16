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

    def deep_copy(self):
        """
        The deep copy is used, so that when temporary models are used in walk_SAT, things are not copied over
        """
        copy = np.zeros((np.size(self.model_input)/2, 2), dtype=np.int32)
        for i in xrange(0, np.shape(self.model)[0]):
            for j in xrange(0, np.shape(self.model)[1]):
                copy[i][j] = self.model[i][j]

        return copy


