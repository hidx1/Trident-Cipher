'''
Key Generator Class
Generates round key from external key
'''
class KeyGenerator:
    def __init__(self, init_key):
        self.key = init_key
        self.subKey = None
        self.crossKey = None
    
    def round(self):
        left_key = self.key[0:32]
        right_key = self.key[32:64]

        


