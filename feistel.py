from helper import Helper as helper
from keyGenerator import KeyGenerator as keygen
import numpy as np
from fFunction import fFunc

def feistel(leftBlock, rightBlock, keygen, itr):
    if (itr > 0):
        # print(itr)
        keygen.round()
        i = itr-1
        print(keygen.subKey, keygen.crossKey)
        feistel(rightBlock, helper.xor(leftBlock, fFunc(rightBlock, keygen.subKey, keygen.crossKey)), keygen, i)
    else:
        # print(itr)
        return helper.convertBinary64ToString(leftBlock + rightBlock)

if __name__ == "__main__":
    stringBlock = helper.convertStringToBinary64("abcdefgh")[0]
    left = stringBlock[:32]
    right = stringBlock[-32:]
    keyBlock = helper.convertStringToBinary64("qwertyui")[0]
    keygen = keygen(keyBlock, 1, 2)
    np.random.seed(helper.totalAsciiCode("qwertyui"))
    feistel(left, right, keygen, 8)