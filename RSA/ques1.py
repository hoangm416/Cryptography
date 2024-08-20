import gmpy2
from gmpy2 import mpz

def factorize_fermat(n):
    # Tính toán sqrt(N)
    A = gmpy2.isqrt(n)
    if A * A == n:
        return A, A  # Trường hợp N là một số chính phương

    A += 1
    while True:
        x2 = A * A - n
        if gmpy2.is_square(x2):
            x = gmpy2.isqrt(x2)
            p = A - x
            q = A + x
            return p, q
        A += 1

N = mpz("179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581")

p, q = factorize_fermat(N)
print(f'p = {p}')
print(f'q = {q}')
