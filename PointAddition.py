# Elliptic curve parameters and modulus
a = 497  # Coefficient 'a' in the curve equation
b = 1768  # Coefficient 'b' in the curve equation
p = 9739  # Modulus

# Function to compute modular inverse
def mod_inverse(n, p):
    """ Compute the modular inverse of n modulo p """
    return pow(n, -1, p)

# Function to add two points on the elliptic curve
def add_points(P, Q):
    """ Add two points P and Q on the elliptic curve """
    if P == "O":
        return Q  # Point at infinity
    if Q == "O":
        return P  # Point at infinity

    x1, y1 = P
    x2, y2 = Q

    # Handle the case where P + (-P) = O
    if x1 == x2 and (y1 + y2) % p == 0:
        return "O"

    # Calculate lambda (slope)
    if P != Q:
        lamb = (y2 - y1) * mod_inverse(x2 - x1, p) % p
    else:  # P == Q (tangent line case)
        lamb = (3 * x1**2 + a) * mod_inverse(2 * y1, p) % p

    # Calculate the resulting point
    x3 = (lamb**2 - x1 - x2) % p
    y3 = (lamb * (x1 - x3) - y1) % p

    return (x3, y3)

# Given points
P = (493, 5564)
Q = (1539, 4742)
R = (4403, 5202)

# Compute S = P + P + Q + R
S = add_points(add_points(add_points(P, P), Q), R)

# Print the result
print(S)
