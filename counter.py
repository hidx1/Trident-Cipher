from helper import Helper as helper

def counter(stringBlocks, keyBlock):
    counter_num = 69
    resultBlocks = []

    for i in range(len(stringBlocks)):
        counterBlock = helper.convertIntToBinary64(counter_num)
        resultBlocks.append(helper.xor(helper.xor(counterBlock, keyBlock), stringBlocks[i]))
        counter_num += 1
    
    return resultBlocks

if __name__ == "__main__":
    cipherText = counter("plaintext", "testkey")
    print(cipherText)
    plainText = counter(cipherText, "testkey")
    print(plainText)