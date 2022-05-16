from math import *
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plot


n = 3.9
s = 14.1
fi = pi * 3/4

def f(tetha, r):
    dr = r/sqrt(n**2 - 1)
    return dr

def f2(t):
    xt = tan(fi*pi)*t
    return xt

r0=s/(n-1)

tetha = np.arange(0,2*pi, 0.01)
r = odeint(f, r0, tetha)

t = np.arange(0.00000000000001, 20)
r1 = np.sqrt(t**2 + f2(t)**2)
tetha1=np.arctan(f2(t)/t)

plot.rcParams["figure.figsize"] = (8, 8)

plot.polar(tetha, r, 'red', label = 'kater')
plot.polar(tetha1, r1, 'green', label = 'lodka')

tmp=0
for i in range(len(tetha)):
    if round(tetha[i], 2) == round(fi+pi, 2):
        tmp = i

print("Teta:", tetha[tmp], "r:", r[tmp][0])
print("X:", r[tmp][0]/sqrt(2), "Y:", -r[tmp][0]/sqrt(2))

plot.legend()
plot.savefig("02.png", dpi=400)


