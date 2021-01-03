#Szommer Petra Stefania, 533
import utils
import random

SIZE = 8

def create_superincreasing_set():
    r = random.randint(2, 10)
    w = [r]
    total = r
    for _ in range(0, SIZE-1):
        wi = random.randint(total+1, 2*total)
        w.append(wi)
        total += wi

    q = random.randint(total+1, 2*total)

    return w, q

def find_coprime(q):
    r = random.randint(2, q-1)
    while not utils.coprime(q, r):
        r = random.randint(2, q-1)
    return r

def generate_private_key():
    (w, q) = create_superincreasing_set()
    r = find_coprime(q)
    return (w, q, r)

def create_public_key(w, q, r):
    b = []
    for i in range(0, len(w)):
        b.append(r*w[i] % q)
    return b


def encrypt_mh(msg, b):
    encdata = []
    for c in msg[0:len(msg)]:
        alpha = utils.byte_to_bits(ord(c))
        s = 0
        for i in range(0, len(alpha)):
            s += alpha[i] * b[i]
        encdata.append(s)
    return encdata


def calculate_modinv(q, r):
    return utils.modinv(r, q)


def solve_subset_sum(c, w):
    alpha = [0] * SIZE
    for i in range(SIZE - 1, -1, -1):
        if w[i] <= c:
            alpha[i] = 1
            c -= w[i]
    return alpha


def decrypt_mh(msg, private_key):
    decdata = ""
    r = private_key[-1]
    q = private_key[-2]
    w = private_key[0:-2]

    s = calculate_modinv(q, r)

    for c in msg[0:len(msg)]:
        cc = c * s % q
        alpha = solve_subset_sum(cc, w)
        i = utils.bits_to_byte(alpha)
        decdata += chr(i)

    return decdata

def merkle_hellman(msg):
    # calculating private key
    (w, q, r) = generate_private_key()

    # public key
    b = create_public_key(w, q, r)

    c = encrypt_mh(msg, b)

    msg = c
    private_key = w
    private_key.append(q)
    private_key.append(r)

    dec = decrypt_mh(msg, private_key)


def generate_knapsack_key_pair():
    (w, q, r) = generate_private_key()
    public_key = create_public_key(w, q, r)

    private_key = w
    private_key.append(q)
    private_key.append(r)

    return(private_key, public_key)

def main():
    merkle_hellman("alma")

main()