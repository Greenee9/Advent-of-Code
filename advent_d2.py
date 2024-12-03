import numpy as np

file = np.loadtxt("inputd2.txt", dtype = str, delimiter="\n")

X = 0
Data = []
for i in range(1000):
    intermed = []
    X = file[i].split(' ')
    for j in range(len(X)):
        intermed.append(int(X[j]))
    Data.append(intermed)
print(Data)