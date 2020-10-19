from helper import Helper as helper

def cbc(stringBlocks, keyBlock, mode):
    iv = helper.convertStringToBinary64("abcdefgh")[0]
    resultBlocks = []

    if (mode == 0): #encrypt
        for i in range(len(stringBlocks)):
            if (i == 0):
                resultBlocks.append(helper.xor(helper.xor(iv, stringBlocks[i]), keyBlock))
            else:
                resultBlocks.append(helper.xor(helper.xor(resultBlocks[i-1], stringBlocks[i]), keyBlock))
        
    else: #decrypt
        for i in range(len(stringBlocks)):
            if (i == 0):
                resultBlocks.append(helper.xor(helper.xor(stringBlocks[i], keyBlock), iv))
            else:
                resultBlocks.append(helper.xor(helper.xor(stringBlocks[i], keyBlock), stringBlocks[i-1]))
    
    return resultBlocks

if __name__ == "__main__":
    cipherText = cbc("plaintext", "testkey", 0)
    print(cipherText)
    plainText = cbc(cipherText, "testkey", 1)
    print(plainText)