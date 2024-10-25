#Find the inverse using Fermat's Little Theorem
def mod_inverse(g, p):
    return pow(g, p - 2, p) #FLT for mod inverse when p is prime

#Inverse of 3%13
d = mod_inverse(3, 13)

#Output result
print("3 pow(-1) % 13 =", d)


