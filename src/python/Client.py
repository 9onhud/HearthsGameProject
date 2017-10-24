import socket


def give_cards():
    cards = []
    for i in range(13):
        card = client_socket.recv(2).decode()  # (13 Receive)
        print("Give a " + card + " card.")
        cards.append(card)
    return cards


def exchange_cards():
    cards_exchange = []
    # give 3 cards from MainGame to assign var cards_exchange

    # Just for Test
    for i in range(3):
        # cards_exchange.append(input("Card Exchange: "))
        client_socket.send(input("Card Exchange: ").encode())

    # for card_exchange in cards_exchange:  # (3 send)
    #     client_socket.send(card_exchange.encode())
    cards_from_other = []
    for i in range(3):
        cards_from_other.append(client_socket.recv(2).decode())     # parameter 2 is mean maximum string size in byte (1str = 1byte)
    print(cards_from_other)


def start_client():

    def give_status():
        return client_socket.recv(1024).decode()

    try:
        client_socket.connect((socket.gethostname(), port))

        # send name to server
        name = input("My name: ")
        client_socket.send(name.encode())  # (1 Send)

        while True:
            status = give_status()
            if status == "Ready":
                cards = give_cards()        # (13 Receive)
                # send cards to MainGame to set GameGUI
            elif status == "Exchange":
                exchange_cards()        # (3 Send)
            elif status == "Your Turn":
                forced_card = client_socket.recv(1024).decode()     # (1 Receive)




    except Exception as e:
        print("You aren't connect.")
        print(e)
    finally:
        client_socket.close()
        print("Client is disconnect")


if __name__ == "__main__":
    port = 5098
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    start_client()
