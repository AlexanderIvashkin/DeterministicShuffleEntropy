# Shuffle a deck of cards in a deterministic way and measure entropy of such a shuffling.
# Alexander Ivashkin, 2018
import gzip

# Test entropy by gzipping
def test_entropy(infoText, data):
    print(infoText + repr(len(gzip.compress(bytes(data)))))

# Create a non-shuffled deck of 52 cards
deck = [i for i in range(52)]

# Test its entropy by calling gzip on it!
test_entropy("Non-shuffled deck gzipped: ", deck)

# Put cards into five piles

