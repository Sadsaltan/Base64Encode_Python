base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
encoded = ''
filename = input("Дайте будь-ласка назву файлу (без txt)")
file = open(filename+".txt", "rb")
encode = file.read()
file.close()
for i in range(0, len(encode), 3):
    char1 = encode[i]
    base_dig1 = (char1 >> 2)
    try:
        char2 = encode[i + 1]
        base_dig2 = ((char1 & 0b00000011) << 4) | (char2 >> 4)
    except:
        base_dig3 = 64
        base_dig4 = 64
    else:
        try:
            char3 = encode[i + 2]
            base_dig3 = ((char2 & 0b00001111) << 2) | (char3 >> 6)
            base_dig4 = char3 & 0b00111111
        except:
            base_dig4 = 64
    encoded += base64[base_dig1] + base64[base_dig2] + base64[base_dig3] + base64[base_dig4]
file = open(filename+"_out.txt", "w+")
file.write(encoded)
file.close()
