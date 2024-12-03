
import numpy as np

data1 = np.sort(np.genfromtxt("input.txt", usecols = 0, dtype = int))
data2 = np.sort(np.genfromtxt("input.txt", usecols = 1, dtype = int))

diff = np.absolute(data1 - data2)
total = np.sum(diff)

M = []
gentag = []
for i in range(len(data1)):
    G = 0
    M = data2 - data1[i]
    for j in range(len(M)):
        if M[j] == 0:
            G += 1
    gentag.append(G)
result = data1 * gentag
print(np.sum(result))


