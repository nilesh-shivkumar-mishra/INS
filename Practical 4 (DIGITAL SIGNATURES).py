from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()
print(" RSA Key Pair Generated!\n")

message = b"Hello TYCS students, this is Digital Signature Demo!"
print("Original Message:", message.decode())
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
print("\n Message signed successfully!")
print("Digital Signature (in bytes):", signature[:50], "...")
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("\n Signature Verified! Message is authentic and untampered.")
except:
    print("\n Signature Verification Failed! Message was changed.")
