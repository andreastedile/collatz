import matplotlib.pyplot as plt

from collatz import collatz

x = []
y = []
for n in range(1, 5000 ):
    x.append(n)
    y.append(max(collatz(n)))

fig, ax = plt.subplots()
ax.plot(x, y, 'o', markersize=1)
ax.set(xlabel='n', ylabel='max', title='Maximum value of Collatz sequence')
plt.show()
