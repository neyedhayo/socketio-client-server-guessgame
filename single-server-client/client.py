import socket

def main():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        
        while True:
            guess = input("Enter your guess: ")
            client_socket.sendall(guess.encode())
            response = client_socket.recv(1024).decode()
            print("Server response:", response)
            if response == 'Correct!':
                print("Congratulations! You guessed the number.")
                break

if __name__ == "__main__":
    main()