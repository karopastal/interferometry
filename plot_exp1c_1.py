from lmfit import Model
import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt
font = {'family' : 'normal', 'size'   : 14}

plt.rc('font', **font)

data = loadtxt('analysis/exp1c_1.dat')

nano = np.power(10, -9.0)
p_atm = 760
red_lambda = 650*nano
d = np.power(10, -2.0)

m = data[:, 0]
delta_m = data[:, 1]

p_scale = (data[:, 2])/p_atm
delta_p = (data[:, 3])/p_atm

print("p/p_atm: ", p_scale)
print("(p/p_atm)_err: ", delta_p)

m_weights = 1/delta_m

def linear(x, a, b):
    return (a*x + b)

linear_model = Model(linear)
result = linear_model.fit(m, weights=m_weights , x=p_scale, a=1, b=1)

print(result.fit_report())
print(result.chisqr)

a = result.params['a'].value
a_err = result.params['a'].stderr

b = result.params['b'].value

n = 1 + ((a*red_lambda)/2*d)
delta_n = np.abs((red_lambda*a_err)/2*d)

print("n: ", n, "+/-", delta_n)

fig, ax = plt.subplots()

ax.set_xlabel(r'(delta p)/(p_atm)', fontsize=18)
ax.set_ylabel(r'delta m', fontsize=18)
plt.title('(delta p)/(p_atm) vs delta m', fontsize=20)

plt.plot(p_scale, m, '.C3', label='data points')
ax.errorbar(p_scale, m, yerr=delta_m, xerr=delta_p, fmt='.k', capthick=2, label='uncertainties')
plt.plot(p_scale, linear(p_scale, a, b), 'C0--', label='linear fit: y=a*x+b')

plt.legend()
plt.show()