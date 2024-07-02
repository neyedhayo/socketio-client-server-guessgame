import socket
import random

def main():
    host = '127.0.0.1'
    port = 65432

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f'Server listening on {host}:{port}')
    
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    number = random.randint(1, 100)
    print(f"Random number: {number}")

    try:
        while True:
            guess = conn.recv(1024).decode()
            if not guess:
                break
            guess = int(guess)
            if guess < number:
                conn.sendall(b'Higher')
            elif guess > number:
                conn.sendall(b'Lower')
            else:
                conn.sendall(b'Correct!')
                break
    finally:
        conn.close()

if __name__ == "__main__":
    main()
