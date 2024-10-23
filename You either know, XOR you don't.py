#Encrypted message in hex
en_msg = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

#Convert hex to bytes
en_bytes = bytes.fromhex(en_msg)

#Known flag format 'crypto{', use to help discover key
known_start = b"crypto{"

#Derive key by XOR en_bytes with known flag
derived_k = [e ^ k for e, k in zip(en_bytes, known_start)] + [ord('y')]

#Decrypt message using derived key
dec_msg = []
k_length = len(derived_k)
for index, byte in enumerate(en_bytes):
    dec_msg.append(byte ^ derived_k[index % k_length])

#Convert decrypted bytes back to string
flag = "".join(chr(b) for b in dec_msg)

#Print flag
print(flag)