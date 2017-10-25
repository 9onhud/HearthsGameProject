class Card:
    def __init__(self, card_face, card_rank, card_point, card_pic):
        self.card_face = card_face
        self.card_rank = card_rank
        self.card_point = card_point
        self.card_pic = card_pic


class Cards:
    def __init__(self):
        self.all_card = [Card("2C", 1, 0, ""), Card("2D", 1, 0, ""), Card("2H", 1, 1, ""), Card("2S", 1, 0, "")
                        , Card("3C", 2, 0, ""), Card("3D", 2, 0, ""), Card("3H", 2, 1, ""), Card("3S", 2, 0, "")
                        , Card("4C", 3, 0, ""), Card("4D", 3, 0, ""), Card("4H", 3, 1, ""), Card("4S", 3, 0, "")
                        , Card("5C", 4, 0, ""), Card("5D", 4, 0, ""), Card("5H", 4, 1, ""), Card("5S", 4, 0, "")
                        , Card("6C", 5, 0, ""), Card("6D", 5, 0, ""), Card("6H", 5, 1, ""), Card("6S", 5, 0, "")
                        , Card("7C", 6, 0, ""), Card("7D", 6, 0, ""), Card("7H", 6, 1, ""), Card("7S", 6, 0, "")
                        , Card("8C", 7, 0, ""), Card("8D", 7, 0, ""), Card("8H", 7, 1, ""), Card("8S", 7, 0, "")
                        , Card("9C", 8, 0, ""), Card("9D", 8, 0, ""), Card("9H", 8, 1, ""), Card("9S", 8, 0, "")
                        , Card("TC", 9, 0, ""), Card("TD", 9, 0, ""), Card("TH", 9, 1, ""), Card("TS", 9, 0, "")
                        , Card("JC", 10, 0, ""), Card("JD", 10, 0, ""), Card("JH", 10, 1, ""), Card("JS", 10, 0, "")
                        , Card("QC", 11, 0, ""), Card("QD", 11, 0, ""), Card("QH", 11, 1, ""), Card("QS", 11, 13, "")
                        , Card("KC", 12, 0, ""), Card("KD", 12, 0, ""), Card("KH", 12, 1, ""), Card("KS", 12, 0, "")
                        , Card("AC", 13, 0, ""), Card("AD", 13, 0, ""), Card("AH", 13, 1, ""), Card("AS", 13, 0, "")]

    def get_rank(self, card_face):
        for card in self.all_card:
            if card.card_face == card_face:
                return card.card_rank

    def get_point(self, card_face):
        for card in self.all_card:
            if card.card_face == card_face:
                return card.card_point

    def get_pic(self, card_face):
        for card in self.all_card:
            if card.card_face == card_face:
                return card.card_pic