import socket


def start_client():
    port = 5098

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((socket.gethostname(), port))

        # send name to server
        name = input("My name: ")
        client_socket.send(name.encode())       # (1 Send)

        status = client_socket.recv(1024).decode()      # (1 Receive)
        print(status)
        if status == "ready":
            for i in range(13):
                card = client_socket.recv(1024).decode()       # (13 Receive)
                print("Give a "+card+" card.")

    except Exception as e:
        print("You aren't connect.")
        print(e)
    finally:
        client_socket.close()
        print("Client is disconnect")


if __name__ == "__main__":
    start_client()
