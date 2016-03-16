from Symbol import Symbol
from Sentence import Sentence
from Model import Model
from HashTable import HashTable



class KnowledgeBase(object):
    def __init__(self):
        self.sentences = [] # will be a list of sentences
        self.SymbolTable = HashTable(10) # will be a HashTable that relates strings to Symbols


    def intern(self,name):
        k = self.SymbolTable.get(name)
        if k == -1:
            self.SymbolTable.put(name)
        return Symbol(name)


    def add(self, sentence):
        # for now a sentence is just a simple atomic symbol
        self.sentences.append(sentence)
