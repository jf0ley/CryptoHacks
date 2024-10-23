#Given hex string
hex_str = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

#Convert hex string to bytes
encrypted_bytes = bytes.fromhex(hex_str)

#Loop through possible byte keys
for key in range(256):
    #XOR each byte in the encrypted data with the key
    decrypted_msg = "".join(chr(b ^ key) for b in encrypted_bytes)

    #Check if the decrypted message is readable
    if "crypto" in decrypted_msg:
        print(f"Key: {key}")
        print(f"Flag: {decrypted_msg}")
        break
    