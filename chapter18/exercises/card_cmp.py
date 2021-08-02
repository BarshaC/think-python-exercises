class Card(object): 
    '''Represents a stack of cards
       Suit: Club,Diamond... Rank: Ace,2,3,4...'''
    def __init__(self, suit = 0, rank =0):
        self.suit = suit 
        self.rank = rank 
   
    suit_names = ['Clubs','Diamonds','Hearts','Spades'] 
    rank_names = [None,'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

    def __str__(self): 
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __cmp__(self,other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
       
        if self.rank < other.rank: return 1
        if self.rank < other.rank: return -1
    
        #Returns 0 if the ranks are same 
        return 0 
    def __cmp__(self,other): 
        t1 = self.suit, self.rank 
        t2 = other.suit, other.rank 
        return cmp(t1,t2)

card1 = Card(1,1)
# print card1
import random
class Deck(object):
   # Deck contains lists of cards

    def __init__(self):
        self.cards = []
        for suit in range(4): 
            for rank in range(1,14): 
                card = Card(suit,rank)
                self.cards.append(card)

    def __str__(self): 
        res = []
        for card in self.cards: 
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self): 
        return self.cards.pop()

    def add_card(self,card): 
        self.cards.append(card) 

    def shuffle(self): 
        random.shuffle(self.cards)

    def sort(self): 
        return self.cards.sort()

    def move_cards(self,hand,num): 
        for i in range(num): 
            hand.add_cards(self.pop_card())

deck = Deck()
#print deck 

class Hand(Deck): 
    '''Represents a hand playing cards'''
'''
    def __init__(self,label=''):
        self.cards = []
        self.label = label'''
hand = Hand('new hand')
deck = Deck() 
card = deck.pop_card() 
hand.add_card(card)
print hand

