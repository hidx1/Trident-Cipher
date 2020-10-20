from helper import Helper as helper
from keyGenerator import KeyGenerator
import numpy as np
from fFunction import fFunc

def feistel(leftBlock, rightBlock, keygen, itr):
    if (itr > 0):
        keygen.round()
        i = itr-1
        print(keygen.subKey, keygen.crossKey)
        feistel(rightBlock, helper.xor(leftBlock, fFunc(rightBlock, keygen.subKey, keygen.crossKey)), keygen, i)
    else:
        return helper.convertBinary64ToString(leftBlock + rightBlock)

if __name__ == "__main__":
    stringBlock = helper.convertStringToBinary64("abcdefgh")[0]
    left = stringBlock[:32]
    right = stringBlock[-32:]
    keyBlock = helper.convertStringToBinary64("qwertyui")[0]
    keygen = KeyGenerator(keyBlock, 1, 2)
    np.random.seed(helper.totalAsciiCode("qwertyui"))
    feistel(left, right, keygen, 8)