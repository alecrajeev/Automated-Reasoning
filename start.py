import numpy as np
from KnowledgeBase import KnowledgeBase
from Symbol import Symbol
from Sentence import Sentence
from Implication import Implication
from Model import Model
from HashTable import HashTable

def start():
    KB = KnowledgeBase()
    
    p = KB.intern("P")
    q = KB.intern("Q")

    sentence1 = Sentence(p)
    sentence2 = Implication(p,q)

    KB.add(sentence1)
    KB.add(sentence2)

    
    



def main():
    start()

if __name__ == '__main__':
  main()