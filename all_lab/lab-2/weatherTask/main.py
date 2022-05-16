from math import *
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plot

# заданые значения в задании
n = 3.5
s = 8.5
fi = pi * 2/5  # сторона побега

# диферинциальное уровнения движеняи катера
def diff(tetha, r):
    dr = r/sqrt(n**2 - 1)
    return dr

# простое уровнения описания движения лодки
def f2(t):
    xt = tan(fi+pi)*t
    return xt

#Решения первого случия когда он идет по часовой стрелке
r0 = s / (n+1)
# solved diff equations
# Задаем значения тета на какомнубуть интервале
tetha = np.arange(0, 2*pi, 0.01)
r = odeint(diff, r0, tetha)

# простой превод из обычных координат в полярные
t = np.arange(0.00000000000001, 20)
r1=np.sqrt(t**2 + f2(t)**2)
tetha1 = np.arctan(f2(t)/t)
#Рисования  картинки
plot.rcParams["figure.figsize"] = (10, 10)

plot.polar(tetha, r, 'red')
plot.polar(tetha1, r1, 'green')

tmp = 0
for i in range(len(tetha)):
    if round(tetha[i], 2) == round(fi+pi, 2):
        tmp=1

print("Teta:", tetha[tmp], "r:", r[tmp][0])
print("X:", r[tmp][0]/sqrt(2), "Y:", -r[tmp][0]/sqrt(2))

plot.legend()
plot.savefig("01.png", dpi=400)

r0 = s/(n-1)

tetha = np.arange(0, 2*pi, 0.01)
r = odeint(diff, r0, tetha)
# вычесления троектории лодки
t=np.arange(0.00000000000001, 20)
r1=np.sqrt(t**2+f2(t)**2)
tetha1 = np.arctan(f2(t)/t)

plot.rcParams["figure.figsize"] = (8, 8)

plot.polar(tetha, r, 'black', label = 'катер')
plot.polar(tetha1, r1, 'red', label = 'лодка')

# вычесления точка пересичения
tmp=0
for i in range(len(tetha)):
    if round(tetha[i], 2) == round(fi+pi, 2):
        tmp=i
print("Тета:", tetha[tmp], "r:", r[tmp][0])
print("X:", r[tmp][0]/sqrt(2), "Y:", -r[tmp][0]/sqrt(2))
plot.legend()
plot.savefig("02.png", dpi=400)