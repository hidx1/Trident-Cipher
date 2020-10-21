from helper import Helper as helper
from keyGenerator import KeyGenerator
import numpy as np
from fFunction import fFunc

def feistel(leftBlock, rightBlock, sKeyList, xKeyList, encrypt, itr):
    if (encrypt):
        sKey = sKeyList[itr]
        xKey = xKeyList[itr]
    else:
        sKey = sKeyList[7-itr]
        xKey = xKeyList[7-itr]
    
    fFunc_res = fFunc(rightBlock, sKey, xKey)
        
    return rightBlock, helper.xor(leftBlock, fFunc_res)

if __name__ == "__main__":
    stringBlock = helper.convertStringToBinary64("abcdefgh")[0]
    left = stringBlock[:32]
    right = stringBlock[-32:]
    keyBlock = helper.convertStringToBinary64("qwertyui")[0]
    keygen = KeyGenerator(keyBlock, 1, 2)

    sKeyList = []
    xKeyList = []

    for i in range(8):
        keygen.round()
        sKeyList.append(keygen.subKey)
        xKeyList.append(keygen.crossKey)

    np.random.seed(helper.totalAsciiCode("qwertyui"))
    encrypt = True

    for i in range(8):
        left, right = feistel(left, right, sKeyList, xKeyList, encrypt, i)
    
    temp = left
    left = right
    right = temp

    print(helper.convertBinary64ToString([left + right]))

    stringBlock = left + right
    left = stringBlock[:32]
    right = stringBlock[-32:]
    keyBlock = helper.convertStringToBinary64("qwertyui")[0]
    keygen2 = KeyGenerator(keyBlock, 1, 2)

    sKeyList = []
    xKeyList = []

    for i in range(8):
        keygen2.round()
        sKeyList.append(keygen2.subKey)
        xKeyList.append(keygen2.crossKey)

    np.random.seed(helper.totalAsciiCode("qwertyui"))
    encrypt = False

    for i in range(8):
        left, right = feistel(left, right, sKeyList, xKeyList, encrypt, i)
    
    temp = left
    left = right
    right = temp
    
    print(helper.convertBinary64ToString([left + right]))
