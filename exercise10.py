def encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)

        elif(char.islower()):
            result += chr((ord(char) - s - 97) % 26 + 97)

        elif i == chr(32):
            result += i

    return result

text = input("Input sentence: ")
s = int(input("Input Shift: "))
print("Text  : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text, s))


