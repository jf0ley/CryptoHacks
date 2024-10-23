# Import long_to_bytes from the Crypto.Util.number module
from Crypto.Util.number import long_to_bytes

# The large integer number that we want to convert to bytes
number = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convert the large integer to bytes
print(long_to_bytes(number))
