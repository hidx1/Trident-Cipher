from helper import Helper

import sys

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
        if mode == "ecb":
            result = self.ecb(self.initial, self.key)
        elif mode == "cbc":
            result = self.cbc(self.initial, self.key, encrypt)
        elif mode == "counter":
            result = self.counter(self.initial, self.key)

        self.result = result
    
    def ecb(self, stringBlocks, keyBlock):
        resultBlocks = []
        for block in stringBlocks:
            resultBlocks.append(Helper.xor(block, keyBlock))
        
        return resultBlocks
    
    def cbc(self, stringBlocks, keyBlock, encrypt):
        key = Helper.convertBinary64ToString([keyBlock])
        ivString = Helper.randomNChar(8, Helper.totalAsciiCode(key))
        iv = Helper.convertStringToBinary64(ivString)[0] 
        resultBlocks = []
        if (encrypt):
            for i in range(len(stringBlocks)):
                if (i == 0):
                    resultBlocks.append(Helper.xor(Helper.xor(iv, stringBlocks[i]), keyBlock))
                else:
                    resultBlocks.append(Helper.xor(Helper.xor(resultBlocks[i-1], stringBlocks[i]), keyBlock))
        else:
            for i in range(len(stringBlocks)):
                if (i == 0):
                    resultBlocks.append(Helper.xor(Helper.xor(stringBlocks[i], keyBlock), iv))
                else:
                    resultBlocks.append(Helper.xor(Helper.xor(stringBlocks[i], keyBlock), stringBlocks[i-1]))
        
        return resultBlocks
    
    def counter(self, stringBlocks, keyBlock):
        key = Helper.convertBinary64ToString([keyBlock])
        counter_num = Helper.totalAsciiCode(key)
        np.random.seed(counter_num)
        resultBlocks = []

        for i in range(len(stringBlocks)):
            counterBlock = Helper.convertIntToBinary64(counter_num)
            resultBlocks.append(Helper.xor(Helper.xor(counterBlock, keyBlock), stringBlocks[i]))
            counter_num += 1
        
        return resultBlocks

if __name__ == "__main__":
    input_name = input("Insert file name: ")
    key = input("Insert key (8 characters): ")
    if len(key) != 8:
        print("Key must be 8 characters")
        sys.exit()
    mode = input("Insert mode (ECB/CBC/Counter): ").lower()
    if not (mode == "ecb" or mode == "cbc" or mode == "counter"):
        print("Mode must either be ECB/CBC/Counter")
        sys.exit()
    encrypt = input("Is this encrypt?(Y/N) ").lower()
    output_name = input("Insert output file name: ")

    is_file = "y"
    encrypt = encrypt == "y"

    bc = BlockCipher()
    bc.set_initial(input_name, is_file)
    bc.set_key(key)
    bc.execute(mode, encrypt)
    bc.write_result(output_name, is_file)
