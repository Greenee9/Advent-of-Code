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

safe = 0
for i in range(len(Data)):
    pos = 0
    neg = 0
    if  sorted(Data[i]) != Data[i] and sorted(Data[i]) != Data[i][::-1]:
        continue
    for j in range(len(Data[i])-1):
        diff = Data[i][j] - Data[i][j+1]
        if diff in [1,2,3]:
            pos += 1
        if diff in [-1,-2,-3]:
            neg += 1
    if  len(Data[i])-1 == pos or len(Data[i])-1 == neg:
        safe += 1

print(safe)

#(pos >= 1 and neg == 0) or (pos == 0 and neg >= 1) 