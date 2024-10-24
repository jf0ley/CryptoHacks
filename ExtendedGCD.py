#Extended Euclidean Algorithm
def ext_gcd(a,b):
    if a == 0:
        return b, 0, 1 #gcd, u, v
    g, u1, v1 = ext_gcd(b % a, a) #Recursion
    u = v1 - (b // a) * u1 #Update u
    v = u1 #Update v
    return g, u, v

#Given primes
p, q = 26513, 32321

#Find gcd and coefficiants
g, u, v = ext_gcd(p, q)

#Get lower number
flag = min(u, v)

#Output results
print("gcd(p, q) =", g)
print("u =", u)
print("v =", v)
print("Lower flag =", flag)
    