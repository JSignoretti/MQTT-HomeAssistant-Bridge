import socket
import ipaddress


def getFileContent(filename)->str:
    """
    Displays the content of a given file to the console.
    """
    try:
        with open(filename, 'r') as f:
            content = f.read()
            return str(content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")




HOST = "127.0.0.1"
PORT = 65432

MAX_CONNECTION_BACKLOG = int(getFileContent("/proc/sys/net/core/somaxconn"))

def runServer(ip:str, port:int)->int:


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind((ip, port))

    if(MAX_CONNECTION_BACKLOG):
        sock.listen(MAX_CONNECTION_BACKLOG//3)
    else:
        sock.listen(1)


    conn, addr = sock.accept()

    print("Connected by", addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)

    conn.close()
    sock.close()

    return 0




def runClient(ip:str, port:int)->int:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    sock.sendall(b"Hello World!")
    data = sock.recv(1024)
    print(f"Received {data!r}")

    sock.close()

    return 0