from card import *
from random import seed
from random import randint

class Deck:

    def __init__(self):
        self.cardsInfo = {
            'Ace': 1,
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5,
            'Six': 6,
            'Seven': 7,
            'Eight': 8,
            'Nine': 9,
            'Jack': 10,
            'Queen': 11,
            'King': 12
        }
        self.cards = [];
        self.initDeck();
        self.shuffle();

    def initDeck(self):
        cardKeys = self.cardsInfo.keys();
        suits = ['Spade', 'Diamond', 'Club', 'Heart'];
        index = 0;
        for suit in suits:
            for key in cardKeys:
                self.cards.append(Card(key, self.cardsInfo[key], suit));

    def shuffle(self):
        tempCards = [];
        seed(1);
        for _ in range(52):
            index = randint(0, len(self.cards) - 1);
            tempCards.append(self.cards[index]);
            self.cards.pop(index);
        self.cards = tempCards;

