from string import printable
from random import choice

def split_by_n(seq: str, n: int) -> list:
    return [seq[i*n:(i+1)*n] for i in range(len(seq)//n)] + [seq[len(seq)//n*n:]]

def intToNum(i: int, length: int = 4) -> str:
    return '0'*(length-len(str(i))) + str(i)

class Homophonic():
    
    def __init__(self, key: str) -> None:
        self.alphabet: str = printable
        self.key: str = key
    
    def keyToInt(self) -> int:
        keyCodes: list = [self.alphabet.index(k) for k in self.key]
        result: int = 1
        for i in range(len(keyCodes)):
            result *= keyCodes[i]+1
        return result%(8192-len(self.alphabet)) + len(self.alphabet)
    
    def generateHomDict(self) -> dict:
        values = [intToNum(i) for i in range(self.keyToInt())]  
        d = {}
        i = 0
        while i < len(values):
            for s in self.alphabet:
                try:
                    d[s].append(values[i])
                except:
                    d[s] = [values[i]]
                i+=1
                if i >= len(values):
                    break
        return d
    
    def encrypt(self, text: str) -> str:
        homDict: dict = self.generateHomDict()
        return ''.join([choice(homDict[s]) for s in text])
    
    def decrypt(self, cryptogram: str) -> str:
        homDict: dict = self.generateHomDict()
        text = ""
        for symbol in split_by_n(cryptogram, 4):
            for key in homDict:
                if symbol in homDict[key]:
                    text += key
        return text