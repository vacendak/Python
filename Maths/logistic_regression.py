import math
from random import uniform
import matplotlib.pyplot as plt


random1 = []
random2 = []
random3 = []
random4 = []
random5 = []

xlist = []

theta = [5, 2, 1, 0.5, 0.1]

for i in range(250):
    x = uniform(-5, 5)
    xlist.append(x)
    logreg1 = 1 / (1 + math.exp(-(theta[0] * x)))
    logreg2 = 1 / (1 + math.exp(-(theta[1] * x)))
    logreg3 = 1 / (1 + math.exp(-(theta[2] * x)))
    logreg4 = 1 / (1 + math.exp(-(theta[3] * x)))
    logreg5 = 1 / (1 + math.exp(-(theta[4] * x)))

    random1.append(logreg1)
    random2.append(logreg2)
    random3.append(logreg3)
    random4.append(logreg4)
    random5.append(logreg5)

print(plt.rcParams.get('figure.figsize'))
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 6
plt.rcParams["figure.figsize"] = fig_size
print(plt.rcParams.get('figure.figsize'))

plt.scatter(xlist, random1, marker='.', s=20, c='orange', alpha=0.3, label=r'$\theta = %3.1f$' % (theta[0]))
plt.scatter(xlist, random2, c='magenta', marker='.', alpha=0.3, s=20, label=r'$\theta = %3.1f$' % (theta[1]))
plt.scatter(xlist, random3, c='navy', marker='.', alpha=0.3, s=20, label=r'$\theta = %3.1f$' % (theta[2]))
plt.scatter(xlist, random4, c='green', marker='.', alpha=0.3, s=20, label=r'$\theta = %3.1f$' % (theta[3]))
plt.scatter(xlist, random5, c='red', marker='.', alpha=0.3, s=20, label=r'$\theta = %3.1f$' % (theta[4]))

plt.axhline(y=0.5, label='P=0.5')
plt.ylabel(r'P', fontsize=12)
plt.xlabel(r'$x$', fontsize=12)
plt.legend(fontsize=8)
plt.title(r'$\mathrm{P=}\frac{1}{1+e^{-(\theta \, x)}}$', fontsize=18, color='r')
plt.show()
