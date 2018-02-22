# Shuffle a deck of cards in a deterministic way and measure entropy of such a shuffling.
# Alexander Ivashkin, 2018

import zlib
import random

# Test data entropy by compressing it
def test_entropy(infoText, data):
    print(infoText + repr(len(zlib.compress(bytes(data), zlib.Z_BEST_COMPRESSION))))

deck_size = 52000

# Create a non-shuffled deck of deck_size cards
deck = [i % 256 for i in range(deck_size)]

# All zeroes and random numbers (for reference)
test_entropy(str(deck_size) + " zeroes: ", [0 for i in range(deck_size)])
test_entropy(str(deck_size) + " random bytes: ", [round(random.random() * 255) for i in range(deck_size)])
test_entropy("Non-shuffled deck: ", deck)

# Put cards into five piles
deck5pi = [[], [], [], [], []]
for card in range(len(deck)):
    deck5pi[card % 5].append(deck[card])

test_entropy("Into five piles: ", [deck5pi[p][c] for p in range(5) for c in range(len(deck5pi[p]))])
