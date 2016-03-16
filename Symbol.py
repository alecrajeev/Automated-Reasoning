

class Symbol(object):
    def __init__(self, name):
        self.name = name
        # this symbol will have a value in a particular model

    def equals(self, a):
        if a is None:
            return False
        elif self.name == a.name:
            return True
        else:
            return False