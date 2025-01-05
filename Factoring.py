from sympy import factorint

# The given 150-bit number
n = 510143758735509025530880200653196460532653147

# Factorize the number
factors = factorint(n)

# Extract the smaller prime factor
smaller_prime = min(factors.keys())

# Print the smaller prime
print("Smaller Prime:", smaller_prime)
