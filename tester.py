import time
from blockCipher import BlockCipher

if __name__ == "__main__":
    input_name = "tests/original.png"
    output_name = "tests/encrypted.png"
    output_name_2 = "tests/decrypted.png"
    key = "asd123pl"
    is_file = "y"
    encrypt = "y"
    mode = "counter"

    encrypt_start = time.time()
    print("ENCRYPTING")
    bc = BlockCipher()
    bc.set_initial(input_name, is_file)
    bc.set_key(key)
    bc.execute(mode, encrypt)
    bc.write_result(output_name, is_file)
    encrpyt_end = time.time()
    encrypt_time = encrpyt_end - encrypt_start
    print("Elapsed encrypt time (sec):", encrypt_time, "sec")

    decrypt_start = time.time()
    print("DECRYPTING")
    bc = BlockCipher()
    encrypt = "n"
    bc.set_initial(output_name, is_file)
    bc.set_key(key)
    bc.execute(mode, encrypt)
    bc.write_result(output_name_2, is_file)
    decrypt_end = time.time()
    decrypt_time = decrypt_start - decrypt_end
    print("Elapsed decrypt time (sec):", encrypt_time, "sec")