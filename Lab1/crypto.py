"""Assignment 1: Cryptography for CS41 Winter 2020.

Name: <Szommer Petra Stefania>
SUNet: <spim1877>

Replace this placeholder text with a description of this module.
"""
import utils
import string

#################
# CAESAR CIPHER #
#################
def encrypt_caesar(plaintext):
    """Encrypt a plaintext using a Caesar cipher.

    Add more implementation details here.

    :param plaintext: The message to encrypt.
    :type plaintext: str

    :returns: The encrypted ciphertext.
    """
    # Your implementation here.
    for c in plaintext:
        if not(c.isupper()):                                  #Error-handling
            print("Wrong input parameters")
            return
    result = ""
    for c in plaintext:
        if (c.isalpha()):
            ind = (string.ascii_uppercase.index(c.upper()) + 3) % 26
            result += string.ascii_uppercase[ind]
        else:
            result += c
    return result

def decrypt_caesar(ciphertext):
    """Decrypt a ciphertext using a Caesar cipher.

    Add more implementation details here.

    :param ciphertext: The message to decrypt.
    :type ciphertext: str

    :returns: The decrypted plaintext.
    """
    # Your implementation here.
    result = ""
    for c in ciphertext:
        if not(c.isupper()):                                  #Error-handling
            print("Wrong input parameters")
            return

        if (c.isalpha()):
            ind = (string.ascii_uppercase.index(c.upper()) - 3) % 26
            result += string.ascii_uppercase[ind]
        else:
            result += c

    return result

###################
# VIGENERE CIPHER #
###################

def encrypt_vigenere(plaintext, keyword):
    """Encrypt plaintext using a Vigenere cipher with a keyword.

    Add more implementation details here.

    :param plaintext: The message to encrypt.
    :type plaintext: str
    :param keyword: The key of the Vigenere cipher.
    :type keyword: str

    :returns: The encrypted ciphertext.
    """

    if not (plaintext.isalpha() and keyword.isalpha()):             #Error-handling
        print("Wrong input parameter")
        return

    for c in plaintext:
        if not(c.isupper()):                                  #Error-handling
            print("Wrong input parameters")
            return

    # Your implementation here.
    enctext = ""
    i = 0
    for c in plaintext:
        if (c.isalpha):
            ind = (string.ascii_uppercase.index(c.upper()) + string.ascii_uppercase.index(keyword[i%len(keyword)].upper()))%26
            enctext += string.ascii_uppercase[ind]
            i += 1
    return enctext

def decrypt_vigenere(ciphertext, keyword):
    """Decrypt ciphertext using a Vigenere cipher with a keyword.

    Add more implementation details here.

    :param ciphertext: The message to decrypt.
    :type ciphertext: str
    :param keyword: The key of the Vigenere cipher.
    :type keyword: str

    :returns: The decrypted plaintext.
    """
    # Your implementation here.
    if not (ciphertext.isalpha() and keyword.isalpha()):   #Error handling
        print("Wrong input parameter")
        return

    for c in ciphertext:
        if not(c.isupper()):                                  #Error-handling
            print("Wrong input parameters")
            return

    for c in keyword:
        if not(c.isupper()):                                  #Error-handling
            print("Wrong input parameters")
            return

    dectext = ""
    i = 0
    for c in ciphertext:
        if (c.isalpha):
            idx = (string.ascii_uppercase.index(c.upper()) - string.ascii_uppercase.index(keyword[i%len(keyword)].upper()))%26
            dectext += string.ascii_uppercase[idx]
            i += 1
    return dectext

##################
# SCYTALE CIPHER #
##################
def encrypt_scytale(plaintext, circumference):
    for c in plaintext:
        if not(c.isupper()):                                  #Error-handling
            print("Wrong input parameters")
            return
    if (type(circumference) != int):
        print("Wrong input parameter")
        return

    enctext = ""
    n = len(plaintext)
    for i in range(circumference):
        x = slice(i, n, circumference)
        enctext+= plaintext[x]
    return enctext

def decrypt_scytale(ciphertext, circumference):
    for c in ciphertext:
        if(not c.isalpha or not c.isupper):
            print("Wrong input parameter")
            return

    if (type(circumference) != int):
        print("Wrong input parameter")
        return

    dectext = ""
    end = ""
    n = len(ciphertext)
    m = n//circumference
    r = n%circumference

    for i in range(1, r+1):
        j = i * m
        end += ciphertext[j]
        ciphertext = ciphertext[:j] + ciphertext[j+1:]

    for i in range(m):
        x = slice(i, n, m)
        dectext+= ciphertext[x]
    dectext += end
    return dectext

####################
# RAILFENCE CIPHER #
####################

def encrypt_railfence(plaintext, rails):

    if (type(rails) != int):
        print("Wrong input parameter")
        return
    for c in plaintext:
        if not(c.isupper()):                                  #Error-handling
            print("Wrong input parameters")
            return
    enctext = ""
    rail = [""] * rails
    i = 0

    dir = False
    for c in plaintext:
        rail[i] += c
        if i == rails-1:
            dir = False
        if i == 0:
            dir = True
        if (dir):
            i+=1
        else:
            i-=1

    enctext = "".join(rail)
    return enctext

def decrypt_railfence(ciphertext, num_rails):
    for c in ciphertext:
        if not(c.isupper()):                                  #Error-handling
            print("Wrong input parameters")
            return

    if (type(num_rails) != int):
        print("Wrong input parameter")
        return

    dectext = ""
    n = len(ciphertext)
    rail = [[' ' for x in range(n)]
                 for y in range(num_rails)]

    dir = False
    r = c = 0
    for i in range(n):
        if r == 0:
            dir = True
        if r == num_rails-1:
            dir = False
        rail[r][c] = 'x'

        if dir:
            r += 1
        else:
            r -= 1
        c += 1

    idx = 0
    for i in range(num_rails):
        for j in range(n):
            if (rail[i][j] != ' ' and idx < n):
                rail[i][j] = ciphertext[idx]
                idx+=1

    for j in range(n):
        for i in range(num_rails):
                if (rail[i][j] != ' '):
                    dectext +=rail[i][j]

    return dectext
