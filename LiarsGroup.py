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
    D is Dee is a truth-teller.
    E is Eli is a truth-teller.
    F is Fay is a truth-teller.
    G is Gill is a truth-teller.
    H is Hal is a truth-teller. (not a killer AI robot, definitely not)
    I is Ida is a truth-teller.
    J is Jay is a truth-teller.
    K is Kay is a truth-teller.
    Lee is Lee is a truth-teller.
    """
    
    A = KB.intern("A")
    B = KB.intern("B")
    C = KB.intern("C")
    D = KB.intern("D")  
    E = KB.intern("E")
    F = KB.intern("F")
    G = KB.intern("G")
    H = KB.intern("H")
    I = KB.intern("I")
    J = KB.intern("J")
    K = KB.intern("K")
    L = KB.intern("L")

    KB.build_models()

    sentence1 = biconditional(unary(A), conjunction(unary(H), unary(I)))
    sentence2 = biconditional(unary(B), conjunction(unary(A), unary(L)))
    sentence3 = biconditional(unary(C), conjunction(unary(B), unary(G)))
    sentence4 = biconditional(unary(D), conjunction(unary(E), unary(L)))
    sentence5 = biconditional(unary(E), conjunction(unary(C), unary(H)))
    sentence6 = biconditional(unary(F), conjunction(unary(D), unary(I)))
    sentence7 = biconditional(unary(G), conjunction(negation(E), negation(J)))
    sentence8 = biconditional(unary(H), conjunction(negation(F), negation(K)))    
    sentence9 = biconditional(unary(I), conjunction(negation(G), negation(K)))
    sentence10 = biconditional(unary(J), conjunction(negation(A), negation(C)))
    sentence11 = biconditional(unary(K), conjunction(negation(D), negation(F)))
    sentence12 = biconditional(unary(L), conjunction(negation(B), negation(J)))

    KB.add(sentence1)
    KB.add(sentence2)
    KB.add(sentence3)
    KB.add(sentence4)
    KB.add(sentence5)
    KB.add(sentence6)
    KB.add(sentence7)
    KB.add(sentence8)
    KB.add(sentence9)
    KB.add(sentence10)
    KB.add(sentence11)
    KB.add(sentence12)


    print "Truth Table Enumeration Method"
    alpha = negation(A)
    if check_alpha(KB, alpha):
        print "The Knowledge Base entails that Amy is a liar"
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

    alpha = negation(D)
    if check_alpha(KB, alpha):
        print "The Knowledge Base entails that Dee is a liar"
    else:
        print "The Knowledge Base is inconclusive"

    alpha = negation(E)
    if check_alpha(KB, alpha):
        print "The Knowledge Base entails that Eli is a liar"
    else:
        print "The Knowledge Base is inconclusive"

    alpha = negation(F)
    if check_alpha(KB, alpha):
        print "The Knowledge Base entails that Fay is a liar"
    else:
        print "The Knowledge Base is inconclusive"

    alpha = negation(G)
    if check_alpha(KB, alpha):
        print "The Knowledge Base entails that Gill is a liar"
    else:
        print "The Knowledge Base is inconclusive"

    alpha = negation(H)
    if check_alpha(KB, alpha):
        print "The Knowledge Base entails that Hal is a liar"
    else:
        print "The Knowledge Base is inconclusive"

    alpha = negation(I)
    if check_alpha(KB, alpha):
        print "The Knowledge Base entails that Ida is a liar"
    else:
        print "The Knowledge Base is inconclusive"

    alpha = unary(J)
    if check_alpha(KB, alpha):
        print "The Knowledge Base entails that Jay is honest"
    else:
        print "The Knowledge Base is inconclusive"

    alpha = unary(K)
    if check_alpha(KB, alpha):
        print "The Knowledge Base entails that Kay is honest"
    else:
        print "The Knowledge Base is inconclusive"

    alpha = negation(L)
    if check_alpha(KB, alpha):
        print "The Knowledge Base entails that Lee is a liar"
    else:
        print "The Knowledge Base is inconclusive"

    print "\n\nWalkSAT Method"

    n = 100

    KB.add(unary(A))
    print "Inconclusive on A." if KB.walk_SAT(.5, n) else "Can likely conclude that KB entails not(A). Amy is probably a liar."
    KB.delete_last_sentence()

    KB.add(unary(B))
    print "Inconclusive on B." if KB.walk_SAT(.5, n) else "Can likely conclude that KB entails not(B). Bob is probably a liar."
    KB.delete_last_sentence()

    KB.add(unary(C))
    print "Inconclusive on C." if KB.walk_SAT(.5, n) else "Can likely conclude that KB entails not(C). Cal is probably a liar."
    KB.delete_last_sentence()

    KB.add(unary(D))
    print "Inconclusive on D." if KB.walk_SAT(.5, n) else "Can likely conclude that KB entails not(D). Dee is probably a liar."
    KB.delete_last_sentence()

    KB.add(unary(E))
    print "Inconclusive on E." if KB.walk_SAT(.5, n) else "Can likely conclude that KB entails not(E). Eli is probably a liar."
    KB.delete_last_sentence()

    KB.add(unary(F))
    print "Inconclusive on F." if KB.walk_SAT(.5, n) else "Can likely conclude that KB entails not(F). Fay is probably a liar."
    KB.delete_last_sentence()

    KB.add(unary(G))
    print "Inconclusive on G." if KB.walk_SAT(.5, n) else "Can likely conclude that KB entails not(G). Gill is probably a liar."
    KB.delete_last_sentence()

    KB.add(unary(H))
    print "Inconclusive on H." if KB.walk_SAT(.5, n) else "Can likely conclude that KB entails not(H). Fay is probably a liar."
    KB.delete_last_sentence()

    KB.add(unary(I))
    print "Inconclusive on I." if KB.walk_SAT(.5, n) else "Can likely conclude that KB entails not(I). Ida is probably a liar."
    KB.delete_last_sentence()

    KB.add(negation(J))
    print "Inconclusive on J." if KB.walk_SAT(.5, n) else "Can likely conclude that KB entails J. Jay is probably honest."
    KB.delete_last_sentence()

    KB.add(negation(K))
    print "Inconclusive on K." if KB.walk_SAT(.5, n) else "Can likely conclude that KB entails K. Kay is probably honest."
    KB.delete_last_sentence()

    KB.add(unary(L))
    print "Inconclusive on L." if KB.walk_SAT(.5, n) else "Can likely conclude that KB entails not(L). Lee is probably a liar."
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