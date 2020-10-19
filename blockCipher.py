from helper import Helper
from ecb import ECB
from cbc import cbc
from counter import counter

'''
Block cipher
'''
class BlockCipher:
    def set_initial(self, input_name, is_file = False):
        if (is_file):
            self.initial = Helper.convertFileToBinary64(input_name)
        else:
            self.initial = Helper.convertStringToBinary64(input_name)
    
    def write_result(self, file_name = None, is_file = False):
        if (is_file):
            Helper.convertBinary64ToFile(self.result, file_name)
        else:
            print(Helper.convertBinary64ToString(self.result))
    
    def set_key(self, key):
        self.key = Helper.convertStringToBinary64(key)[0]
    
    def execute(self, mode, encrypt=True):
        if mode == "ECB":
            result = ECB.execute(self.initial, self.key)
        elif mode == "CBC":
            result = cbc(self.initial, self.key, not encrypt)
        elif mode == "COUNTER":
            result = counter(self.initial, self.key)
        self.result = result

if __name__ == "__main__":
    input_name = input("Insert input: ")
    is_file = input("Is this a file?(Y/N) ")
    key = input("Insert key: ")
    mode = input("Insert mode: ")
    encrypt = input("Is this encrypt?(Y/N) ")
    output_name = input("Insert output (can be anything if not file): ")

    is_file = is_file == "Y"
    encrypt = encrypt == "Y"

    bc = BlockCipher()
    bc.set_initial(input_name, is_file)
    bc.set_key(key)
    bc.execute(mode, encrypt)
    bc.write_result(output_name, is_file)
