def makeKey(curr_cipher, stt):
    return hex(int("0x" + curr_cipher[stt], 16) ^ 0x20)


def convertToHex(hex_string):
    arr = []
    for i in range(2, len(hex_string), 2):
        hex_value = hex_string[i:i+2]
        arr.append(hex_value)
    return arr


def convert():
    m = []
    for character_value in range(97, 123):
        m.append(hex(character_value ^ 0x20))

    m.append("0x00")
    return m





def enCode(cipher, k):
    cip = convertToHex(cipher)
    m = []

    for i in range(min(len(cip), len(k))): 
        if k[i] is None:
            m.append("_")
        else:
            hex_value = hex(int("0x" + cip[i], 16) ^ int(k[i], 16))
            m.append(chr(int(hex_value, 16)))
    return m



def main():
    with open("D:\\Code\\hust\\AnToanTT\\input.txt", "r") as file:
        als = file.read().splitlines()

    c = convert()
    key = [None for _ in range(200)]

    for cipher_index, current_cipher in enumerate(als):
        h = convertToHex(current_cipher)
        dis_index = {}

        for c_index, c_cipher in enumerate(als):
            if c_cipher == current_cipher:
                continue

            else:
                arr2 = convertToHex(c_cipher)
                for i in range(min(len(h), len(arr2))): 
                    hex_value = hex(int("0x" + h[i], 16) ^ int("0x" + arr2[i], 16))
                    if hex_value in c:
                        dis_index[i] = dis_index.get(i, 0) + 1
                        if dis_index[i] > 7:
                            key[i] = makeKey(h, i)

    with open("D:\\Code\\hust\\AnToanTT\\target.txt", "r") as file:
        secret_cipher = file.read()

    decrypted_message = enCode(secret_cipher, key)
    
    print(decrypted_message)
    

if __name__ == "__main__":
    main()
