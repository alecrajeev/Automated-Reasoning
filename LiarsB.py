import numpy as np
from KnowledgeBase import KnowledgeBase
from Symbol import Symbol
from HashTable import HashTable
from Sentence import Sentence
from ComplexSentence import ComplexSentence

diagnostics = False

def Liar():
    KB = KnowledgeBase()

    """
    A is Amy is a truth-teller.
    B is Bob is a truth-teller.
    C is Cal is a truth-teller.
    """
    
    A = KB.intern("A")
    B = KB.intern("B")
    C = KB.intern("C")

    KB.build_models()

    sentence1 = biconditional(unary(A), negation(C))
    sentence2 = biconditional(unary(B), conjunction(negation(A),negation(C)))
    sentence3 = biconditional(unary(C), unary(B))

    KB.add(sentence1)
    KB.add(sentence2)
    KB.add(sentence3)

    print "Truth Table Enumeration Method"
    alpha = unary(A)
    if check_alpha(KB, alpha):
        print "The Knowledge Base entails that Amy is honest"
    else:
        print "The Knowledge Base is inconclusive"
    
    alpha = negation(B)
    if check_alpha(KB, alpha):
        print "The Knowledge Base entails that Bob is a liar"
    else:
        print "The Knowledge Base is inconclusive"
    
    alpha = negation(C)
    if check_alpha(KB, alpha):
        print "The Knowledge Base entails that Cal is a liar"
    else:
        print "The Knowledge Base is inconclusive"

    print "\n\nWalkSAT Method"

    KB.add(negation(A))
    print "Inconclusive on A." if KB.walk_SAT(.5, 10000) else "Can likely conclude that KB entails A. Amy is probably honest."
    KB.delete_last_sentence()

    KB.add(unary(B))
    print "Inconclusive on B." if KB.walk_SAT(.5, 10000) else "Can likely conclude that KB entails not(B). Bob is probably a liar."
    KB.delete_last_sentence()

    KB.add(unary(C))
    print "Inconclusive on C." if KB.walk_SAT(.5, 10000) else "Can likely conclude that KB entails not(C). Cal is probably a liar."
    KB.delete_last_sentence()

def check_alpha(KB, alpha):
    """
    This finds the models that satisy the Knowledge Base.
    This finds the models that satisy alpha.
    Then checks if models(KB) is a subset of models(alpha).
    If this is true, then KB entails alpha.
    Else, inconclusive.
    """

    models_from_KB = KB.find_KB_models()
    models_from_alpha = KB.verify_alpha(alpha)
    intersection = np.intersect1d(models_from_KB,models_from_alpha)
    if diagnostics:
        print "index of models from Knowledge Base"
        print models_from_KB
        print "index of models from alpha"
        print models_from_alpha
        print "intersection of those two"
        print intersection

    if np.size(intersection) == np.size(models_from_KB):
        return True
    else:
        return False

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
    Liar()

if __name__ == '__main__':
  main()