#!/usr/bin/env python3

import sys
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256

KEY_LEN = 16            
IV_LEN = 16            
SALT_LEN = 8            
HEADER = b"Salted__"    
PBKDF2_ITERATIONS = 10000  

def derive_key_and_iv(password, salt):
    key_iv = PBKDF2(password, salt, dkLen=KEY_LEN + IV_LEN,
                    count=PBKDF2_ITERATIONS,
                    hmac_hash_module=SHA256)
    return key_iv[:KEY_LEN], key_iv[KEY_LEN:]

def encrypt(password):
    salt = get_random_bytes(SALT_LEN)
    key, iv = derive_key_and_iv(password.encode(), salt)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    plaintext = sys.stdin.buffer.read()

    pad_len = 16 - (len(plaintext) % 16)
    plaintext += bytes([pad_len] * pad_len)

    ciphertext = cipher.encrypt(plaintext)

    sys.stdout.buffer.write(HEADER + salt + ciphertext)

def decrypt(password):
    data = sys.stdin.buffer.read()

    if data[:8] != HEADER:
        sys.stderr.write("Error: formato no válido. Falta encabezado 'Salted__'\n")
        sys.exit(1)

    salt = data[8:16]
    ciphertext = data[16:]
    key, iv = derive_key_and_iv(password.encode(), salt)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    plaintext_padded = cipher.decrypt(ciphertext)

    pad_len = plaintext_padded[-1]
    if not 1 <= pad_len <= 16:
        sys.stderr.write("Error: padding inválido. ¿Contraseña incorrecta?\n")
        sys.exit(1)

    plaintext = plaintext_padded[:-pad_len]
    sys.stdout.buffer.write(plaintext)

def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ['-e', '-d']:
        print("Uso correcto: ./xaes.py -e|-d 'contraseña'", file=sys.stderr)
        sys.exit(1)

    modo = sys.argv[1]
    password = sys.argv[2]

    if modo == '-e':
        encrypt(password)
    else:
        decrypt(password)
# Borrable, sirve para cuando no se quiere ejeuctar el programa desde la linea de cmandos y se quiere importar en otro script.
if __name__ == "__main__":
    main()
