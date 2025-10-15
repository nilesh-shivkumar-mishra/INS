def one_time_pad(plaintext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ""
    for i in range(len(plaintext)):
        plaintext_index = alphabet.index(plaintext[i])
        key_index = alphabet.index(key[i])
        new_index = (plaintext_index + key_index) % 26
        ciphertext += alphabet[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ""
    for i in range(len(ciphertext)):
        cipher_index = alphabet.index(ciphertext[i])
        key_index = alphabet.index(key[i])
        new_index = (cipher_index - key_index) % 26
        plaintext += alphabet[new_index]
    return plaintext

plaintext = "HELLO"
key = "XMCKL"
ciphertext = one_time_pad(plaintext, key)
print(f"Ciphertext: {ciphertext}")
decrypted_text = decrypt(ciphertext, key)
print(f"Decrypted Text: {decrypted_text}")
