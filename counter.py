from helper import Helper as helper

def counter(string, key):
    counter = 69
    stringBlocks = helper.convertStringToBinary64(string)
    keyBlock = helper.convertStringToBinary64(key)[0]
    resultBlocks = []

    for i in range(len(stringBlocks)):
        counterBlock = helper.convertIntToBinary64(counter)[0]
        resultBlocks.append(helper.xor(helper.xor(counterBlock, keyBlock), stringBlock[i]))
        counter += 1
    
    return helper.convertBinary64ToString(resultBlocks)

if __name__ == "__main__":
    cipherText = counter("plaintext", "testkey")
    print(cipherText)
    plainText = counter(cipherText, "testkey")
    print(plainText)