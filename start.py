import numpy as np
from KnowledgeBase import KnowledgeBase
from Symbol import Symbol
from Sentence import Sentence
from Model import Model
from HashTable import HashTable

def start():
    KB = KnowledgeBase()
    
    p = intern(KB,"P")
    q = intern(KB, "Q")
    KB.SymbolTable.dump()
    print KB.SymbolTable.get(p.name)


def intern(KB,name):
    k = KB.SymbolTable.get(name)
    if k == -1:
        KB.SymbolTable.put(name)
    return Symbol(name)



def main():
    start()

if __name__ == '__main__':
  main()