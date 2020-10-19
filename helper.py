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
    
    @staticmethod
    def convertBinary64ToString(input_binary):
        result = ""
        for binary in input_binary:
            splitted_binary = [binary[i:i+8] for i in range(0, len(binary), 8)]
            for splitted_bin in splitted_binary:
                if splitted_bin != '00000000':
                    splitted_bin = '0b' + splitted_bin
                    int_splitted_bin = int(splitted_bin, 2)
                    result += chr(int_splitted_bin)
        return result


if __name__ == "__main__":
    bin_input = Helper.convertStringToBinary64(test_input)
    print(Helper.convertBinary64ToString(bin_input))