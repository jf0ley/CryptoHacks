import hashlib

# Elliptic curve parameters
a = 497
b = 1768
p = 9739

# Modular inverse function
def mod_inverse(n, p):
    return pow(n, -1, p)

# Point addition on the elliptic curve
def add_points(P, Q):
    if P == "O": return Q  # Handle point at infinity
    if Q == "O": return P  # Handle point at infinity
    x1, y1 = P
    x2, y2 = Q

    # Handle point addition when x1 == x2 and y1 == -y2 (mod p)
    if x1 == x2 and (y1 + y2) % p == 0:
        return "O"

    # Calculate slope (lambda)
    if P != Q:
        lamb = (y2 - y1) * mod_inverse(x2 - x1, p) % p
    else:  # Tangent case (P == Q)
        lamb = (3 * x1**2 + a) * mod_inverse(2 * y1, p) % p

    # Compute resulting point
    x3 = (lamb**2 - x1 - x2) % p
    y3 = (lamb * (x1 - x3) - y1) % p
    return (x3, y3)

# Scalar multiplication using double and add algorithm
def scalar_multiply(P, n):
    R = "O"  # Initialize to point at infinity
    Q = P  # Initialize Q to P
    while n > 0:
        if n % 2 == 1:  # If the current bit is 1
            R = add_points(R, Q)
        Q = add_points(Q, Q)  # Double the point
        n //= 2  # Shift to the next bit
    return R

# Provided generator point, QA, and Bob's secret integer
G = (1804, 5368)
QA = (815, 3190)
nB = 1829

# Calculate shared secret S = [nB]QA
shared_secret = scalar_multiply(QA, nB)

# Extract the x-coordinate and hash it with SHA-1
x_coordinate = shared_secret[0]
key = hashlib.sha1(str(x_coordinate).encode()).hexdigest()

# Output the final key (flag)
print("crypto{" + key + "}")

