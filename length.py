import matplotlib.pyplot as plt

from collatz import collatz

x = []
y = []
for n in range(1, 5000):
    x.append(n)
    y.append(len(collatz(n)))

fig, ax = plt.subplots()
ax.plot(x, y, 'x', markersize=1)
ax.set(xlabel='n', ylabel='length', title='Length of Collatz sequence')
plt.show()
