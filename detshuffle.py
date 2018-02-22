# Shuffle a deck of cards in a deterministic way and measure entropy of such a shuffling.
# Alexander Ivashkin, 2018
import gzip

# Create a non-shuffled deck of 52 cards
deck = [i for i in range(52)]

# Test its entropy by calling gzip on it!
print("Non-shuffled deck gzipped: " + repr(len(gzip.compress(bytes(deck)))))
