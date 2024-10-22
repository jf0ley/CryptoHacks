from base64 import b64encode

# Hexadecimal string to be converted 
code = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Convert the hex string to bytes
bytesString = bytes.fromhex(code)

# Encode the bytes into Base64 format
b64code = b64encode(bytesString)

# Print the Base64 encoded result
print(b64code)