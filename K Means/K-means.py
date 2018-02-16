import math
import numpy as np
from matplotlib import pyplot as plt

def distance(a, b):    # function for finding distances
    return math.sqrt(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2))


x = np.random.randint(400, size=(100, 2)).tolist()              # generate random data of size 100

#print(x)


k = 2                   # using k = 2 ( only 2 clusters to form)

centers = np.random.randint(400, size=(k, 2)).tolist()              # generate random centers

newCenters = centers[:]                 # copy centers

previousCenter = centers[:]             # copy centers
cent1 = []
cent2 = []

while 1:                # run the loop

    dis1 = []
    dis2 = []

    del cent1[:]
    del cent2[:]

    newCenters = []


    for i in range(len(x)):                         # Loop for calculating distance of each point from each center
        dis1.append(distance(centers[0], x[i]))
        dis2.append(distance(centers[1], x[i]))

    for i in range(len(dis1)):                  #Now compare each point distance from each center and assign it to closest center

        if dis1[i] <= dis2[i]:
            cent1.append(list(x[i]))
        else:
            cent2.append(list(x[i]))

    s = 0
    q = 0

    for i in cent1:         # this part is calculate mean of alloted points of center 1
        s = s + i[0]
        q = q + i[1]

    s = s / len(cent1)
    q = q / len(cent1)

    newCenters.append([s, q])       # assign new center according to mean of alloted points

    s = 0
    q = 0

    for i in cent2:             # this part is calculate mean of alloted points of center 2
        s = s + i[0]
        q = q + i[1]

    s = s / len(cent2)
    q = q / len(cent2)

    newCenters.append([s, q])           # assign new center according to mean of alloted points



    del x[:]
    x = cent1[:] + cent2[:]

    del centers[:]
    centers = newCenters[:]

    if previousCenter == centers :          # this part we check if new center is equal to previous center
        break                       # if equal then break the loop

    del previousCenter[:]
    previousCenter = centers[:]




# this part is for plotting the points

for i in cent1:
    plt.scatter(i[0], i[1], c='y')
for i in cent2:
    plt.scatter(i[0], i[1], c='b')

#plotting centers
plt.scatter(centers[0][0], centers[0][1], c='r')
plt.scatter(centers[1][0], centers[1][1], c='r')
plt.annotate('center 1', (centers[0][0], centers[0][1]))
plt.annotate('center 1', (centers[1][0], centers[1][1]))
plt.show()