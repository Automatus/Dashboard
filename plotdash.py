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
    ax.spines['bottom'].set_color('grey')
    ax.spines['top'].set_color('grey')
    ax.spines['right'].set_color('grey')
    ax.spines['left'].set_color('grey')
    ax.tick_params(axis='x', colors='black')
    ax.tick_params(axis='y', colors='black')
    # src https://stackoverflow.com/questions/1982770/matplotlib-changing-the-color-of-an-axis#12059429
    ax.set_title("Error for each try", color="grey")
    ax.plot(list(range(len(values))), values)
    # src list range: https://stackoverflow.com/questions/11480042/python-3-turn-range-to-a-list
    plt.savefig("img/chart" + str(i))

    # Generate and save HTML
    texta = ('<!DOCTYPE html> <html>'
             '<head><meta charset="UTF-8"><meta http-equiv="refresh" content="5">'
             '<title>Automatus Dashboard</title>'
             '<style>body {text-align: center; background-image: url(""); background-size: cover;}</style>'
             '</head><body><header>'
             '<h1>Automatus Dashboard</h1>'
             '<img src="img/chart')
    # src autorefresh: https://stackoverflow.com/questions/8711888/auto-refresh-code-in-html-using-meta-tags
    textc = '.png" alt="Chart"></header></body> </html>'

    file = open("index.html", "w")
    file.write(texta + str(i) + textc)
    file.close()


shutil.rmtree("img/charts")
os.makedirs("img/charts")
values = [0.5, 5, 1, 5, 8, 0.5, 40, 35, 20, 0, 10, 12, 13, 15 , 16, 18, 19]
dashplot(values, 1)
