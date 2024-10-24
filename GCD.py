#GCD using Euclid's Algorithm
def gcd(a, b):
    while b !=0:
        a, b = b, a % b #Update a, b
    return a

#Tests
g1 = gcd(12,8)
g2 = gcd(66528, 52920)

print("gcd(12,8) =", g1)
print("gcd(66528, 52920) =", g2)