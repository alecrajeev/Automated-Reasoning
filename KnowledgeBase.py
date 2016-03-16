from Symbol import Symbol
from Sentence import Sentence
from HashTable import HashTable
from ModelTable import ModelTable
from Model import Model
import numpy as np



class KnowledgeBase(object):
    def __init__(self):
        self.sentences = [] # will be a list of sentences
        self.SymbolTable = HashTable(10) # will be a HashTable that relates strings to Symbols
    
    def build_models(self):
        """
        This will build every possible model where there are 2^n number of models
        """
        scount = self.SymbolTable.key_count
        symbol_int_list = self.SymbolTable.list_of_ints
        self.ModelTable = ModelTable(scount, symbol_int_list)
        
        self.model_list = [None]*(2**scount)
        for i in xrange(0, 2**scount):
            self.model_list[i] = Model(self.ModelTable.Table[i])


    def intern(self,name):
        """
        This places a specific symbol into a HashTable that makes it easier to verify equality
        """

        k = self.SymbolTable.get(name)
        if k == -1:
            self.SymbolTable.put(name)
        return Symbol(name)


    def add(self, sentence):
        """
        This will add a sentence to the knowledge base.
        A more complicated sentence like a implication is added also using this.
        """
        self.sentences.append(sentence)

    def test(self):
        print self.sentences[1].grammar_type
        print self.sentences[1].sentenceLHS.grammar_type
        print self.sentences[1].sentenceRHS.grammar_type

        # print self.sentences[1].sentenceRHS.isSatisfiedBy(self.model_list[2].model, self.SymbolTable)
        print self.sentences[1].isSatisfiedBy(self.model_list[2].model, self.SymbolTable)

    def find_KB_models(self):
        """
        This will return a list of the index of every model that satisfies the knowledge base
        """
        list_of_verified_models = []
        for i in xrange(0, np.size(self.model_list)):
            check = True
            for j in xrange(0, len(self.sentences)):
                if check:
                    check = check and self.sentences[j].isSatisfiedBy(self.model_list[i].model, self.SymbolTable)
            if check:
                list_of_verified_models.append(i)
        return list_of_verified_models

    def verify(self, sentence_verify):
        list_of_verified_models = []
        for i in xrange(0, np.size(self.model_list)):
            if sentence_verify.isSatisfiedBy(self.model_list[i].model, self.SymbolTable):
                list_of_verified_models.append(i)
        
        return list_of_verified_models

