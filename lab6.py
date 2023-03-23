def encoder(integer):
    result = ""
    encode_list = []
    encode_list[:0] = integer
    encode_list = [int(j) + 3 for j in encode_list]
    for j in encode_list:
        result += str(j)
    print(result)
    pass
def decoder(Input):
    pass
def main():
    while True:
        option = input(f'Menu\n'
            f'-------------\n'
            f'1. Encode\n'
            f'2. Decode\n'
            f'3. Quit\n'
            f'Please enter an option: ')
        if option == "1":
            encode = input(f'Please enter your password to encode: ')
            encoder(encode)
        if option == "3":
            break
if __name__ == '__main__':
    main()
