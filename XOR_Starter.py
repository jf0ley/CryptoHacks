#Given string and int
string = "label"
int = 13

#Convert characters to Unicode vals
unicode_values = [ord(char) for char in string]

#XOR each val with 13
xor_vals = [int ^ val for val in unicode_values]

#Convert back to chars and join
xor_string_res = "".join(chr(v) for v in xor_vals)

#Format flag
flag = f"crypto{{{xor_string_res}}}"

