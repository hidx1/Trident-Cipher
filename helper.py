test_input = "abcdefghijklmnopq"

class Helper:
    @staticmethod
    def convertStringToBinary64(input_string):
        byte_array = bytearray(test_input, "utf8")

        byte_list = []
        for byte in byte_array:
            bin_byte = bin(byte)[2:]
            pad_bit_count = 8 - len(bin_byte)
            for pad_bit in range(pad_bit_count):
                bin_byte = '0' + bin_byte
            byte_list.append(bin_byte)

        for pad in range(8 - (len(byte_list) % 8)):
            bin_byte = '00000000'
            byte_list.insert(0, bin_byte)

        bytes_64 = []
        for i in range(0, len(byte_list), 8):
            result_64 = ''
            for j in range(8):
                result_64 += byte_list[i+j]
            bytes_64.append(result_64)
        
        return bytes_64


if __name__ == "__main__":
    print(Helper.convertStringToBinary64(test_input))