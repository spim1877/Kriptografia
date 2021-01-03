import unittest
import utils
from merkle_hellman_knapsack import (create_superincreasing_set,
                                     generate_knapsack_key_pair,
                                     encrypt_mh, decrypt_mh)
from solitaire import (get_deck, encrypt_solitaire, decrypt_solitaire)

class TestMerkleHellmann(unittest.TestCase):
    def test_superincreasing(self):
        supinc = create_superincreasing_set()
        self.assertTrue(utils.is_superincreasing(supinc[0]))

    def test1(self):
        key = generate_knapsack_key_pair()
        msg = 'Szep napunk van'
        enc = encrypt_mh(msg, key[1])
        dec = decrypt_mh(enc, key[0])

        self.assertEqual(msg, dec)

    def test2(self):
        key = generate_knapsack_key_pair()
        msg = 'Nagy BeTu HaszNalat Test2'
        enc = encrypt_mh(msg, key[1])
        dec = decrypt_mh(enc, key[0])

        self.assertEqual(msg, dec)

    def test3(self):
        key = generate_knapsack_key_pair()
        msg = '123456789'
        enc = encrypt_mh(msg, key[1])
        dec = decrypt_mh(enc, key[0])

        self.assertEqual(msg, dec)

class TestSolitaire(unittest.TestCase):
    def test_encdec(self):
        deck = get_deck('SECRETKEY')
        msg = 'soliTaire EncrYpt'
        enctext = encrypt_solitaire(deck, msg)
        dectext = decrypt_solitaire(deck, enctext)
        self.assertEqual(dectext, 'SOLITAIREENCRYPTXXXX')