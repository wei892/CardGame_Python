# global variable
# suit list
suit = ["Heart", "Clover", "Diamond", "Spade"]
# rank list
rank = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

# value dictionary of 2 - ace
value_list = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}

# create a card class
class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = value_list[rank]

    def __str__(self):
        return f'{self.rank} Of {self.suit}'
    
a = Card(suit[0], rank[0])
print(a)
print(a.rank)
print(a.value)
print(a.suit)
