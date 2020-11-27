import matplotlib.pyplot as plt

fileWithDots = open("Numbers.txt", "r")
listOfDots = fileWithDots.readlines()
fileWithDots.close()

x = []
y = []

for i in range(len(listOfDots)):
    listOfDots[i] = listOfDots[i].split()
    x.append(int(listOfDots[i][1]))
    y.append(int(listOfDots[i][0]))

fig, ax = plt.subplots()
sizeInInches = (7.714285714285714, 13.714285714285714)
ax.scatter(x, y, s=1)
fig.set_figwidth(sizeInInches[0])
fig.set_figheight(sizeInInches[1])
plt.savefig('plot.png', dpi=70, bbox_inches='tight')
plt.show()

