import random
import math
def is_prime(num):
    if num < 2: return False
    for i in range(2, int (math.sqrt(num)) + 1):
        if num % i == 0: return False
    return True
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1
        if is_prime(num): return num
def gcd (a, b):
    while b: a, b = b, a % b
    return a
def mod_inverse(e, phi):

    g, x, y = extended_gcd(e, phi)
    if g != 1: raise Exception("Mod inverse does not exist")
    return x % phi
def extended_gcd(a, b):
    if a == 0: return b, 0, 1
    g, x, y = extended_gcd(b % a, a)
    return g, y - (b // a) * x, x

def generate_key_pair_fixed():
    # Your provided fixed values
    p = 5
    q = 7
    n = 35
    e = 5
    d = 5
    return (e, n), (d, n)
def encrypt(message_int, public_key):
    e, n = public_key
    return pow (message_int, e, n)
def decrypt(ciphertext_int, private_key):
    d, n = private_key
    return pow (ciphertext_int, d, n)
if __name__ == "__main__":

    public_key, private_key = generate_key_pair_fixed()

    original_message = 3
    _, n_val = public_key
    print (f"--- Using Fixed RSA Parameters ---")
    print (f"Public Key (e, n) : {public_key}")
    print (f"Private Key (d, n): {private_key}")
    print (f"Original Message: {original_message}")
    if original_message >= n_val:
        print(f"Error: Message {original_message} is too large for n={n_val}.Please ensure M < n.")
    else:
        encrypted_message = encrypt (original_message, public_key)
        print (f"Encrypted Message: {encrypted_message}")

        decrypted_message = decrypt (encrypted_message, private_key)
        print (f"Decrypted Message: {decrypted_message}")
        assert original_message == decrypted_message
        print("\nRSA demonstration successful with fixed values!")
