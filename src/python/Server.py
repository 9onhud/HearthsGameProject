import socket
from random import SystemRandom
import time


class Player:
    def __init__(self, client_name, client, address):
        self.name = client_name
        self.client = client
        self.address = address

    def send(self, data):
        self.client.send(data.encode())

    def receive(self):
        return self.client.recv(1024).decode()


# def transfer_data(client):
#     while True:
#         data = client.recv(1024).decode()
#
#         if not data:
#             break
#
#         print("Receive :" + data)
#
#         data = data.upper()
#
#         client.send(data.encode())
#         print("Send :" + data)
#     client.close()
#     print("Client is disconnect")


def play_game():
    def deal_cards():
        def make_cards():
            for rank in "23456789TJQKA":
                for suit in "CDHS":
                    cards.append(rank + suit)

        # random card and send to each player 13 cards (13 Send)
        def deal():
            for i in range(13):
                for j in range(4):
                    card = SystemRandom().choice(cards)
                    print("Send : " + card + " To : " + str(j))
                    players[j].send(card)
                    cards.remove(card)
                    time.sleep(0.05)  # wait because sometime data send too fast

        cards = []
        make_cards()
        deal()

    def exchange_cards():
        pass

    deal_cards()  # 13 send
    exchange_cards()


def start_server():
    # wait 4 client(Player) connect and receive name from client
    def connect_client():
        for i in range(player_number):
            client, address = server_socket.accept()
            client_name = client.recv(1024).decode()  # wait to receive name from client

            players.append(Player(client_name, client, address))
            print("Client: " + players[i].name + " Connect")

    # send to all client that all client are connection
    def send_ready():
        for player in players:
            player.send("ready")

    port = 5098
    player_number = 4

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((socket.gethostname(), port))

    print("Server is wait for client's connect")
    server_socket.listen(player_number)  # can connect 4 client

    connect_client()  # wait to connect 4 clients (1 Receive)
    send_ready()  # send ready to client (1 Send)


if __name__ == "__main__":
    players = []
    start_server()

    game_round = 1
    while True:
        play_game()  # start game
        game_round += 1
