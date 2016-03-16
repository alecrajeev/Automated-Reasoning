from Symbol import Symbol
from Sentence import Sentence
from Model import Model
from HashTable import HashTable



class KnowledgeBase(object):
    def __init__(self):
        self.sentences = [] # will be a list of sentences
        self.SymbolTable = HashTable(10) # will be a HashTable that relates strings to Symbols
