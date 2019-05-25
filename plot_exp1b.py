from lmfit import Model
import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt
font = {'family' : 'normal', 'size'   : 14}

plt.rc('font', **font)

data = loadtxt('analysis/exp1b.dat')

mili = np.power(10, -3.0)

m = data[:, 0]
delta_m = data[:, 1]

x = data[:, 2]*mili
delta_x = data[:, 3]*mili

x_weights = 1/delta_x

k = 6.769
delta_k = 0.217

def delta_green_lambda(a, a_err):
    d1 = (2*a_err)/(k)
    d2 = ((2*a)/(np.power(k, 2)))*delta_k

    return np.sqrt(np.power(d1, 2) + np. power(d2, 2))

def linear(x, a, b):
    return (a*x + b)

linear_model = Model(linear)
result = linear_model.fit(x, weights=x_weights , x=m, a=1, b=1)

print(result.fit_report())
print(result.chisqr)

a = result.params['a'].value
a_err = result.params['a'].stderr

b = result.params['b'].value

green_lambda = (2*a)/k

print(green_lambda, delta_green_lambda(a, a_err))

fig, ax = plt.subplots()

ax.set_xlabel(r'delta m', fontsize=18)
ax.set_ylabel(r'delta x [meter]', fontsize=18)
plt.title('delta x vs delta m', fontsize=20)

plt.plot(m, x, '.C3', label='data points')
ax.errorbar(m, x, yerr=delta_x, xerr=delta_m, fmt='.k', capthick=2, label='uncertainties')
plt.plot(m, linear(m, a, b), 'C0--', label='linear fit: y=a*x+b')

plt.legend()
plt.show()