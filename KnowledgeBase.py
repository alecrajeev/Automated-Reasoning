from Symbol import Symbol
from Sentence import Sentence
from HashTable import HashTable
from ModelTable import ModelTable
from Model import Model



class KnowledgeBase(object):
    def __init__(self):
        self.sentences = [] # will be a list of sentences
        self.SymbolTable = HashTable(10) # will be a HashTable that relates strings to Symbols
    
    def build_models(self):
        scount = self.SymbolTable.key_count
        symbol_int_list = self.SymbolTable.list_of_ints
        self.ModelTable = ModelTable(scount, symbol_int_list)
        
        self.model_list = [None]*(2**scount)
        for i in xrange(0, 2**scount):
            self.model_list[i] = Model(self.ModelTable.Table[i])


    def intern(self,name):
        k = self.SymbolTable.get(name)
        if k == -1:
            self.SymbolTable.put(name)
        return Symbol(name)


    def add(self, sentence):
        # for now a sentence is just a simple atomic symbol
        self.sentences.append(sentence)

    def check_models(self, k):
        # print self.model_list[k].model
        print self.sentences[0].isSatisfiedBy(self.model_list[k].model, self.SymbolTable)

