# Given parameters
p = 9739  # Modulus
P = (8045, 6936)  # Given point

# Calculate Q(x, y) 
x_Q = P[0]  # x-coordinate 
y_Q = (-P[1]) % p  # y-coordinate is negated modulo p

print((x_Q, y_Q))
