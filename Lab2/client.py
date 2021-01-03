import socket
from sys import argv
from merkle_hellman_knapsack import (generate_knapsack_key_pair, encrypt_mh, decrypt_mh)

HOST = '127.0.0.1'
SERVERPORT = 8080

def main():
    port = argv[1]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, SERVERPORT))
    except socket.error as err:
        print("Connection err:" + str(err))
        exit()
    (private_key, public_key) = generate_knapsack_key_pair()


main()