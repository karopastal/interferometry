from lmfit import Model
import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt
font = {'family' : 'normal', 'size'   : 14}

plt.rc('font', **font)

data = loadtxt('analysis/exp1d.dat')

nano = np.power(10, -9.0)
mili = np.power(10, -3.0)
red_lambda = 650*nano
d = mili

m = data[:, 0]
delta_m = data[:, 1]

theta = data[:, 2]
delta_theta = data[:, 3]

alpha2 = np.power(np.radians(theta), 2)
delta_alpha2 = np.abs(theta*delta_theta*np.power(np.pi/180, 2))

print(alpha2)
print(delta_alpha2)

m_weights = 1/delta_m

def linear(x, a, b):
    return (a*x + b)

linear_model = Model(linear)
result = linear_model.fit(m, weights=m_weights , x=alpha2, a=1, b=1)

print(result.fit_report())
print(result.chisqr)

a = result.params['a'].value
a_err = result.params['a'].stderr

b = result.params['b'].value

n = d/(d - (red_lambda*a))
delta_n = np.abs(((red_lambda*d*a_err)/np.power((d - red_lambda*a), 2)))

print("n: ", n, "+/-", delta_n)

fig, ax = plt.subplots()

ax.set_xlabel(r'alpha^2 [rad^2]', fontsize=18)
ax.set_ylabel(r'delta m', fontsize=18)
plt.title('delta m vs alpha^2', fontsize=20)

plt.plot(alpha2, m, '.C3', label='data points')
ax.errorbar(alpha2, m, yerr=delta_m, xerr=delta_alpha2, fmt='.k', capthick=2, label='uncertainties')
plt.plot(alpha2, linear(alpha2, a, b), 'C0--', label='linear fit: y=a*x+b')

plt.legend()
plt.show()