#!/usr/bin/python

import numpy as np
import sys
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


# Line command CSV file argument
pairDataFile = sys.argv[1]

data = np.genfromtxt(pairDataFile, delimiter=',', dtype=None,max_rows=10, names=True)

fig, ax = plt.subplots()
ax.bar(data['Occurrences'], color='r', label = "Ocurrences")

ax.set_title("Mains power stability")
ax.set_xlabel('time')
ax.set_ylabel('Mains voltage')

ax.set_xticklabels(data['Pair'])


ax.plot()

plt.show()


