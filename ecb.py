from simpleCrypt import SimpleCrypt

'''
ECB Class
'''
class ECB:
    @staticmethod
    def execute(plain, key):
        return SimpleCrypt.execute(key, plain)