import random
import matplotlib.pyplot as plt

len = 10
probability = 0.5
mutation = 0.4
population = 100

gene = population*[population*[0]]

def genetic():

    minimum = 1000000

    for i in range(0, population):
        for j in range(0, len):
            rand = random.random()
            if rand < 0.5:
                gene[i][j] = 0
            else:
                gene[i][j] = 1

    count = 1
    x = []
    mins = []

    while (True):

        x.append(count)

        a = int(population * random.random())
        b = int(population * random.random())

        fa = fitness(a)
        fb = fitness(b)
        minf = 0

        if (fa < fb):
            winner = a
            loser = b
            minf = fa
        else:
            winner = b
            loser = a
            minf = fb
        for i in range(0, len):
            if (random.random() < probability):
                gene[loser][i] = gene[winner][i]
            if (random.random() < mutation):
                gene[loser][i] = 1 - gene[loser][i]
            if (minf < minimum):
                minimum = minf
            if (fitness(loser) == 0.0):
                mins.append(0)
                showResult(count, loser)
                plot(x, mins)
                return

        mins.append(minimum)
        count += 1

def fitness(n):

    sum = 0
    pr = 1
    for i in range(0, len):
        if gene[n][i] == 0:
            sum += (1 + i)
        else:
            pr *= 1 + i

    sumError = (sum - 36) / 36
    prError = (pr - 360) / 360
    error = abs(sumError) + abs(prError)

    return error

def showResult(count, card):
    print("count: ", count)
    sum = 0
    pr = 1
    print ("group 1: ")
    for i in range(0, len):
        if gene[card][i] == 0:
            print (i)
            sum += (1 + i)
    print ("sum: ", sum)
    print ("group 2: ")
    for i in range(0, len):
        if gene[card][i] == 1:
            print (i)
            pr *= 1 + i
    print ("pr: ", pr)

def plot(x, y):
    plt.scatter(x, y)
    plt.show()

genetic()