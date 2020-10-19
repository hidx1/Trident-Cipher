from simpleCrypt import SimpleCrypt

'''
ECB Class
'''
class ECB:
    @staticmethod
    def execute(plain, key):
        result = []
        for byte_64 in plain:
            result.append(SimpleCrypt.execute(key, byte_64))
        
        return result