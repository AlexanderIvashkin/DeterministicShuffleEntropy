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

def perfect_riffle_shuffle(deck):
    """Run one perfect (deterministic) riffle shuffle on the deck"""
    return [deck[(c % 2) * 5 + c // 2] for c in range(len(deck))]


# Create a non-shuffled deck of deck_size cards
deck_size = 52
deck = [i for i in range(1, deck_size + 1)]

entropy(deck, "Ordered deck")

# To ensure same results on each run
random.seed(666)
entropy([random.randrange(0, deck_size)
    for i in range(deck_size)], "random.random()")

entropy([1] * deck_size, "All 1's")
entropy([secrets.randbelow(deck_size)
    for i in range(deck_size)], "secrets.randbelow()")

# Put cards into five piles
# NB: this is not the most efficient code, but I'm writing it to learn different features of Python
deck5pi = [[], [], [], [], []]
for card in range(len(deck)):
    deck5pi[card % 5].append(deck[card])

entropy([deck5pi[p][c] for p in range(5)
    for c in range(len(deck5pi[p]))], "'into five piles'")

# Ten piles
deck10pi = [[], [], [], [], [], [], [], [], [], []]
for card in range(len(deck)):
    deck10pi[card % 10].append(deck[card])

entropy([deck10pi[p][c] for p in range(10)
    for c in range(len(deck10pi[p]))], "'into ten piles'")

# Perfect riffle shuffle
entropy(perfect_riffle_shuffle(deck), "Perfect riffle shuffle (non-random)")


# Show the combined plot!
output_file("entropy.html", mode="inline")
combined = gridplot(plots, ncols = 2)
show(combined)
