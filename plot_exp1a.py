from lmfit import Model
import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt
font = {'family' : 'normal', 'size'   : 14}

plt.rc('font', **font)

data = loadtxt('analysis/exp1a.dat')

mili = np.power(10, -3.0)

red_lambda = 650*np.power(10, -9.0)

m = data[:, 0]
delta_m = data[:, 1]

x = data[:, 2]*mili
delta_x = data[:, 3]*mili

x_weights = 1/delta_x

def linear(x, a, b):
    return (a*x + b)

linear_model = Model(linear)
result = linear_model.fit(x, weights=x_weights , x=m, a=1, b=1)

print(result.fit_report())
print(result.chisqr)

a = result.params['a'].value
a_err = result.params['a'].stderr

b = result.params['b'].value

k = (2*a)/red_lambda
delta_k = 2*a_err/red_lambda

print(k, delta_k)

fig, ax = plt.subplots()

ax.set_xlabel(r'delta m', fontsize=18)
ax.set_ylabel(r'delta x [meter]', fontsize=18)
plt.title('delta x vs delta m', fontsize=20)

plt.plot(m, x, '.C3', label='data points')
ax.errorbar(m, x, yerr=delta_x, xerr=delta_m, fmt='.k', capthick=2, label='uncertainties')
plt.plot(m, linear(m, a, b), 'C0--', label='linear fit: y=a*x+b')

plt.legend()
plt.show()