import gmpy2
from gmpy2 import mpz

def factorize(n):
    # isqrt returns the integer square root of n
    a = gmpy2.isqrt(n)

    # if n is a perfect square the factors will be ( sqrt(n), sqrt(n) )
    if a * a == n:
        return a, a

    # Duyệt từ sqrt(N) trở đi cho đến khi tìm được thừa số nguyên tố
    while True:
        a = a + 1
        bsq = a * a - n
        b = gmpy2.isqrt(bsq)
        if b * b == bsq:
            break

    return a + b, a - b

N = mpz("648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877")
p, q = factorize(N)
print(f'p = {p}')
print(f'q = {q}')
