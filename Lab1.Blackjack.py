# This game is a simplified version of the blackjack
# For this project we are using python 3.5
from random import randint, random

class Card:
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.type = type

#set dealer tolerance:
tolerance = 0.1


possibleCards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
valueOfCards =  [ 1,   2,   3,   4,   5,   6,   7,   8,   9,   10,   10,  10,  10]
typesOfCards = ['clubs', 'diamonds', 'heats', 'spades']

#create deck
oDeck = []

for i in range(4):
    for j in range(13):
        oDeck.append(Card(possibleCards[j], valueOfCards[j], typesOfCards[i]))


#reorder deck:
deck = []
for i in range(len(oDeck)):
    deck.append(oDeck.pop(randint(0, len(oDeck)-1)))


#start game
myScore = 0
dealerScore = 0
dealerLoose = 0

print("Use \'g\' to get a card, \'c\' to cut")
keep = 1
cut = 0
while keep:
    option = str(input("\'g\' or \'c\'?: "))
    if option == 'g':
        #take card:
        oneCard = deck.pop(0)
        myScore = myScore + int(oneCard.value)
        print('Card: ' + str(oneCard.name) + ' ' + str(oneCard.type))
        print('Actual Score is: ' + str(myScore))

        if myScore > 21:
            keep = 0

    elif option == 'c':
        print("You CUT with Score = " + str(myScore))
        keep = 0
        cut = 1
        break


if cut == 1:
    #calculate the dealer score:
    keep = 1
    while keep:
        if(dealerScore < int(21*(1-tolerance))):
            oneCard = deck.pop(0)
            dealerScore = dealerScore + int(oneCard.value)
        else:
            keep = 0

    #Set the dealer loose if more than 21
    if dealerScore > 21:
        dealerLoose = 1

    print("dealer Score is: " + str(dealerScore))
    if (myScore > dealerScore) or (dealerLoose):
        print("You win! congrats! :)")
    else:
        print("You loose! dealer wins")

else:
    print("You loose!")



