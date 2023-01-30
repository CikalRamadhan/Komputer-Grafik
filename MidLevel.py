print("\033c")      #donlot numpy dulu sama matlotlib di pyhton packages

import numpy as np
import matplotlib.pyplot as plt

#---------------------------------------
#Menggambar garis dan bentuk menggunakan persamaan matematika dan Matplotlib
#---------------------------------------
#kode untuk menentukan wilayah (domain) diagram cartesian
x = np.linspace(-20, 20, 10000)

#r(red), g(green), b(blue), y(yellow, m(magenta), c(cyan), w(white), k(black)
y1 = x-x-0
y2 = x + 10
y3 = (25-x**2)**0.5
y4 = -((25-x**2)**0.5)

plt.figure(figsize=(6,6.5))
plt.plot(x,     y1,             '-k', label= 'y1')
plt.plot(x,     y2,             '-g', label= 'y2')
plt.plot(x,     (0.2-x**2)**0.5, '-k')
plt.plot(x,     -((0.2-x**2)**0.5),     '-k')
plt.plot(x,     y3,             '-r', label= 'y3')
plt.plot(x,     y4,             '-r', label= 'y4')
plt.legend(loc='upper left')
plt.grid()
plt.show()