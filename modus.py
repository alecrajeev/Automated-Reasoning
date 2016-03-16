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
    # k = KB.intern("K")
    # j = KB.intern("J")

    KB.build_models()

    sentence1 = unary(p)
    sentence2 = implies(p,q)

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
        print "NO, because Models(KnowledgeBase) is NOT a subset of Models(alpha)"

    print "\nWalkSAT Method"

    KB.add(alpha)
    print "Is there a model that satisfies all sentences after trying 10,000 times?"
    print "YES" if KB.walk_SAT(.5,10000) else "NO"


def unary(p):
    return ComplexSentence(0,[p])

def negation(p):
    return ComplexSentence(1, [p])

def conjuntion(p,q):
    return ComplexSentence(2,[ComplexSentence(0,[p]),ComplexSentence(0,[q])])

def disjuntion(p,q):
    return ComplexSentence(3,[ComplexSentence(0,[p]),ComplexSentence(0,[q])])
    
def implies(p,q):
    return ComplexSentence(4,[ComplexSentence(0,[p]),ComplexSentence(0,[q])])

def biconditional(p,q):
    return ComplexSentence(5,[ComplexSentence(0,[p]),ComplexSentence(0,[q])])



def main():
    ModusPonens()

if __name__ == '__main__':
  main()