import numpy as np
from KnowledgeBase import KnowledgeBase
from Symbol import Symbol
from Sentence import Sentence
from Implication import Implication
from Model import Model
from HashTable import HashTable

def ModusPonens():
    KB = KnowledgeBase()
    
    p = KB.intern("P")
    q = KB.intern("Q")
    k = KB.intern("K")
    J = KB.intern("J")

    sentence1 = Sentence(p)
    sentence2 = Implication(p,q)

    KB.add(sentence1)
    KB.add(sentence2)

    scount = KB.SymbolTable.key_count
    symbol_int_list = KB.SymbolTable.list_of_ints

    M = Model(scount, symbol_int_list)
    # print symbol_int_list

    print M.ModelTable

    
    



def main():
    ModusPonens()

if __name__ == '__main__':
  main()