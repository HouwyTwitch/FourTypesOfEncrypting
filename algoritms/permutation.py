from string import printable
from math import ceil

def getNormalLen(textLen: int, key: list) -> int:
    fullColumns: int = textLen%len(key)
    lastNums: list = sorted(key)[fullColumns-len(key):]
    return ceil((textLen+len(lastNums))/len(key))

def basedSort(a1: list, a2: list) -> list:
    return [list(x) for x in zip(*sorted(zip(a1, a2)))][-1]

class Permutation():

    def __init__(self, key: str) -> None:
        self.alphabet = printable
        self.key: str = key
    
    def form_key(self) -> list:
        return [self.alphabet.index(s) for s in self.key]    
    
    def encrypt(self, text: str) -> list:
        if len(self.key) == 0: return text
        key: list = self.form_key()
        result: list = ['' for _ in key]
        sortedKey: list = sorted(key)
        textArr = key*(len(text)//len(key))+key[:len(text)%len(key)]
        for i in range(len(textArr)):
            result[key.index(textArr[i])] = result[key.index(textArr[i])] + text[i]           
        return ''.join([result[sortedKey.index(i)] for i in key])
        
    def decrypt(self, cryptogram: str) -> str:
        if len(self.key) == 0:
            return cryptogram
        key, sortedKey = self.form_key(), sorted(self.form_key())
        normalLen = getNormalLen(len(cryptogram), key)
        lastLen, lastKs = normalLen-1, sorted(key)[len(cryptogram)%len(key)-len(key):]
        keyArr = [([k]*normalLen if k not in lastKs else [k]*lastLen) for k in key]
        lenArr = [len(k) for k in keyArr]
        cryptogramArr = [cryptogram[sum(lenArr[:i]):sum(lenArr[0:i+1])] for i in range(len(key))]
        cryptogramArr = basedSort(key, cryptogramArr)
        result = ''
        for i in range(normalLen):
            for cryptogram in cryptogramArr:
                try: result = result + cryptogram[i]
                except: pass                  
        return result