#Drawing Indonesian National Flag
print("\033c")      #To close all
import numpy as np
import matplotlib.pyplot as plt

#kode program agar bendera nya menjadi full hd
row = int(5/7*1080)
col = int(5/7*1920)

#kode agar atas, bawah, kiri dan kanan margin untuk bendera nya
#untuk persegi merah
Rrow1 = int(0.25*row)
Rrow2 = int(0.5*row)
Rcol1 = int(0.25*col)
Rcol2 = int(0.75*col)
#untuk persegi putih
Wrow1 = int(0.5*row) + 1
Wrow2 = int(0.75*row) + 1
Wcol1 = int(0.25*col)
Wcol2 = int(0.75*col)

#kode program untuk mewujudkan gambarnya
Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16)
for i in range(Rrow1, Rrow2+1):
    for j in range(Rcol1, Rcol2):
        Gambar[i, j, 0] = 255

for i in range(Wrow1, Wrow2+1):
    for j in range(Rcol1, Rcol2):
        Gambar[i, j, :] = 255


plt.figure()
plt.imshow(Gambar)
plt.show()