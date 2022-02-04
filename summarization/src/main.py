from function import *
import random
import itertools

# File Source
# filename = "tester 1.txt"
filename = "teks.txt"

# Open File
with open(filename, 'r') as myfile:
    meta = myfile.read()

# Get Matriks
(type_per_kalimat, paragraph) = function_split_teks(meta)
(x, sentences, t) = get_matrix(type_per_kalimat, paragraph)
print(x)
jml_kalimat = len(x)
jml_t = len(t)

# Inisialisasi
c = 2
w = 2
max_iter = 100
e = 0.01
p = []
p.append(0)
t = 1
u = []
pangkat = -1/w-1
iterasi = 0;

for i in range(0, jml_t):
    r = [random.random() for i in range(0, c)]
    s = sum(r)
    r = [i/s for i in r]
    u.append(r)

# u = list(map(list, zip(*u)))

while True:
    # iterasi = iterasi+1
    iterasi = 100
    print(len(u))


    # Menguadratkan nilai masing2 index U dan menghitung nilai total u2
    u2 = []
    for i in u:
        u2.append([y*y for y in i])

    total_u2 = ([sum(y) for y in u2])


    u2x = []
    total_u2x = []

    for i in range(0, c):
        u2x_kalimat = []
        temp_total_u2x = []
        for j in range(0, jml_kalimat):
            temp = []
            total = 0
            for k in range(0, jml_t):
                hitung_u2x = u2[i][k]*x[j][k]
                temp.append(hitung_u2x)
            u2x_kalimat.append(temp)
            temp_total_u2x.append(sum(temp))
        total_u2x.append(temp_total_u2x)
        u2x.append(u2x_kalimat)

    # print(total_u2)
    # print(total_u2x)

    # Hitung pusat cluster
    pusat_cluster = []
    for i in range(0, c):
        pusat_cluster.append([j/total_u2[i] for j in total_u2x[i]])
        # pusat_cluster.append([y*y for y in i])

    # print(pusat_cluster)

    # Hitung fungsi objektif
    fungsi_objektif = []
    for h in range(0, jml_t):
        temp_fungsi_objektif = []
        for i in range(0, c):
            temp_fungsi_objektif.append((sum([(pusat_cluster[i][j]*x[j][h])**2 for j in range(0, jml_kalimat)]))*u2[i][h])
        fungsi_objektif.append(temp_fungsi_objektif)

    subtotal_fungsi_objektif = []


    for i in fungsi_objektif:
        subtotal_fungsi_objektif.append(sum(i))

    total_fungsi_objektif = sum(subtotal_fungsi_objektif)
    # print(total_fungsi_objektif)
    p.append(total_fungsi_objektif)


    # Update matriks U / matriks partisi
    u = []
    for h in range(0, jml_t):
        temp_u = []
        temp_u_2 = []
        for i in range(0, c):
            temp_u.append((sum([(pusat_cluster[i][j]*x[j][h]) ** 2 for j in range(0, jml_kalimat)])) ** pangkat)
        total = sum(temp_u)
        u.append([temp_u[i]/total for i in range(0, c)])

    u = list(map(list, zip(*u)))
    # print("\nIterasi ke-%d" %iterasi)
    # print(p[iterasi])
    if iterasi >= max_iter or abs(p[iterasi]-p[iterasi-1]) < e:
        break


# print("\nNilai x")
# print(x)

# print("\nNilai Fungsi Objektif")
# print(fungsi_objektif)
#
# print("\nSubtotal")
# print(subtotal_fungsi_objektif)