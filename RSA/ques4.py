import gmpy2

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

def rsa_decrypt(c, d, N):
    return pow(c, d, N)

def main():
    N = gmpy2.mpz("179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581")
    e = 65537
    ciphertext = gmpy2.mpz("22096451867410381776306561134883418017410069787892831071731839143676135600120538004282329650473509424343946219751512256465839967942889460764542040581564748988013734864120452325229320176487916666402997509188729971690526083222067771600019329260870009579993724077458967773697817571267229951148662959627934791540")

    # Bước 1: Phân tích N thành p và q
    p, q = factorize(N)
    
    # Bước 2: Tính phi(N)
    phi_N = (p - 1) * (q - 1)

    # Bước 3: Tính số mũ giải mã d
    d = gmpy2.invert(e, phi_N)

    # Bước 4: Giải mã bản mã
    plaintext = rsa_decrypt(ciphertext, d, N)

    # Bước 5: Chuyển đổi plaintext thành dạng hex hợp lệ
    plaintext_hex = format(plaintext, 'x')
    
    # Bước 6: Đảm bảo chiều dài của plaintext_hex là chẵn (mỗi byte là 2 ký tự hex)
    if len(plaintext_hex) % 2 != 0:
        plaintext_hex = '0' + plaintext_hex

    # Bước 7: Chuyển đổi từ hex sang bytes
    plaintext_bytes = bytes.fromhex(plaintext_hex)
    
    # Bước 8: Tìm chỉ số của 0x00 trong plaintext_bytes
    separator_index = plaintext_bytes.index(b'\x00', 2)  # Tìm từ vị trí 2 trở đi để bỏ qua 0x02 đầu tiên
    message = plaintext_bytes[separator_index + 1:]  # Bản rõ bắt đầu sau 0x00
    
    print("Thông điệp giải mã được:", message.decode('ascii'))

if __name__ == "__main__":
    main()
