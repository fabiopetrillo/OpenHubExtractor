#!/usr/bin/python

import numpy as np
import sys
import matplotlib.pyplot as plt
from numpy.random import rand
from numpy import arange

plt.rcdefaults()

# Line command CSV file argument
pairDataFile = sys.argv[1]

data = np.genfromtxt(pairDataFile, delimiter=',',
                     dtype=None,max_rows=10, names=True)

print data['Pair']
print data['Occurrences']

y_pos = np.arange(len(data['Occurrences']))

fig = plt.figure()
ax = plt.subplot(111)
ax.barh(y_pos,data['Occurrences'], color='gray', label = "Ocurrences")

ax.set_yticks(y_pos)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_yticklabels(data['Pair'])
ax.set_xlabel('Occurrences')

ax.plot()
plt.show()

