from sbox import SBox
from helper import Helper as h

'''
Key Generator Class
Generates round key from external key
'''
class KeyGenerator:
    def __init__(self, init_key, seed1, seed2):
        self.key = init_key
        self.sbox1 = SBox(seed1)
        self.sbox2 = SBox(seed2)
        self.subKey = None
        self.crossKey = None
    
    def round(self):
        # Key Split
        left_key = self.key[0:32]
        right_key = self.key[32:64]

        # Addition & Multiplication Modulo
        left_key = h.additionModulo(left_key, 2, 16, 4)
        right_key = h.multiplicationModulo(right_key, 2, 16, 4)

        # Share input
        left_key = left_key + right_key[0:16]
        right_key = right_key + left_key[0:16]

        # SBox
        left_key = self.sbox1.execute48_24(left_key)
        right_key = self.sbox2.execute48_24(right_key)

        self.subKey = left_key[0:8] + right_key[16:24]
        self.crossKey = left_key[8:24] + right_key[0:16]
        self.key = self.crossKey
        

if __name__ == "__main__":
    test_case = 'waef290e'
    test_case = h.convertStringToBinary64(test_case)[0]

    keygen = KeyGenerator(test_case, 1, 2)
    keygen.round()

    print(keygen.subKey)
    print(keygen.crossKey)


