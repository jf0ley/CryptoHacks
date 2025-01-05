# Elliptic curve parameters
a = 497
b = 1768
p = 9739

# Modular inverse function
def mod_inverse(n, p):
    return pow(n, -1, p)

# Add two points on the curve
def add_points(P, Q):
    if P == "O": return Q
    if Q == "O": return P
    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return "O"

    if P != Q:
        lamb = (y2 - y1) * mod_inverse(x2 - x1, p) % p
    else:
        lamb = (3 * x1**2 + a) * mod_inverse(2 * y1, p) % p

    x3 = (lamb**2 - x1 - x2) % p
    y3 = (lamb * (x1 - x3) - y1) % p
    return (x3, y3)

# Scalar multiplication using double and add
def scalar_multiply(P, n):
    R = "O"
    Q = P
    while n > 0:
        if n % 2 == 1:
            R = add_points(R, Q)
        Q = add_points(Q, Q)
        n //= 2
    return R

# Given point and scalar
P = (2339, 2213)
n = 7863

# Compute the result
Q = scalar_multiply(P, n)

# Verify the result is on the curve
x, y = Q
assert (y**2 - (x**3 + a * x + b)) % p == 0

# Print the result
print(Q)
