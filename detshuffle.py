# Shuffle a deck of cards in a deterministic way and visualize entropy of such shuffling.
# Alexander Ivashkin, 2018

import random
import secrets
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot

plots = []
def entropy(data, title):
    """Add a new circle plot into the list of Bokeh plots to visualise entropy"""
    plot = figure(title = title)
    plot.circle([i for i in range(len(data))], data)
    plots.append(plot)

def perfect_riffle_shuffle(deck, times = 1):
    """Run perfect (deterministic) riffle shuffle on the deck one or more times"""
    # TODO for sfl in range(times):
    # TODO return [deck[(c % 2) * 5 + c // 2] for c in range(len(deck))]

def shuffle_into_piles(deck, piles):
    """Shuffle cards into piles (non-randomly)"""
    deck_copy = deck[:]
    deck_piles = [deck_copy[i::piles] for i in range(piles)]
    return [deck_piles[p][c] for p in range(piles)
            for c in range(len(deck_piles[p]))]

# Create a non-shuffled deck of deck_size cards
deck_size = 52
deck = [i for i in range(1, deck_size + 1)]

entropy(deck, "Ordered deck")

# To ensure same results on each run
random.seed(666)
randdeck = deck[:]
random.shuffle(randdeck)
entropy(randdeck, "random.shuffle()")

entropy([1] * deck_size, "All 1's")

# randdeck = deck[:]
# random.shuffle(randdeck, lambda: secrets.randbelow(1))
# entropy(randdeck, "random.shuffle(secrets.randbelow)")

# Put cards into five piles
entropy(shuffle_into_piles(deck, 5), "'into five piles'")

# Seven piles
entropy(shuffle_into_piles(deck, 7), "'into seven piles'")

# Ten piles
entropy(shuffle_into_piles(deck, 10), "'into ten piles'")

# Perfect riffle shuffle
# entropy(perfect_riffle_shuffle(deck), "Perfect riffle shuffle (non-random)")


# Show the combined plot!
output_file("entropy.html", mode="inline")
combined = gridplot(plots, ncols = 2)
show(combined)
