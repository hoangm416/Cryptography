import gmpy2

# Given large number N
N = gmpy2.mpz('72006226374735042527956443552558373833808445147399984182665305798191'
              '63556901883377904234086641876639384851752649940178970835240791356868'
              '77441155132015188279331812309091996246361896836573643119174094961348'
              '52463970788523879939683923036467667022162701835329944324119217381272'
              '9276147530748597302192751375739387929')

# Multiply N by 24
twentyFourN = 24 * N

# A is an approximation of sqrt(24 * N), taking the ceiling value
A = gmpy2.isqrt(twentyFourN) + 1

# Ensure A^2 is greater than 24N
A_squared = A**2

# x has the square root of A^2 - 24N
x_squared = A_squared - twentyFourN
x = gmpy2.isqrt(x_squared)

# Calculate p and q
p = (A - x) // 6
q = (A + x) // 4

print(f'p = {p}')
print(f'q = {q}')
