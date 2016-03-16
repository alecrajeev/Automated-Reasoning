import numpy as np
from KnowledgeBase import KnowledgeBase
from HashTable import HashTable

from Symbol import Symbol
from Sentence import Sentence
from Implication import Implication
from Negation import Negation
from Biconditional import Biconditional
from Disjunction import Disjunction
from Conjunction import Conjunction

def Wumpus():
    KB = KnowledgeBase()
    
    p11 = KB.intern("P1,1")
    p12 = KB.intern("P1,2")
    p21 = KB.intern("P2,1")
    p22 = KB.intern("P2,2")
    p31 = KB.intern("P3,1")
    b11 = KB.intern("B1,1")
    b21 = KB.intern("B2,1")

    KB.build_models()

    sentence1 = Negation(p11)
    sentence2 = Biconditional(b11, Disjunction(p12, p21))
    sentence3 = Biconditional(b21, Disjunction(p12, Disjunction(p22, p31)))
    sentence4 = Negation(b11)
    sentence5 = Sentence(b21)

    KB.add(sentence1)
    KB.add(sentence2)
    KB.add(sentence3)
    KB.add(sentence4)
    KB.add(sentence5)    

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
    Wumpus()

if __name__ == '__main__':
  main()