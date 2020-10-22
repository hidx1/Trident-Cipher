def compare(first_file, second_file):
    with open(first_file, mode='rb') as f:
        first_file = f.read()
    with open(second_file, mode='rb') as f:
        second_file = f.read()
    
    first_file = bytearray(first_file)
    second_file = bytearray(second_file)

    byte_temp = b'\x00'

    diff = len(second_file) - len(first_file)
    for i in range(diff):
        first_file[0:0] = byte_temp

    byte_size = len(first_file)
    diff_count = 0
    for i in range(byte_size):
        if first_file[i] != second_file[i]:
            diff_count += 1
    
    print("Total difference:", diff_count)
    print("Diff percentage:", diff_count / byte_size * 100)

if __name__ == "__main__":
    compare('tests/input.txt', 'tests/output.txt')