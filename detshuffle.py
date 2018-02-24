# Shuffle a deck of cards in a deterministic way and measure entropy of such shuffling.
# Alexander Ivashkin, 2018

import zlib
import random
import secrets

# Create a non-shuffled deck of deck_size cards
deck_size = 65536
deck = [i for i in range(deck_size)]

def word_to_byte(data):
    """Generator function to convert words (i.e. integers 0-65535) into two
    integers representing bytes"""
    for wr in data:
        yield wr // 256
        yield wr % 256


def get_entropy(data):
    """Calculate entropy of data by zlib'bing it"""
    cmpr = zlib.compressobj(level = 9, wbits = -15, memLevel = 9)
    # bdata = ''.join(chr(data[i]) for i in range(len(data))).encode()
    return len(cmpr.compress(bytes(list(word_to_byte(data)))) + cmpr.flush())


ordered_deck_entropy = get_entropy(deck)

# To ensure same results on each run
random.seed(666)
random_deck_entropy = get_entropy([secrets.randbelow(deck_size) for i in range(deck_size)])

def test_entropy(infoText, data):
    """Test data entropy by compressing it with zlib"""
    entropy = get_entropy(data)
    print("{} of {} cards: entropy measure {}, {:.1f}% ordered / {:.1f}% random".format(
        deck_size, infoText, entropy, entropy / ordered_deck_entropy * 100, entropy / random_deck_entropy * 100))


# All zeroes and random numbers (for reference)
test_entropy("'0'", [0 for i in range(deck_size)])
# test_entropy(str(deck_size) + " random bytes: ", )
test_entropy("non-shuffled", deck)
test_entropy("random.random()", [random.randrange(0, deck_size) for i in range(deck_size)])

# Put cards into five piles
# NB: this is not the most efficient code, but I'm writing it to learn different features of Python
deck5pi = [[], [], [], [], []]
for card in range(len(deck)):
    deck5pi[card % 5].append(deck[card])

test_entropy("'into five piles'", [deck5pi[p][c] for p in range(5) for c in range(len(deck5pi[p]))])

# Ten piles
deck10pi = [[], [], [], [], [], [], [], [], [], []]
for card in range(len(deck)):
    deck10pi[card % 10].append(deck[card])

test_entropy("'into ten piles'", [deck10pi[p][c] for p in range(10) for c in range(len(deck10pi[p]))])
