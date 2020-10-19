from helper import Helper
from ecb import ECB

'''
Block cipher
'''
class BlockCipher:
    def set_initial_from_file(self, file_name):
        self.initial = Helper.convertFileToBinary64(file_name)
        print(self.initial)
    
    def write_result_to_file(self, file_name):
        Helper.convertBinary64ToFile(self.result, file_name)
    
    def set_key(self, key):
        self.key = Helper.convertStringToBinary64(key)[0]
    
    def execute(self):
        result = []
        for byte_64 in self.initial:
            result.append(ECB.execute(byte_64, self.key))
        self.result = result

if __name__ == "__main__":
    bc = BlockCipher()
    bc.set_key("ABCDEFGH")
    bc.set_initial_from_file("test2.txt")
    bc.execute()
    bc.write_result_to_file("test3.txt")
