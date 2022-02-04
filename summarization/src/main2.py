from function import *
import random
import itertools

# # File Source
# filename = "tester 1.txt"
# # filename = "teks.txt"
#
# # Open File
# with open(filename, 'r') as myfile:
#     meta = myfile.read()


def peringkasan(meta, tingkat):
    # Get Matriks
    (type_per_kalimat, paragraph) = function_split_teks(meta)
    # print(paragraph)
    (x, sentences, term, list_stopwords) = get_matrix(type_per_kalimat, paragraph)
    jml_kalimat = len(x)
    jml_t = len(term)

    # Inisialisasi
    # peringkasan = 30%
    peringkasan = tingkat
    jml_kal_ringkasan = math.ceil(jml_kalimat*peringkasan)
    c = jml_kal_ringkasan
    w = 2
    persentase_jarak = 0.4
    persentase_bobot = 0.6
    max_iter = 100
    e = 0.000016
    p = []
    p.append(0)
    t = 1
    u = []
    pangkat = -1/w-1
    iterasi = 0;

    for i in range(0, jml_kalimat):
        r = [random.random() for i in range(0, c)]
        s = sum(r)
        r = [i/s for i in r]
        u.append(r)

    # u = list(map(list, zip(*u)))

    while True:
        iterasi = iterasi+1
        # iterasi = 100

        # Menguadratkan nilai masing2 index U dan menghitung nilai total u2
        u2 = []
        for i in u:
            u2.append([y * y for y in i])

        u2 = list(map(list, zip(*u2)))
        # print(len(u2))
        # print(len(u2[0]))

        total_u2 = ([sum(y) for y in u2])
        # print(total_u2)

        u2x = []
        total_u2x = []

        # print(len(u2))

        for i in range(0, c):
            u2x_kalimat = []
            temp_total_u2x = []
            for j in range(0, jml_kalimat):
                temp = []
                total = 0
                for k in range(0, jml_t):
                    hitung_u2x = u2[i][j]*x[j][k]
                    temp.append(hitung_u2x)
                u2x_kalimat.append(temp)
                # temp_total_u2x.append(sum(temp))
            # total_u2x.append(temp_total_u2x)
            u2x.append(u2x_kalimat)

        # print(len(u2x))
        # print(len(u2x[0]))
        # print(len(u2x[0][0]))
        temp2 = []
        for i in range(0, c):
            temp = []
            for j in range(0, jml_t):
                total = 0
                for k in range(0, jml_kalimat):
                    total = total+u2x[i][k][j]
                temp.append(total)
            total_u2x.append(temp)

        # print(len(total_u2))
        # print(len(u2x_kalimat))
        # print(len(u2x_kalimat[0]))


        # Hitung pusat cluster
        # print(len(total_u2x[0][0]))
        #
        pusat_cluster = []
        for i in range(0, c):
            temp = []
            for j in total_u2x[i]:
                temp.append(j/total_u2[i])
            pusat_cluster.append(temp)

        # print(pusat_cluster)
        #
        # print(len(pusat_cluster))
        # print(len(pusat_cluster[0]))

        # Hitung fungsi objektif

        fungsi_objektif = []
        partisi = []
        for i in range(0, c):
            subtotal = []
            temp = []
            temp_partisi = []
            for j in range(0, jml_kalimat):
                hasil = 0
                for k in range(0, jml_t):
                    count = (x[j][k] - pusat_cluster[i][k])
                    hasil = hasil + round((count * count), 32)
                    # hasil = hasil + (count * count)
                if hasil != 0.0:
                    temp_partisi.append(pow(hasil, pangkat))
                else:
                    temp_partisi.append(0)
                hitung = hasil*u2[i][j]
                temp.append(hitung)
            partisi.append(temp_partisi)
            temp2.append(temp)
            # temp2 = list(map(list, zip(*temp)))

        fungsi_objektif = list(map(list, zip(*temp2)))
        for i in fungsi_objektif:
            subtotal.append(sum(i))

        partisi = list(map(list, zip(*partisi)))
        subtotal_partisi = []
        for i in partisi:
            subtotal_partisi.append(sum(i))

        total_fungsi_objektif = sum(subtotal)
        p.append(total_fungsi_objektif)

        # print(len(partisi))
        # print(len(partisi[0]))

        # Update matriks U / matriks partisi
        u = []
        for i in range(0, jml_kalimat):
            temp_u = []
            for j in range(0, c):
                temp_u.append(partisi[i][j] / subtotal_partisi[i])
            u.append(temp_u)

        print("\nIterasi ke-%d" %iterasi)
        print(p[iterasi])

        if iterasi >= max_iter or abs(p[iterasi]-p[iterasi-1]) < e:
            break

    distance = []
    for i in range(0, c):
        temp2 = []
        for j in range(0, jml_kalimat):
            temp = []
            for k in range(0, jml_t):
                d = x[j][k] - pusat_cluster[i][k]
                d = d*d
                temp.append(d)
            temp2.append(sum(temp))
        distance.append(temp2)

    distance = list(map(list, zip(*distance)))
    # print('distance')
    # print(distance)

    temp = []
    cluster = []
    # Peringkasan dengan rule ambil kalimat dari setiap cluster hingga batas kalimat terpenuhi
    # ========================================================================================

    bobot = bobot_kalimat(x, jml_t, jml_kalimat)
    bobot_max = max(bobot)
    for i in range(0, c):
        temp.append([])

    for i in range(0, c):
        for j in range(0, jml_kalimat):
            value = min(distance[j])
            index = distance[j].index(value)
            if index == i:
                temp[i].append([j, index, value, bobot[j]])
        # print('before')
        # print(temp[i])
        temp[i].sort(key=lambda x:x[2])
        # print('after')
        # print(temp[i])
        cluster.append(temp[i])
        # print('cluster')
        # print(cluster[i])
    # print('total')
    # print(cluster)

    nilai_kalimat = []
    temp_nilai_kalimat = []
    # print('bobot max')
    # print(bobot_max)

    # Kolaborasi Nilai Bobot dan jarak
    for i in range(0, c):
        nilai_kalimat.append([])
        for j in range(0, len(cluster[i])):
            jarak = cluster[i][j][2]
            bobot_per_kalimat = cluster[i][j][3]
            temp_jarak = (bobot_max - cluster[i][j][2]) * persentase_jarak
            temp_bobot = cluster[i][j][3] * persentase_bobot
            no_kalimat = cluster[i][j][0]
            nilai_kalimat[i].append([no_kalimat, temp_jarak + temp_bobot, jarak, bobot_per_kalimat])
        nilai_kalimat[i].sort(reverse=True, key=lambda x: x[1])
        temp_nilai_kalimat.append(nilai_kalimat[i])

    print(nilai_kalimat)
    print(temp_nilai_kalimat)

    # print(cluster)
    cluster2 = []
    counter = 0
    for i in range(0, c):
        if len(nilai_kalimat[i]) is not 0:
            cluster2.append(nilai_kalimat[i][0])
        else:
            counter = counter+1

    # print('ini counter')
    # print(counter)
    if counter > 0:
        cluster_cadangan = []
        for i in range(0, c):
            for j in range(0, len(cluster[i])):
                temp_jarak = (bobot_max - cluster[i][j][2]) * persentase_jarak
                temp_bobot = cluster[i][j][3] * persentase_bobot
                no_kalimat = cluster[i][j][0]
                jarak = cluster[i][j][2]
                bobot_per_kalimat = cluster[i][j][3]
                cluster_cadangan.append([no_kalimat, temp_jarak + temp_bobot, jarak, bobot_per_kalimat])
                cluster_cadangan.sort(reverse=True, key=lambda x: x[1])

        counter2 = 0
        while True:
            for i in cluster_cadangan:
                if i not in cluster2:
                    cluster2.append(i)
                    counter2 = counter2+1
                if counter2 == counter:
                    break
            if counter2 == counter:
                break
    cluster2.sort(reverse=True, key=lambda x: x[1])
    # print('cluster2')
    # print(cluster2)

    tf_isf = ''
    for i in range(0, jml_kalimat):
        if i == 0:
            tf_isf = 'Kalimat %d' %(i+1)
        else:
            tf_isf = tf_isf+'\n\nKalimat %d' %(i+1)

        tf_isf = tf_isf+'\n'+paragraph[i]+'\n'+str(x[i])

    # KODE PROGRAM PENYUSUN TEKS KALIMAT HASIL CLUSTERING
    # kalimat_ringkasan = []
    result = ''
    for i in range(0, len(nilai_kalimat)):
        for j in range(0, len(nilai_kalimat[i])):
            index_kal = nilai_kalimat[i][j][0]
            pusat_cluster_kal = nilai_kalimat[i][j][2]
            temp_bobot_kalimat = nilai_kalimat[i][j][3]
            teks = paragraph[index_kal] + ' (%f) (%f)' % (temp_bobot_kalimat, pusat_cluster_kal)
            # kalimat_ringkasan.append(paragraph[index_kal])
            if i == 0 and j == 0:
                result = 'Cluster 1\n' + teks + '.\n\n'
            elif j == 0:
                result = result + 'Cluster %d\n' % (i + 1) + teks + '.\n\n'
            else:
                result = result + teks + '.\n\n'

    # Penyusun Teks Hasil Ringkasan
    kalimat = ''
    list_kalimat_ringkasan = []
    for j in range(0, c):
        index_kal = cluster2[j][0]
        if j == 0:
            kalimat = paragraph[index_kal]+'.'
        else:
            kalimat = kalimat+' '+paragraph[index_kal]+'.'
        list_kalimat_ringkasan.append(paragraph[index_kal])

    # print(len(cluster))
    # print(len(cluster[0]))
    # print(len(cluster[0][0]))

    # print('bobot max')
    # print(bobot_max)
    # print(nilai_kalimat)
    # print(jml_kal_ringkasan)
    # print(cluster2)
    kalimat_ringkasan = []

    # print(result)
    # print(jml_t)
    # print(jml_kalimat)
    temp_tf_idf = list(map(list, zip(*x)))
    tf_idf = []

    for i in temp_tf_idf:
        tf_idf.append(sum(i))

    # print('tf_isf')
    # print(tf_isf)

    freq_tf = ''
    for i in range(0, jml_t):
        if i == 0:
            freq_tf = term[i]+'= '+str(tf_idf[i])
        else:
            freq_tf = freq_tf+'\n'+term[i]+'= '+str(tf_idf[i])

    print("Jumlah Kalimat Ringkasan")
    print(jml_kal_ringkasan)

    return term, freq_tf, tf_isf, kalimat, list_stopwords, result, paragraph, list_kalimat_ringkasan
    #==========================Sampai Sini================================


    # # Peringkasan berdasarkan kalimat yang paling dekat dengan pusat clusternya
    # for i in range(0, c):
    #     for j in range(0, jml_kalimat):
    #         value = min(distance[j])
    #         index = distance[j].index(value)
    #         if index == i:
    #             cluster.append([j, index, value])
    #     cluster.sort(key=lambda x: x[2])
    #
    # kalimat = ''
    #
    # for i in range(0, jml_kal_ringkasan):
    #     if i == 0:
    #         kalimat = paragraph[i] + '.'
    #     else:
    #         kalimat = kalimat + ' ' + paragraph[i] + '.'
    #
    # tf_isf = ''
    # for i in range(0, jml_kalimat):
    #     if i == 0:
    #         tf_isf = 'Kalimat %d' %(i+1)
    #     else:
    #         tf_isf = tf_isf+'\n\nKalimat %d' %(i+1)
    #
    #     tf_isf = tf_isf+'\n'+str(x[i])
    #
    # # print(tf_isf)
    # return term, tf_isf, kalimat
    # #==========================Sampai Sini================================#



    # counter = 0
    # for i in range(0, c):
    #     for j in range(0, jml_kalimat):
    #         if counter == c:
    #             counter = 0
    # print(cluster[0][1])

    # for i in range(0, jml_kal_ringkasan):

    # print(len(total_u2x))
    # print(len(total_u2x[0]))
    # print(len(pusat_cluster))
    # print(len(pusat_cluster[0]))

    # print("\nNilai x")
    # print(x)

    # print("\nNilai Fungsi Objektif")
    # print(fungsi_objektif)
    #
    # print("\nSubtotal")
    # print(subtotal_fungsi_objektif)


