from Symbol import Symbol

class Sentence(object):
    """
    This basic Sentence just consists of a single atom
    """

    def __init__(self, atom):
        self.atom = atom

    def isSatisfiedBy(self, model):
        return true
