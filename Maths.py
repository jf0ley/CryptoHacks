from sympy import mod_inverse
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

#Step 1: Calculate N
n = p * q

#Step 2: Calculate Euler's Totient function, phi(N)
phi_N = (p - 1) * (q - 1)

#Step 3: Calculate for the private key d as the modular inverse of mod phi(N)
d = mod_inverse(e, phi_N)
print(d)




# Given primes
p = 857504083339712752489993810777
q = 1029224947942998075080348647219

# Calculating Euler's totient φ(N)
phi = (p - 1) * (q - 1)
print(phi)
