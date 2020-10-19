from helper import Helper

'''
Enkripsi filter
Pada enkripsi ini. Hanya dilakukan XOR dengan Key
'''
class SimpleCrypt:
    @staticmethod
    def execute(key, source):
        print("Key =", key)
        print("Source =", source)
        return Helper.xor(key, source)
        
    