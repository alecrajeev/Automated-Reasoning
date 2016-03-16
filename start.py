import numpy as np
from KnowledgeBase import KnowledgeBase
from Symbol import Symbol
from Sentence import Sentence
from Implication import Implication
from HashTable import HashTable

def ModusPonens():
    KB = KnowledgeBase()
    
    p = KB.intern("P")
    q = KB.intern("Q")
    # k = KB.intern("K")
    # j = KB.intern("J")

    KB.build_models()

    sentence1 = Sentence(p)
    sentence2 = Implication(p,q)

    KB.add(sentence1)
    KB.add(sentence2)

    print KB.check_models()
    
    



def main():
    ModusPonens()

if __name__ == '__main__':
  main()