from string import printable

class Vigenere():
    
    def __init__(self, key: str) -> None:
        self.alphabet = printable
        if len(key) >= 1:
            self.key: str = key
        else:
            self.key: str = ''
    
    @staticmethod
    def form_key(text: str, key: str) -> str:
        lenKey, lenText = len(key), len(text)
        return key[:lenText] if lenKey>=lenText else key*(lenText//lenKey) + key[:lenText%lenKey]           
    
    def encrypt(self, text: str) -> str:
        if len(self.key) == 0:
            return text
        tempKey = self.form_key(text, self.key)
        textArr, keyArr = [self.alphabet.index(i) for i in text], [self.alphabet.index(i) for i in tempKey]
        cryptogram = [self.alphabet[(textArr[i]+keyArr[i])%len(self.alphabet)] for i in range(len(textArr))]
        return ''.join(cryptogram)
        
    def decrypt(self, cryptogram: str) -> str:
        if len(self.key) == 0:
            return cryptogram
        tempKey = self.form_key(cryptogram, self.key)
        textArr, keyArr = [self.alphabet.index(i) for i in cryptogram], [self.alphabet.index(i) for i in tempKey]
        text = [self.alphabet[(len(self.alphabet)+textArr[i]-keyArr[i])%len(self.alphabet)] for i in range(len(textArr))]
        return ''.join(text)