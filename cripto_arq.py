def msg_and_key():
    arquivo = input("Digite o nome do arquivo: ")
    file = open(arquivo, 'r')
    msg = file.read().upper().replace('\n','')
    
                                     
    key = input("Digite a chave de criptografia: ").upper()

    key_map = ""

    j=0

    for i in range(len(msg)):
        if ord(msg[i]) == 32:
            
            key_map += " "
        else:
            
            if j < len(key):
                key_map += key[j]
                j+= 1
            else:
                j = 0
                key_map += key[j]
                j += 1
    #print(key_map)
    return msg, key_map

def create_vigenere_table():
    table = []
    for i in range(26):
        table.append([])

    for row in range(26):
        for column in range(26):
            if (row + 65) + column > 90:
                table[row].append(chr((row+65) + column - 26))
            else:
                table[row].append(chr((row+65)+column))

    #for row in table:
    #    for column in row:
    #        print(column, end=" ")
    #    print(end="\n")
    return table
        

def cipher_encryption(message, mapped_key):
    table = create_vigenere_table()
    encrypted_text = ""

    for i in range(len(message)):
        if message[i] == chr(32):
            encrypted_text += " "
        else:
            row = ord(message[i])-65
            column = ord(mapped_key[i]) - 65
            encrypted_text += table[row][column]

            file = open('cripto.txt', 'w')
            file.write(encrypted_text)
            file.close()
            
    
    print("Arquivo Criptografado!")
    
    

def itr_count(mapped_key, message):
    counter = 0
    result = ""

    for i in range(26):
        if mapped_key + i > 90:
            result += chr(mapped_key+(i-26))
        else:
            result += chr(mapped_key+i)

    for i in range(len(result)):
        if result[i] == chr(message):
            break
        else:
            counter += 1

    return counter


def cipher_decryption(message, mapped_key):
    table = create_vigenere_table()
    decrypted_text = ""

    for i in range(len(message)):
        if message[i] == chr(32):
            decrypted_text += " "
        else:
            decrypted_text += chr(65 + itr_count(ord(mapped_key[i]), ord(message[i])))

            file = open('decripto.txt', 'w')
            file.write(decrypted_text)
            file.close()

    print("Arquivo Decriptografado!")
    
def main():
    print("-----CIFRA DE VIGENERE-----")
    choice = int(input("1.Criptografar\n2.Deccriptografar\nEscolha 1 ou 2: "))
    if choice == 1:
        print("---Criptografar---")
        message, mapped_key = msg_and_key()
        cipher_encryption(message, mapped_key)

    elif choice == 2:
        print("---Decriptografar---")
        message, mapped_key = msg_and_key()
        cipher_decryption(message, mapped_key)

    else:
        print("Você digitou um comando inválido!")


if __name__ == "__main__":
    main()



