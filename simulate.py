from qutip import *
from numpy import sqrt, pi, array, sin, cos, arange
import matplotlib.pyplot as plt

# H = basis(2,0)
# V = basis(2,1)
# P45 = 1/sqrt(2)*(H + V)
# # M45 = 1/sqrt(2)*(H - V)
# # R = 1/sqrt(2)*(H - 1j*V)
# # L = 1/sqrt(2)*(H + 1j*V)
# Sx = 1/2.0*sigmax()

# print(Sx)


pz = basis(2,0) # i.e. the column vector (1,0)
mz = basis(2,1) # i.e. the column vector (0,1)
px = 1/sqrt(2)*(pz + mz)
mx = 1/sqrt(2)*(pz - mz)
py = 1/sqrt(2)*(pz + 1j*mz)
my = 1/sqrt(2)*(pz - 1j*mz)

Sx = 1/2.0*sigmax()
Sy = 1/2.0*sigmay()
Sz = 1/2.0*sigmaz()

omega = 5
Hz = -omega*Sz
t = arange(0,4*pi/omega,0.05)
expect_ops = [Sx,Sy,Sz]
psi0 = px
result = sesolve(Hz, psi0, t, expect_ops)


labels = ['x','y','z']
style = {'x':'-.', 'y':'--', 'z':'-'}
for r,l in zip(result.expect,labels):
    plt.plot(t*omega/pi, r, style[l], 
    label="$\langle S_%c \\rangle $" % l)
plt.xlabel("Time ($\Omega t/\pi$)", size=18)
plt.legend(fontsize=16)