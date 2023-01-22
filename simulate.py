from qutip import *
from numpy import sqrt, pi, array, sin, cos, arange
import matplotlib.pyplot as plt

H = basis(2,0)
V = basis(2,1)
P45 = 1/sqrt(2)*(H + V)
M45 = 1/sqrt(2)*(H - V)
R = 1/sqrt(2)*(H - 1j*V)
L = 1/sqrt(2)*(H + 1j*V)