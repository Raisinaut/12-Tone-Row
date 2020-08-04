# This program randomly generates a twelve tone row by
# creating a list, shuffling, and then printing it out neatly


import random


toneRow = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

random.shuffle(toneRow)

for i in range (len(toneRow)):
    print('  ' * i + toneRow[0+i])
