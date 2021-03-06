import numpy as np
from KnowledgeBase import KnowledgeBase
from Symbol import Symbol
from HashTable import HashTable
from Sentence import Sentence
from ComplexSentence import ComplexSentence

def ModusPonens():
    KB = KnowledgeBase()
    
    p = KB.intern("P")
    q = KB.intern("Q")

    KB.build_models()

    sentence1 = unary(p)
    sentence2 = implies(unary(p), unary(q))

    KB.add(sentence1)
    KB.add(sentence2)

    print "Truth Table Enumeration Method"
    print "Models that satisfy the Knowledge Base:"
    models_from_KB = KB.find_KB_models()
    print models_from_KB

    alpha = unary(q)

    print "Models that satisfy alpha:"
    models_from_alpha = KB.verify_alpha(alpha)
    print models_from_alpha

    intersection = np.intersect1d(models_from_KB,models_from_alpha)

    print "Models that satisfy both of the two previous ones"
    print intersection
    print ""

    print "Does KB entail alpha?"
    if np.size(intersection) == np.size(models_from_KB):
        print "YES, because Models(KnowledgeBase) is a subset of Models(alpha)"
    else:
        print "NO, because Models(KnowledgeBase) is NOT a subset of Models(alpha). It is inconclusive."

    print "\nWalkSAT Method"

    KB.add(negation(q))
    print "Is there a model that satisfies all sentences after trying 10,000 times?"
    print "YES. Thus it is inconclusive." if KB.walk_SAT(.5,10000) else "NO. Since no model was found in the alloted trials, " + \
    "it is likely that no model exists that satifies all the sentences. Therefore one can conclude " + \
    "it is most likely that the Know Base entails the alpha. \nThus KB entails q (probably)"


def unary(p):
    return ComplexSentence(0,[p])

def negation(p):
    return ComplexSentence(1, [p])

def conjunction(p,q):
    return ComplexSentence(2,[p,q])

def disjunction(p,q):
    return ComplexSentence(3,[p,q])
    
def implies(p,q):
    return ComplexSentence(4,[p,q])

def biconditional(p,q):
    return ComplexSentence(5,[p,q])



def main():
    ModusPonens()

if __name__ == '__main__':
  main()