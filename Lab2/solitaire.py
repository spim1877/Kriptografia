#Szommer Petra Stefania, 533

N = 54
ABC = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def simplify(msg):
    simpletext = ""
    for c in msg:
        c = c.upper()
        if (c.isalpha() and ABC.find(c) != -1):
            simpletext += c
    return simpletext


def get_keystream(deck):
    joker_A_pos = deck.index('A')
    joker_B_pos = deck.index('B')

    #1. Find the A joker. Move it one card down.

    if ((joker_A_pos + 1) % N == 0):
        deck =  deck[0:1] + deck[joker_A_pos:joker_A_pos+1] + deck[1:joker_A_pos] + deck[joker_A_pos+1:N]
    else:
        deck = deck[0:joker_A_pos] + deck[joker_A_pos+1:(joker_A_pos + 1) % N+1] + deck[joker_A_pos:joker_A_pos+1] + deck[(joker_A_pos + 1) % N+1:N]

    joker_A_pos = deck.index('A')
    joker_B_pos = deck.index('B')

    # print(deck)

    #2. Find the B joker. Move it two cards down.

    if ((joker_B_pos + 2) % N == 0):
        deck =  deck[0:1] + deck[joker_B_pos:joker_B_pos+1] + deck[1:joker_B_pos] + deck[joker_B_pos+1:N]
    else:
        deck = deck[0:joker_B_pos] + deck[joker_B_pos+1:(joker_B_pos + 2) % N+1] + deck[joker_B_pos:joker_B_pos+1] + deck[(joker_B_pos + 2) % N+1:N]

    joker_B_pos = deck.index('B')
    joker_A_pos = deck.index('A')

    # print(deck)

    #3. Perform a triple cut. That is, swap the cards above the first joker with the cards below the second joker.

    if (joker_A_pos < joker_B_pos):
        first = joker_A_pos
        last= joker_B_pos
    else:
        first = joker_B_pos
        last = joker_A_pos

    newdeck = deck[last+1:N] + deck[first:last+1] + deck[0:first]
    deck=newdeck
    joker_A_pos = deck.index('A')
    joker_B_pos = deck.index('B')

    # print(deck)

    #4. Perform a count cut. Cut after the card that you counted down to, leaving the bottom card on the bottom.

    count = deck[53]
    if (count == 'A' or count == 'B'):
        count = 53

    newdeck = deck[count:N - 1] + deck[0:count]
    newdeck.append(deck[N - 1])
    deck=newdeck

    # print(deck)

    #5. Find the output card.

    topcard = deck[0]
    if (topcard == 'A' or topcard == 'B'):
        topcard = 53


    if (deck[topcard] != 'A' and deck[topcard] != 'B'):
        key=(deck[topcard])
    else:
        (deck, key) = get_keystream(deck)

    return (deck, key)

def encrypt_solitaire(deck, msg):
    msg = simplify(msg)
    print(msg)
    #1. Take the ciphertext message and put it in five-character groups.

    msglen = len(msg)
    #msglen = 16

    fives = msglen//5


    if msglen//5 < msglen/5:
        fives += 1

    length=5*fives
    keystream = []

    #2. Use Solitaire to generate keystream

    for i in range(0, length):
        (deck, key) = get_keystream(deck)  #encrypt a single character
        keystream.append(key)

    enctext = ""

    #5. Add the plaintext number stream to the keystream numbers, modulo 26.
    for i in range(0, msglen):
        enctext += ABC[((keystream[i] + ABC.index(msg[i])) %26) +1]

        if ((i+1)%5 == 0):
            enctext +=' '

    for i in range(0, 5*fives - msglen):
        enctext += ABC[((keystream[msglen+i] + ABC.index('X')) %26) +1]

    return enctext

def decrypt_solitaire(deck, msg):
    #decryption is the same as encryption, except that we subtract the keystream from the ciphertext message
    msg = simplify(msg)
    msglen = len(msg)
    keystream = []
    for i in range(0, len(msg)):
        (deck, key) = get_keystream(deck)  # encrypt a single character
        keystream.append(key)
    dectext = ""
    for i in range(0, msglen):
        dectext += ABC[(ABC.index(msg[i]) - keystream[i] -2) %26 +1]

    return dectext

def get_deck(passphrase):
    # Keying the Deck: 3. Use a passphrase to order the deck. This method uses the Solitaire algorithm to create an initial deck ordering.
    # Start with the deck in a fixed order
    deck = list(range(1, 55))
    joker_A_pos = 52
    joker_B_pos = 53
    deck[joker_A_pos] = 'A'
    deck[joker_B_pos] = 'B'

    passphrase = simplify(passphrase)

    for c in passphrase:
        cut=ABC.index(c)
        joker_A_pos = deck.index('A')
        joker_B_pos = deck.index('B')

        # Solitaire algorithm:
        # 1. Find the A joker. Move it one card down.

        if ((joker_A_pos + 1) % N == 0):
            deck = deck[0:1] + deck[joker_A_pos:joker_A_pos + 1] + deck[1:joker_A_pos] + deck[joker_A_pos + 1:N]
        else:
            deck = deck[0:joker_A_pos] + deck[joker_A_pos + 1:(joker_A_pos + 1) % N + 1] + deck[
                                                                                           joker_A_pos:joker_A_pos + 1] + deck[
                                                                                                                          (
                                                                                                                                      joker_A_pos + 1) % N + 1:N]

        joker_A_pos = deck.index('A')
        joker_B_pos = deck.index('B')

        # 2. Find the B joker. Move it two cards down.

        if ((joker_B_pos + 2) % N == 0):
            deck = deck[0:1] + deck[joker_B_pos:joker_B_pos + 1] + deck[1:joker_B_pos] + deck[joker_B_pos + 1:N]
        else:
            deck = deck[0:joker_B_pos] + deck[joker_B_pos + 1:(joker_B_pos + 2) % N + 1] + deck[
                                                                                           joker_B_pos:joker_B_pos + 1] + deck[
                                                                                                                          (
                                                                                                                                      joker_B_pos + 2) % N + 1:N]

        joker_B_pos = deck.index('B')
        joker_A_pos = deck.index('A')

        # 3. Perform a triple cut. That is, swap the cards above the first joker with the cards below the second joker.

        if (joker_A_pos < joker_B_pos):
            first = joker_A_pos
            last = joker_B_pos
        else:
            first = joker_B_pos
            last = joker_A_pos

        newdeck = deck[last + 1:N] + deck[first:last + 1] + deck[0:first]
        deck = newdeck
        joker_A_pos = deck.index('A')
        joker_B_pos = deck.index('B')

        # 4. Perform a count cut. Cut after the card that you counted down to, leaving the bottom card on the bottom.

        count = cut
        if (count == 'A' or count == 'B'):
            count = 53

        newdeck = deck[count:N - 1] + deck[0:count]
        newdeck.append(deck[N - 1])
        deck = newdeck
    return deck



