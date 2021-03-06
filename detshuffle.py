# Shuffle a deck of cards in a few different ways and visualize entropy of such shuffling.
# Alexander Ivashkin, 2018

# Version: 1.0.0-alpha

import random
import secrets
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot
from itertools import chain

plots = []
def entropy(data, title):
    """Add a new histogram plot into the list of Bokeh plots to visualise entropy"""
    plot = figure(title = title)
    plot.quad(top = data, bottom = 0, left = [i + 1 for i in range(len(data))],
            right = [i + 2 for i in range(len(data))], line_color = "black")
    plot.xaxis.axis_label = "card in deck"
    plot.yaxis.axis_label = "card number"
    plots.append(plot)


# TODO - math is wrong (duplicates a card for odd number of cards)
def perfect_riffle_shuffle(deck, times = 1):
    """Run perfect (deterministic) riffle shuffle on the deck one or more times"""
    shuffled_deck = deck[:]
    temp_deck = []

    for sfl in range(times):
        temp_deck = [shuffled_deck[i//2 + i%2 * len(shuffled_deck)//2]
                for i in range(len(shuffled_deck))]
        # I might have dropped the '== 1' but left it for clarity
        if len(deck) % 2 == 1:
            temp_deck.append(*shuffled_deck[-1:])
        shuffled_deck = temp_deck[:]
        temp_deck = []

    return shuffled_deck


def shuffle_into_piles(deck, piles):
    """Shuffle cards into piles (non-randomly)"""
    deck_copy = deck[:]
    deck_piles = [deck_copy[i::piles] for i in range(piles)]
    return list(chain.from_iterable(deck_piles))


# Create a non-shuffled deck of deck_size cards
# A consists of three copies of each card (i.e. for LOTR LCG)
deck_size = 50
deck = [i // 3 + 1 for i in range(deck_size)]

entropy(deck, "Ordered LOTR deck")

# Shuffle using random.shuffle()
random.seed(666)
randdeck = deck[:]
random.shuffle(randdeck)
entropy(randdeck, "random.shuffle()")

# Shuffle using "more robust" RNG (secrets)
randdeck = deck[:]
random.shuffle(randdeck, lambda: secrets.randbelow(10000000) / 10000000)
entropy(randdeck, "random.shuffle(secrets.randbelow)")

# Put cards into five piles
entropy(shuffle_into_piles(deck, 5), "'into five piles'")

# Seven piles
entropy(shuffle_into_piles(deck, 7), "'into seven piles'")

# Ten piles
entropy(shuffle_into_piles(deck, 10), "'into ten piles'")

# Five piles... twice!
entropy(shuffle_into_piles(shuffle_into_piles(deck, 5), 5), "'into five piles... twice'")

# Perfect riffle shuffle TODO
# entropy(perfect_riffle_shuffle(deck), "Perfect riffle shuffle (non-random)")
# entropy(perfect_riffle_shuffle(deck, 3), "Perfect riffle shuffle (three times)")

# Show the combined plot!
output_file("entropy.html", mode="inline")
combined = gridplot(plots, ncols = 2)
show(combined)
