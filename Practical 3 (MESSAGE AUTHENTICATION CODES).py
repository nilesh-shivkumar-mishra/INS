from __future__ import annotations
import hmac
import hashlib
import secrets
import base64
from typing import Literal
HashName = Literal["sha256", "sha512", "sha1"]

def generate_secret_key(num_bytes: int = 32) -> bytes:

    return secrets.token_bytes(num_bytes)
def encode_key_b64(key: bytes) -> str:

    return base64.b64encode(key).decode("utf-8")

def hmac_hex(message: bytes | str, key: bytes, algo: HashName = "sha256") -> str:
    if isinstance(message, str):
        message = message.encode("utf-8")
    digestmod = getattr(hashlib, algo)
    return hmac.new(key, message, digestmod).hexdigest()
def verify_hmac(message: bytes | str, key: bytes, received_hex_mac: str, algo: HashName = "sha256") -> bool:
    expected = hmac_hex(message, key, algo)
    return hmac.compare_digest(expected, received_hex_mac)

if __name__ == "__main__":

    secret_key = generate_secret_key(32) 
    print("Secret key (Base64):", encode_key_b64(secret_key))

    message = "This is a confidential message."
    algorithm: HashName = "sha256"

    mac_hex = hmac_hex(message, secret_key, algorithm)
    print("\n--- Sender ---")
    print("Message:", message)
    print("Algorithm:", algorithm.upper())
    print("Generated MAC with SHA-256 (hex):", mac_hex)

    mac_sha512 = hmac_hex(message, secret_key, "sha512")
    print("\nGenrated MAC with SHA-512 (hex):", mac_sha512)

    print("\n--- Receiver ---")
    ok = verify_hmac(message, secret_key, mac_hex, algorithm)
    print("Verification (original message):", "Valid" if ok else "Invalid")

    tampered = "This is a confidential message!"
    ok_tamper = verify_hmac(tampered, secret_key, mac_hex, algorithm)
    print("Verification (tampered message):", "Valid" if ok_tamper else "Invalid")

