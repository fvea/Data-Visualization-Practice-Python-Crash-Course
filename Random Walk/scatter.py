""" Greeting Cards Sent and Received by Five Friends. """

import matplotlib.pyplot as plt 
import numpy as np


# Data 
card_sent = [1,5,7,13,19]
card_received = [6,10,12,14,18]
point_numbers = np.arange(len(card_sent))

plt.scatter(card_sent,card_received,c=card_received,
    cmap=plt.cm.Blues,edgecolors='none')

plt.xticks(ticks=point_numbers,labels=card_sent)

plt.show()