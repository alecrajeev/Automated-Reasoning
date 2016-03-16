from Symbol import Symbol
from Sentence import Sentence
from HashTable import HashTable
from ModelTable import ModelTable
from Model import Model
import numpy as np



class KnowledgeBase(object):
    def __init__(self):
        self.sentences = [] # will be a list of sentences or clauses
        self.SymbolTable = HashTable(10) # will be a HashTable that relates strings to Symbols

    def delete_last_sentence(self):
        self.sentences.pop()
    
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

    def find_KB_models(self):
        """
        This will return a list of the indexes of every model that satisfies the knowledge base
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

    def verify_alpha(self, sentence_verify):
        """
        This will return a list of the indexes of every model that satsifies the alpha sentence.
        """
        list_of_verified_models = []
        for i in xrange(0, np.size(self.model_list)):
            if sentence_verify.isSatisfiedBy(self.model_list[i].model, self.SymbolTable):
                list_of_verified_models.append(i)
        
        return list_of_verified_models

    def walk_SAT(self, p, max_flips):

        k = np.random.randint(0, len(self.model_list))

        # randomly chosen model to start
        model = self.model_list[k].model

        for i in xrange(0, max_flips):
            check = True
            list_of_unsatisfied_clauses = []
            for j in xrange(0, len(self.sentences)):
                clause_value = self.sentences[j].isSatisfiedBy(model, self.SymbolTable)
                check = check and clause_value
                if not(clause_value):
                    list_of_unsatisfied_clauses.append(j)

            if check: # a model satisfies the sentence
                print "a model satisfies the sentences"
                print model
                return True
            else:
                k = np.random.randint(0, len(list_of_unsatisfied_clauses))
                index_of_sentence = list_of_unsatisfied_clauses[k]

                list_of_symbols = self.get_all_symbols_from_sentence(self.sentences[index_of_sentence])
                list_of_symbol_ids = self.get_symbol_ids(list_of_symbols)

                if np.random.rand() < p:
                    # randomly choose a symbol in the selected clause
                    k = np.random.randint(0, len(list_of_symbols))
                    id = list_of_symbol_ids[k]
                    # flip sign of selected symbol
                    where = np.where(model == id)[0][0]
                    model[where][1] = (model[where][1] + 1) % 2
                else:
                    id_of_symbol_chosen = self.get_maximize_satisfied_clauses(list_of_symbol_ids, model)

        return "failure"

    def test(self):
        print self.walk_SAT(.5, 1000)

    def get_maximize_satisfied_clauses(self, list_of_symbol_ids, model):
        number_of_satisfied_clauses = np.zeros(len(list_of_symbol_ids), dtype=np.int16)

        for i in xrange(0, len(list_of_symbol_ids)):
            temp_model = np.copy(model)
            self.flip_sign(temp_model,list_of_symbol_ids[i])
            for j in xrange(0, len(self.sentences)):
                if self.sentences[j].isSatisfiedBy(temp_model, self.SymbolTable):
                    number_of_satisfied_clauses[i] += 1

        index_of_max = np.argmax(number_of_satisfied_clauses)
        return list_of_symbol_ids[index_of_max]


    def flip_sign(self, temp_model, id):
        where = np.where(temp_model == id)[0][0]
        temp_model[where][1] = (temp_model[where][1] + 1) % 2

    def get_symbol_ids(self, list_of_symbols):
        list_of_symbol_ids = []
        for i in xrange(0, len(list_of_symbols)):
            list_of_symbol_ids.append(self.SymbolTable.get(list_of_symbols[i]))
        return list_of_symbol_ids

    def get_all_symbols_from_sentence(self, sen):
        if sen.grammar_type < 2:
            return [sen.sentence.atom.name]
        return self.get_all_symbols_from_sentence(sen.sentenceLHS) + self.get_all_symbols_from_sentence(sen.sentenceRHS)




