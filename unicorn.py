import numpy as np
from KnowledgeBase import KnowledgeBase
from HashTable import HashTable
from Symbol import Symbol
from Sentence import Sentence
from ComplexSentence import ComplexSentence

def Unicorn():
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

    print "Truth Table Enumeration"
    print "Can you prove the unicorn is mythical?"
    print "\nYES. You can prove the unicorn is mythical. Since models(KB) is a subset of models(alpha)" if check_alpha(KB, unary(myth)) \
    else "\nNO. You cannot prove the unicorn is mythical. Since models(KB) is not a subset of models(alpha). It is inconclusive."

    print "\nCan you prove the unicorn is magical?"
    print "\nYES. You can prove the unicorn is magical. Since models(KB) is a subset of models(alpha)" if check_alpha(KB, unary(magic)) \
    else "\nNO. You cannot prove the unicorn is magical. Since models(KB) is not a subset of models(alpha). It is inconclusive."

    print "\nCan you prove the unicorn is horned?"
    print "\nYES. You can prove the unicorn is horned. Since models(KB) is a subset of models(alpha)" if check_alpha(KB, unary(horn)) \
    else "\nNO. You cannot prove the unicorn is horned. Since models(KB) is not a subset of models(alpha). It is inconclusive."

    print "\n\nWalkSAT Method"
    print "\nIs there a model that satisfies all sentences after trying 10,000 times for unicorn being mythical?"
    KB.add(negation(myth))
    print "YES. Since there is a model that satifies all the sentences, so you can NOT concluded that the Knowledge Base entails alpha." +\
    " Thus you can NOT conclude that the unicorn is mythical. It is inconclusive." if KB.walk_SAT(.5,10000) else "NO. Since no model was found in the alloted trials, " + \
    "it is likely that no model exists that satifies all the sentences. Therefore one can conclude " + \
    "it is most likely that the Know Base entails the alpha. \nThus the unicorn is mythical (probably)"
    KB.delete_last_sentence()

    print "\nIs there a model that satisfies all sentences after trying 10,000 times for unicorn being magical?"
    KB.add(negation(magic))
    print "YES. Since there is a model that satifies all the sentences, so you can NOT concluded that the Knowledge Base entails alpha." +\
    " Thus you can NOT conclude that the unicorn is magical. It is inconclusive." if KB.walk_SAT(.5,10000) else "NO. Since no model was found in the alloted trials, " + \
    "it is likely that no model exists that satifies all the sentences. Therefore one can conclude " + \
    "it is most likely that the Know Base entails the alpha. \nThus the unicorn is magical (probably)"
    KB.delete_last_sentence()

    print "\nIs there a model that satisfies all sentences after trying 10,000 times for unicorn being horned?"
    KB.add(negation(horn))
    print "YES. Since there is a model that satifies all the sentences, so you can NOT concluded that the Knowledge Base entails alpha." +\
    " Thus you can NOT conclude that the unicorn is horned. It is inconclusive." if KB.walk_SAT(.5,10000) else "NO. Since no model was found in the alloted trials, " + \
    "it is likely that no model exists that satifies all the sentences. Therefore one can conclude " + \
    "it is most likely that the Know Base entails the alpha. \nThus the unicorn is horned (probably)"
    KB.delete_last_sentence()

def check_alpha(KB, alpha):
    models_from_KB = KB.find_KB_models()
    print "index of models from Knowledge Base"
    print models_from_KB

    models_from_alpha = KB.verify_alpha(alpha)
    print "index of models from alpha"
    print models_from_alpha

    intersection = np.intersect1d(models_from_KB,models_from_alpha)
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
    Unicorn()

if __name__ == '__main__':
  main()