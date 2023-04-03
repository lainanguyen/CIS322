# Name: Laina Nguyen
# Ch 6 Book exercises, R-6.1, R6.7

"""
Exercise R-6.1
# Push and pop - LIFO
Time complexity: O(1)

initial: []
push(5) - [5]
push(3) - [5, 3]
pop() - [5]
push(2) - [5, 2]
push(8) - [5, 2, 8]
pop() - [5, 2]
pop() - [5]
push(9) - [5, 9]
push(1) - [5, 9, 1]
pop() - [5, 9]
push(7) - [5, 9, 7]
push(6) - [5, 9, 7, 6]
pop() - [5, 9, 7]
pop() - [5, 9]
push(4) - [5, 9, 4]
pop() - [5, 9]
pop() - [5]

Exercise R-6.7
# Enqueue and Dequeue - FIFO
Time complexity: O(1)

initial - []
enqueue(5) - [5]
enqueue(3) - [5, 3]
dequeue() - [3]
enqueue(2) - [3, 2]
enqueue(8) - [3, 2, 8]
dequeue() - [2, 8]
dequeue() - [8]
enqueue(9) - [8, 9]
enqueue(1) - [8, 9, 1]
dequeue() - [9, 1]
enqueue(7) - [9, 1, 7]
enqueue(6) - [9, 1, 7, 6]
dequeue() - [1, 7, 6]
dequeue() - [7, 6]
enqueue(4) - [7, 6, 4]
dequeue() - [6, 4]
dequeue() - [4]
"""

# Codingame Challenge: War

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# Time complexity: O(1)
n = int(input())  # the number of cards for player 1
deck1 = []  # initiate empty array for first deck

# loop through the card rank and add to the deck1 array
# Time complexity: O(n)
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    rank = cardp_1[:-1]  # remove the suit
    deck1.append(rank)  # add that suit to deck1 array

# Time complexity: O(1)
m = int(input())  # the number of cards for player 2
deck2 = []  # initiate empty array for second deck

# loop through the card rank and add to the deck1 array
# Time complexity: O(m)
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    rank = cardp_2[:-1]  # remove the suit
    deck2.append(rank)  # add that suit to deck2 array


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# convert card rank to its integer value and return index of rank in array
# Time complexity: O(1)
def parse(rank):
    return ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"].index(rank)


# keep track of round number, start with 1
# Time complexity: O(1)
round_num = 1

# initiate empty arrays for pots to store cards
# Time complexity: O(1)
pot1 = []
pot2 = []

# game rules: the player with the higher card takes both the cards played and moves them to the bottom of their stack
# true - no winner
# false - there is a winner/s
# Time complexity: O(n)
while True:
    # draw last card from each deck and assign it to the variable
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)
    # the cards are not equal so one is higher/lower than the other
    if card1 != card2:
        pot1.append(card1)
        pot2.append(card2)
        # higher takes both cards, add to their deck
        if parse(card1) > parse(card2):
            deck1.extend(pot1 + pot2)
        else:
            deck2.extend(pot1 + pot2)
        # clear the pot for next round
        pot1 = []
        pot2 = []
        # loop through deck to see if any decks are empty
        # if it is empty then they win
        if not deck2:  # player 1 wins
            print(f"1 {round_num}")
            break
        elif not deck1:  # player 2 wins
            print(f"2 {round_num}")
            break
        # if no winners yet then move on to next round
        round_num += 1
    # game rule: if fewer than three cards left, the game ends in a tie
    elif len(deck1) < 3 or len(deck2) < 3:
        print("PAT")
        break
    # both players put down 3 cards
    else:
        pot1.append(card1)
        pot2.append(card2)
        for i in range(3):
            pot1.append(deck1.pop(0))
            pot2.append(deck2.pop(0))

# O(1) + O(n) + O(1) + O(m) + O(1) + O(1) + O(1) + O(n) = O(n+m)
# Overall Time Complexity: O(n+m)
