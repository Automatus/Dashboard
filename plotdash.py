#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
setup a server to be able to use the dashboard from another pc in the network.
create a folder called img
@author: automatus
"""

import time
import matplotlib.pyplot as plt
import shutil
import os


def dashplot(values, i):
    """
    Generate a chart for a given array and output the chart
    to the img folder of a server. Also generates the HTML code,
    The HTML page will autorefresh and show a new chart each time.
    """


    # Generate and save chart
    fig, ax = plt.subplots()
    fig.patch.set_alpha(0)
    ax.patch.set_alpha(0)
    # src https://www.science-emergence.com/Articles/How-to-change-the-color-background-of-a-matplotlib-figure-/
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(axis='x', colors='yellow')
    ax.tick_params(axis='y', colors='yellow')
    # src https://stackoverflow.com/questions/1982770/matplotlib-changing-the-color-of-an-axis#12059429
    ax.set_title("Error for each try", color="yellow")
    ax.plot(list(range(len(values))), values)
    # src list range: https://stackoverflow.com/questions/11480042/python-3-turn-range-to-a-list
    plt.savefig("img/chart" + str(i))

    # Generate and save HTML
    texta = '<!DOCTYPE html> <html><head><meta charset="UTF-8"><title>Automatus Dashboard</title><style></style></head><body><header><h1>Automatus Dashboard</h1><img src="img/chart'
    textc = '.png" alt="Chart"></header></body> </html>'

    file = open("index.html", "w")
    file.write(texta + str(i) + textc)
    file.close()


shutil.rmtree("img")
os.makedirs("img")
values = [0.5, 0]
dashplot(values, 1)
