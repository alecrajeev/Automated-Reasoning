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

    print "Models that satisfy the Knowledge Base:"
    models_from_KB = KB.find_KB_models()
    print models_from_KB

    alpha = Sentence(q)

    print "Models that satisfy alpha:"
    models_from_alpha = KB.verify(alpha)
    print models_from_alpha

    intersection = np.intersect1d(models_from_KB,models_from_alpha)

    print "Models that satisfy both of the two previous ones"
    print intersection
    print ""

    print "Does KB entail alpha?"
    if np.size(intersection) == np.size(models_from_KB):
        print "YES, because Models(KnowledgeBase) is a subset of Models(alpha)"
    else:
        print "NO, because Models(KnowledgeBase) is NOT a subset of Models(alpha)"
    
    



def main():
    ModusPonens()

if __name__ == '__main__':
  main()