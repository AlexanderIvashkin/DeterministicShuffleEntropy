# Shuffle a deck of cards in a deterministic way and visualize entropy of such shuffling.
# Alexander Ivashkin, 2018

import random
import secrets
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot

def entropy_plot(data, title):
    """Visualise entropy of data with bokeh scatter plot"""
    plot = figure(title = title)
    plot.circle([i + 1 for i in range(len(data))], data)
    return plot

# Create a non-shuffled deck of deck_size cards
deck_size = 256
deck = [i for i in range(deck_size)]

plots = []

plots.append(entropy_plot(deck, "Ordered deck"))

# To ensure same results on each run
random.seed(666)
plots.append(entropy_plot([random.randrange(0, deck_size)
    for i in range(deck_size)], "random.random()"))

# All zeroes and random numbers (for reference)
plots.append(entropy_plot([0] * deck_size, "All 0's"))
# entropy_plot("non-shuffled", deck)
plots.append(entropy_plot([secrets.randbelow(deck_size)
    for i in range(deck_size)], "secrets.randbelow()"))

# Put cards into five piles
# NB: this is not the most efficient code, but I'm writing it to learn different features of Python
deck5pi = [[], [], [], [], []]
for card in range(len(deck)):
    deck5pi[card % 5].append(deck[card])

plots.append(entropy_plot([deck5pi[p][c] for p in range(5)
    for c in range(len(deck5pi[p]))], "'into five piles'"))

# Ten piles
deck10pi = [[], [], [], [], [], [], [], [], [], []]
for card in range(len(deck)):
    deck10pi[card % 10].append(deck[card])

plots.append(entropy_plot([deck10pi[p][c] for p in range(10)
    for c in range(len(deck10pi[p]))], "'into ten piles'"))


# Show the combined plot!
output_file("entropy.html")
combined = gridplot([plots])
show(combined)
