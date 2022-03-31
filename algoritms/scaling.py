from string import printable

def congruent(*args) -> list:
    codes = [args[0]]
    for i in range(args[4]):
        codes.append((args[1]*codes[-1] + args[2]) % (args[3]))
    del codes[0]
    return codes

class Scaling():
    
    def __init__(self, key: str) -> None:
        self.alphabet: str = printable
        self.key: str = key
    
    def mergeSymbols(self, maxLen: int = 3) -> str:
        keyCodes: list = [self.alphabet.index(k) for k in self.key]
        i: int = 0
        while len(keyCodes)!=maxLen:
            if len(keyCodes)<maxLen:
                keyCodes.append(int((sum(keyCodes)*len(self.alphabet)/2**len(keyCodes))%len(self.alphabet)))
            else:
                try:
                    keyCodes[i] = (keyCodes[i]+keyCodes[i+1])%len(self.alphabet)
                    del keyCodes[i+1]
                    i+=1
                except:
                    i = 0
        return keyCodes           
    
    def generateKey(self, textLen: int):
        keyCodes: list = self.mergeSymbols()
        return congruent(keyCodes[0], keyCodes[1], keyCodes[2], len(self.alphabet), textLen)   
    
    def encrypt(self, text: str) -> str:
        key: list = self.generateKey(len(text))
        textCodes: list = [self.alphabet.index(s) for s in text]
        return ''.join([self.alphabet[(textCodes[i]+key[i])%len(self.alphabet)] for i in range(len(text))])
    
    def decrypt(self, cryptogram: str) -> str:
        key: list = self.generateKey(len(cryptogram))
        textCodes: list = [self.alphabet.index(s) for s in cryptogram]
        return ''.join([self.alphabet[(len(self.alphabet)+textCodes[i]-key[i])%len(self.alphabet)] for i in range(len(cryptogram))])