print("\033c")      #To close all
import numpy as np
import matplotlib.pyplot as plt

row = int(5/7*1080)
col = int(5/7*1920)

Yrow1 = int(0.25*row)
Yrow2 = int(0.5*row)
Ycol1 = int(0.25*col)
Ycol2 = int(0.75*col)
Mrow1 = int(0.5*row) + 1
Mrow2 = int(0.75*row) + 1
Mcol1 = int(0.25*col)
Mcol2 = int(0.75*col)

#kode program untuk mewujudkan gambarnya
Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16)
for i in range(Yrow1, Yrow2+1):
    for j in range(Ycol1, Ycol2):
        Gambar[i, j, 0] = 255

for i in range(Mrow1, Mrow2+1):
    for j in range(Mcol1, Mcol2):
        Gambar[i, j, :] = 255


plt.figure()
plt.imshow(Gambar)
plt.show()