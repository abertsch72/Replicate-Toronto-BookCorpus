import os
from itertools import combinations
import collections

dir = "data/"

folders = {}

total = []
for directory in os.walk(dir):
   folders[directory[0]] = directory[2]

folders.pop(dir)
print(folders.keys())
for directory in folders:
   total.extend(folders[directory])

print(len(total))


print(len(set(total)))

frequency = collections.Counter(total)
counts = dict(frequency)
keylist = list(counts.keys())
most_freq = {}
for key in keylist:
    if counts[key] < 2:
       counts.pop(key)
    else:
       most_freq[counts[key]] = most_freq.get(counts[key], 0) + 1
print(most_freq)

for combo in combinations(folders.keys(), 2):
    count1 = len(set(folders[combo[0]]))
    count2 = len(set(folders[combo[1]]))
    overlap = count1 + count2 - len(set(folders[combo[0]] + folders[combo[1]]))
    if overlap > 50:
        print(f"{combo}: {overlap} where first set has {count1} and second set has {count2}")
