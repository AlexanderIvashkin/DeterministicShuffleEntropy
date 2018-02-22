# Shuffle a deck of cards in a deterministic way and measure entropy of such a shuffling.
# Alexander Ivashkin, 2018

import zlib
import random

# Test entropy by zlibping
def test_entropy(infoText, data):
    print(infoText + repr(len(zlib.compress(bytes(data)))))

# Create a non-shuffled deck of 52 cards
deck = [i for i in range(52)]

# Test its entropy by calling zlib on it!
test_entropy("52 zeroes: ", [0 for i in range(52)])
test_entropy("Random: ", [round(random.random() * 52) for i in range(52)])
test_entropy("Non-shuffled deck zlibped: ", deck)

# Put cards into five piles
deck5pi = [[], [], [], [], []]
for card in range(len(deck)):
    deck5pi[card % 5].append(deck[card])

test_entropy("Into five piles: ", [deck5pi[p][c] for p in range(5) for c in range(len(deck5pi[p]))])
