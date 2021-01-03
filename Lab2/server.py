import socket
import threading

HOST = '127.0.0.1' #localhost?
PORT = 8080

ENCODING = 'utf-8'

client_dict = {}

def register_public_key(id, public_key):
    if id.isdigit(): 
        print("REGISTERING NEW CLIENT WITH ID", id)
        client_dict[id] = public_key
        print(client_dict[id])
        return True
    return False

def get_public_key(id):
    try:
        key = client_dict[id]
    except KeyError: 
        key = 0
    print(key)
    return key

def client_handler(conn, addr):
    print("Kliens ", addr[1], " kapcsolodva")
    data = conn.recv(1024)
    msg = str(data, ENCODING)
    print ("Kapott uzenet:", msg )
    msglist = msg.split(' ')
    if len(msglist) > 1:
        ok = register_public_key(msglist[0], msglist[1:len(msglist)])
        if (ok):
            conn.send(b'PUBLIC KEY SUCCESFULLY REGISTERED/UPDATED')
        else:
            conn.send(b'REGISTRATION/UPDATE UNSUCCESSFUL')
    else:
        public_key = get_public_key(msglist[0])
        if(not public_key == 0):
            conn.send(bytes(' '.join(map(str, public_key)), ENCODING))
        else:
            conn.send(bytes(public_key)) 

    print("Kapcsolat", addr[1], " klienssel vege\n")
    conn.close()


def main():
    print("Szerver elindul")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST, PORT))
    server.listen(5)
    print("Szerver portja", PORT, "...")

    while True:
        conn, addr = server.accept()
        cln = threading.Thread(target=client_handler, args=(conn, addr))
        cln.start() 
    server.close()
    print("Szerver leall")

main()