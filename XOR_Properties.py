#Define hex strings for keys and encrypted flag
k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
k2_k1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
k2_k3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_k1_k3_k2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

#Convert hex strings to int values
k1_bytes = [byte for byte in bytes.fromhex(k1)]
k2_k3_bytes = [byte for byte in bytes.fromhex(k2_k3)]
flag_k1_k3_k2_bytes = [byte for byte in bytes.fromhex(flag_k1_k3_k2)]

#XOR flag_k1_k3_k2 with k2_k3 to eliminate k3
flag_k1_bytes = [fk1k3k2 ^ k2k3 for fk1k3k2, k2k3 in zip(flag_k1_k3_k2_bytes, k2_k3_bytes)]

#XOR the result with k1 to get original flag
flag_bytes = [fk1 ^ k1 for fk1, k1 in zip(flag_k1_bytes, k1_bytes)]

#Convert the list of bytes back to a string to reveal flag
flag = "".join(chr(byte) for byte in flag_bytes)

#Print flag
print(flag)