import collections
from random import choice 

Card = collections.namedtuple('Card', ['rank','suit'])

class FrenchDeck(object):
    ranks = [ x for x in range(2,11,1) ] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def  __init__(self) -> None:
        self.Card = [ Card(rank, suit) for suit in self.suits for rank in self.ranks]
        
    def __len__(self) -> int:
        return len(self.Card)
    
    def __getitem__(self, position) -> object:
        '''
        It's suscriptable, iterable 
        '''
        return self.Card[position]
    

french_Deck = FrenchDeck()
for card in french_Deck:
    print(card)
print(french_Deck[12::13])
print(len(french_Deck))
print(french_Deck[:7], end='\n')
print(Card('J', 'hearts'))
print(choice(french_Deck))