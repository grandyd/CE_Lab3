import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import odeint

def system(v, t):
   dx1dt = v[1]
   dy1dt = (-k*v[0] - u*(v[0] - v[2]))/m
   dx2dt = v[3]
   dy2dt = (-k*v[2] + u*(v[0] - v[2]))/m
   return [dx1dt, dy1dt, dx2dt, dy2dt]

if __name__=='__main__':
   m = 4.56
   u = 3.0
   k = 38

   A=-(k+u)/m
   B=u/m

   v=[4,0,0,0]
   C1 = 2
   C2 = 0.5

   t = np.linspace(0, 58, 140)

   omega1=(A+B)**(1/2)
   omega2=(A-B)**(1/2)
   x1 = C1*np.exp(omega1*t)*(1 + (C2/C1)*np.exp((omega2 - omega1)*t))
   x2 = C1*np.exp(omega1*t)*(1 - (C2/C1)*np.exp((omega2 - omega1)*t))

   solution = odeint(system, v, t)
   y1 = solution[:, 0] + x1
   y2 = solution[:, 2] + x2

   plt.plot(t, y1.real)
   plt.xlabel('t')
   plt.ylabel('x1')
   plt.savefig('blue1.png')
   plt.show()

   plt.plot(t, y2.real, 'orange')
   plt.xlabel('t')
   plt.ylabel('x2')
   plt.savefig('orange1.png')
   plt.show()
