import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

# числиность армии
x0 = 895000
y0 = 577000
#время
t0 = 0
tmax = 1
# коэффициенты регулярная армия
a = 0.34
b = 0.93
c = 0.54
h = 0.29
# портизаны
a2 = 0.31
b2 = 0.88
c2 = 0.41
h2 = 0.41
# функции подкрепления
def support(t):
    p=2*math.sin(t)
    return p

def Q(t):
    q=math.cos(t)+3
    return q


def support2(t):
    p=2*math.sin(2*t)
    return p

def Q2(t):
    q=math.cos(t)+3
    return q
# Система дифферинциальных уровнений
def f(y, t):
    y1, y2 = y
    return [-a * y1 - b * y2 + support(t), -c * y1 - h * y2 + Q(t)]

def f2(y, t):
    y1, y2 = y
    return [-a2 * y1 - b2 * y2 + support2(t), -c2 * y1 * y2 - h2 * y2 + Q2(t)]

# решения уровнений
t = np.linspace( 0, tmax, num = 100)
y0 = [x0, y0]
w1 = odeint(f, y0, t)
y11 = w1[:,0]
y21 = w1[:,1]
fig = plt.figure(facecolor='white')
plt.plot(t, y11, t, y21, linewidth=2)
plt.ylabel("x, y")
plt.xlabel("t")
plt.grid(True)
plt.show()
fig.savefig('03.png', dpi = 600)

w1 = odeint(f2, y0, t)
y12 = w1[:,0]
y22 = w1[:,1]
fig2 = plt.figure(facecolor='white')
plt.plot(t, y12, t, y22, linewidth=2)
plt.ylabel("x, y")
plt.xlabel("t")
plt.grid(True)
plt.show()
fig2.savefig('04.png', dpi = 600)