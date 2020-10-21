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
        
    return rightBlock, helper.xor(leftBlock, fFunc(rightBlock, sKey, xKey))

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
    
    print(helper.convertBinary64ToString([left + right]))