from Symbol import Symbol
from Sentence import Sentence
import numpy as np

class ComplexSentence(object):
    """
    This Sentence consists of two atoms. lhs <-> rhs
    """

    def __init__(self, grammar_type, parts):
        self.grammar_type = grammar_type
        if self.grammar_type < 2:
            self.sentence = Sentence(parts[0])
        else:
            self.sentenceLHS = parts[0]
            self.sentenceRHS = parts[1]

    def isSatisfiedBy(self, model, SymbolTable):
        """
        This checks whether a particular model will be satisfied by that sentence.
        If the grammar_type < 2, then it's just a simple unary sentence.
        If the grammar_type >= 2, then it's a compound sentence and recusively calls the lhs and rhs.
        The grammar_type will also specify whether it is and, or, implication, etc.
        """

        if self.grammar_type < 2: # unary 
            if self.grammar_type == 0: # positive
                return self.sentence.isSatisfiedBy(model, SymbolTable)
            else: # negative
                return (1 + self.sentence.isSatisfiedBy(model, SymbolTable)) % 2
        else:
            if self.grammar_type == 2: # conjuntion (and)
                return self.sentenceLHS.isSatisfiedBy(model, SymbolTable) and self.sentenceRHS.isSatisfiedBy(model, SymbolTable)
            if self.grammar_type == 3: # disjuntion (or)
                return self.sentenceLHS.isSatisfiedBy(model, SymbolTable) or self.sentenceRHS.isSatisfiedBy(model, SymbolTable)
            if self.grammar_type == 4: # implies
                return not (self.sentenceLHS.isSatisfiedBy(model, SymbolTable)) or self.sentenceRHS.isSatisfiedBy(model, SymbolTable)
            if self.grammar_type == 5: # biconditional
                return self.sentenceLHS.isSatisfiedBy(model, SymbolTable) == self.sentenceRHS.isSatisfiedBy(model, SymbolTable)