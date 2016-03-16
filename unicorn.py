import numpy as np
from KnowledgeBase import KnowledgeBase
from HashTable import HashTable

from Symbol import Symbol
from Sentence import Sentence
from ComplexSentence import ComplexSentence

def Wumpus():
    KB = KnowledgeBase()
    
    """
    myth  = the unicorn is mythical
    mort  = the unicorn is mortal
    mamm  = the unicorn is a mammal
    horn  = the unicorn is horned
    magic = the unicorn is magical
    """

    myth = KB.intern("myth")
    magic = KB.intern("magic")
    mort = KB.intern("mort")
    mamm = KB.intern("mamm")
    horn = KB.intern("horn")

    KB.build_models()

    sentence1 = implies(unary(myth),negation(mort))
    sentence2 = implies(negation(myth), conjunction(unary(mort),unary(mamm)))
    sentence3 = implies(disjunction(negation(mort), unary(mamm)), unary(horn))
    sentence4 = implies(unary(horn), unary(magic))

    KB.add(sentence1)
    KB.add(sentence2)
    KB.add(sentence3)
    KB.add(sentence4)

    print "Can you prove the unicorn is mythical?"
    print "YES" if check_alpha(KB, unary(myth)) else "NO"

    print "Can you prove the unicorn is magical?"
    print "YES" if check_alpha(KB, unary(magic)) else "NO"

    print "Can you prove the unicorn is horned?"
    print "YES" if check_alpha(KB, unary(horn)) else "NO"

    KB.test()

def check_alpha(KB, alpha):
    models_from_KB = KB.find_KB_models()
    models_from_alpha = KB.verify_alpha(alpha)
    intersection = np.intersect1d(models_from_KB,models_from_alpha)
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
    Wumpus()

if __name__ == '__main__':
  main()