from helper import Helper as helper

def feistel(leftBlock, rightBlock):
    # return rightBlock, helper.xor(leftBlock, function(rightBlock, key))

if __name__ == "__main__":
    stringBlock = helper.convertStringToBinary64("abcdefgh")[0]
    left = stringBlock[:32]
    right = stringBlock[-32:]
    feistel(left, right)