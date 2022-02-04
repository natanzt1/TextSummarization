import math
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def function_tokenization(data):
    special_char = ['!','@', '?', '-', '.', ',', '"', ';', '—', "'", '"', '“', '’', '”']
    remove_character = data
    for char in special_char:
        while char in remove_character:
            remove_character = remove_character.replace(char, "")
    remove_split_line = ' '.join(remove_character.splitlines())
    remove_dbl_space = remove_split_line.replace('  ', ' ')
    lowercase = remove_dbl_space.lower()
    words = lowercase.split(' ')

    if '' in words:
        words.remove('')

    for x in range(0, len(words)):
        words[x] = stemmer.stem(words[x])

    return words


def function_type(words):
    i = 0
    k = 0
    count_word = len(words)
    token = []
    stemming = []


    for k in range(count_word):
        token.append(0)

    k = 0
    for word in words:
        if word not in token:
            token[i] = word
            i += 1

    for i in range(count_word):
        if 0 in token:
            token.remove(0)

    token.sort()
    type = []
    # type2 = []
    factory = StopWordRemoverFactory()
    stopWords = factory.get_stop_words()
    for w in token:
        if w not in stopWords:
            type.append(w)
            # type2.append(w)
    return type


def function_get_stopwords(words):
    i = 0
    k = 0
    count_word = len(words)
    token = []
    stemming = []


    for k in range(count_word):
        token.append(0)

    k = 0
    for word in words:
        if word not in token:
            token[i] = word
            i += 1

    for i in range(count_word):
        if 0 in token:
            token.remove(0)

    token.sort()
    type = []
    # type2 = []
    factory = StopWordRemoverFactory()
    stopWords = factory.get_stop_words()
    list_stopwords = []
    for w in token:
        if w in stopWords and w not in list_stopwords:
            list_stopwords.append(w)

    # print(list_stopwords)
    return list_stopwords


def function_cari_term(teks_biasa):
    data = teks_biasa
    words = function_tokenization(data)

    type = function_type(words)
    list_stopwords = function_get_stopwords(words)
    return type, list_stopwords


def function_split_teks(paragraf):
    # data = paragraf
    paragraph = []
    data = paragraf.split('\n')

    if '' in data:
        data.remove('')

    all_kalimat = ''
    jml_para = len(data)
    # Untuk mengelompokkan kalimat dalam satu paragraf
    for x in range(0, jml_para):
        if '! ' in data[x]:
            data[x] = data[x].replace('! ', '. ')
        elif '? ' in data[x]:
            data[x] = data[x].replace('? ', '. ')

        if all_kalimat == '':
            all_kalimat = data[x]
        else:
            all_kalimat = all_kalimat+' '+data[x]

    if '. ' in all_kalimat:
        paragraph = all_kalimat.split('. ')

    if '' in paragraph:
        paragraph.remove('')

    for y in range(0, len(paragraph)):
        if '.' in paragraph[y]:
            paragraph[y] = paragraph[y].replace('.', '')
    # ============================================================
    # print(paragraph)

    type_per_kalimat = []
    for x in paragraph:
        words = function_tokenization(x)
        type_per_kalimat.append(function_type(words))
    return (type_per_kalimat, paragraph)


def get_matrix(type_per_kalimat, paragraph):
    counter = 0
    # print(paragraph)
    for x in paragraph:
        if counter == 0:
            kalimat = x
            counter += 1
        else:
            kalimat = kalimat + '. ' + x

    type, list_stopwords = function_cari_term(kalimat)
    words = type_per_kalimat

    tf_all = []
    for x in words:
        type_paragraph = []
        for a_type in type:
            count = 0
            for word in x:
                if a_type == word:
                    count = count + 1
                    # Frequency tiap term dicatat setelah looping ketiga berhenti
                    # Looping ketiga adalah looping untuk membandingkan term dengan setiap kata pada kalimat
            type_paragraph.append(count)
        tf_all.append(type_paragraph)
    x = tf_all
    sentences = words
    t = type

    return x, sentences, t, list_stopwords


def check_df(temp, jml_kal, jml_t):
    df = []
    for i in range(0, jml_t):
        count = 0
        for j in range(0, jml_kal):
           if temp[i][j] > 0:
               count = count+1
        df.append(count)

    return df


def bobot_kalimat(x, jml_t, jml_kal):
    temp = list(map(list, zip(*x)))
    df = check_df(temp, jml_kal, jml_t)
    bobot = []
    for i in range(0, jml_kal):
        hasil2 = 0
        for j in range(0, jml_t):
            hasil = temp[j][i] * math.log10(jml_kal/df[j])
            hasil2 = hasil2+hasil
        bobot.append(hasil2)

    return bobot



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



# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        self.status = 0
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1000, 712), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook1 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel1 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        fgSizer3 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText6 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Open File", wx.Point(-1, -1), wx.Size(200, 20),
                                           0)
        self.m_staticText6.Wrap(-1)
        fgSizer3.Add(self.m_staticText6, 0, wx.ALL, 5)

        fgSizer4 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_filePicker2 = wx.FilePickerCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                               wx.DefaultPosition, wx.Size(500, -1), wx.FLP_DEFAULT_STYLE)
        fgSizer4.Add(self.m_filePicker2, 0, wx.ALL, 5)

        fgSizer9 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer9.SetFlexibleDirection(wx.BOTH)
        fgSizer9.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_button8 = wx.Button(self.m_panel1, wx.ID_ANY, u"Open File", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer9.Add(self.m_button8, 0, wx.ALL, 5)

        # self.m_button3 = wx.Button(self.m_panel1, wx.ID_ANY, u"Evaluasi Sistem", wx.DefaultPosition, wx.DefaultSize, 0)
        # fgSizer9.Add(self.m_button3, 0, wx.ALL, 5)

        fgSizer4.Add(fgSizer9, 1, wx.EXPAND, 5)

        fgSizer3.Add(fgSizer4, 1, wx.EXPAND, 5)

        bSizer4.Add(fgSizer3, 1, wx.EXPAND, 5)

        self.m_textCtrl1 = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(970, 100),
                                       wx.TE_MULTILINE)
        bSizer4.Add(self.m_textCtrl1, 0, wx.ALL, 5)

        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText10 = wx.StaticText(self.m_panel1, wx.ID_ANY, u" Tingkat Peringkasan", wx.Point(-1, -1),
                                            wx.Size(200, -1), 0)
        self.m_staticText10.Wrap(-1)
        fgSizer2.Add(self.m_staticText10, 0, wx.ALL, 5)

        fgSizer8 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer8.SetFlexibleDirection(wx.BOTH)
        fgSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        m_comboBox2Choices = [u"10%", u"20%", u"30%", u"40%", u"50%"]
        self.m_comboBox2 = wx.ComboBox(self.m_panel1, wx.ID_ANY, u"10%", wx.DefaultPosition, wx.Size(255, -1),
                                       m_comboBox2Choices, 0)
        self.m_comboBox2.SetSelection(0)
        fgSizer8.Add(self.m_comboBox2, 0, wx.ALL, 5)

        self.m_button1 = wx.Button(self.m_panel1, wx.ID_ANY, u"Process", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer8.Add(self.m_button1, 0, wx.ALL, 5)

        fgSizer2.Add(fgSizer8, 1, wx.EXPAND, 5)

        bSizer4.Add(fgSizer2, 1, wx.EXPAND, 5)

        fgSizer7 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer7.SetFlexibleDirection(wx.BOTH)
        fgSizer7.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer81 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer81.SetFlexibleDirection(wx.BOTH)
        fgSizer81.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText31 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Term", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        fgSizer81.Add(self.m_staticText31, 0, wx.ALL, 5)

        self.m_staticText27 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Stopwords", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText27.Wrap(-1)
        fgSizer81.Add(self.m_staticText27, 0, wx.ALL, 5)

        self.m_textCtrl112 = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(200, 125), wx.TE_MULTILINE)
        fgSizer81.Add(self.m_textCtrl112, 0, wx.ALL, 5)

        self.m_textCtrl1121 = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(250, 125), wx.TE_MULTILINE)
        fgSizer81.Add(self.m_textCtrl1121, 0, wx.ALL, 5)

        fgSizer7.Add(fgSizer81, 1, wx.EXPAND, 5)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"TF-ISF", wx.DefaultPosition, wx.Size(470, -1), 0)
        self.m_staticText3.Wrap(-1)
        bSizer2.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_textCtrl11 = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(500, 125),
                                        wx.TE_MULTILINE)
        bSizer2.Add(self.m_textCtrl11, 0, wx.ALL, 5)

        fgSizer7.Add(bSizer2, 1, wx.EXPAND, 5)

        bSizer4.Add(fgSizer7, 1, wx.EXPAND, 5)

        fgSizer5 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer5.SetFlexibleDirection(wx.BOTH)
        fgSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        bSizer4.Add(fgSizer5, 1, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText26 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Hasil Clustering Kalimat", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText26.Wrap(-1)
        bSizer3.Add(self.m_staticText26, 0, wx.ALL, 5)

        self.m_textCtrl14 = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(970, 150),
                                        wx.TE_MULTILINE)
        bSizer3.Add(self.m_textCtrl14, 0, wx.ALL, 5)

        bSizer4.Add(bSizer3, 1, wx.EXPAND, 5)

        self.m_staticText5 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Hasil Ringkasan", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer4.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_textCtrl111 = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(970, 100), wx.TE_MULTILINE)
        bSizer4.Add(self.m_textCtrl111, 0, wx.ALL, 5)

        self.m_panel1.SetSizer(bSizer4)
        self.m_panel1.Layout()
        bSizer4.Fit(self.m_panel1)
        self.m_notebook1.AddPage(self.m_panel1, u"Peringkasan", False)
        self.m_panel2 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText9 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Teks", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        self.bSizer6.Add(self.m_staticText9, 0, wx.ALL, 5)

        self.m_textCtrl12 = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(970, 100),
                                        wx.TE_MULTILINE | wx.TE_READONLY)
        self.bSizer6.Add(self.m_textCtrl12, 0, wx.ALL, 5)

        self.m_staticline6 = wx.StaticLine(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        self.bSizer6.Add(self.m_staticline6, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText13 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Kalimat Hasil Ringkasan", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)
        self.bSizer6.Add(self.m_staticText13, 0, wx.ALL, 5)

        self.m_textCtrl113 = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(970, 100), wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
        self.bSizer6.Add(self.m_textCtrl113, 0, wx.ALL, 5)

        self.m_staticline3 = wx.StaticLine(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        self.bSizer6.Add(self.m_staticline3, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText101 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"List Kalimat", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText101.Wrap(-1)
        self.bSizer6.Add(self.m_staticText101, 0, wx.ALL, 5)

        self.m_scrolledWindow5 = wx.ScrolledWindow(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow5.SetScrollRate(5, 5)
        self.bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow5.SetSizer(self.bSizer8)
        self.m_scrolledWindow5.Layout()
        self.bSizer8.Fit(self.m_scrolledWindow5)
        self.bSizer6.Add(self.m_scrolledWindow5, 1, wx.EXPAND | wx.ALL, 5)

        self.m_button4 = wx.Button(self.m_panel2, wx.ID_ANY, u"Nilai", wx.DefaultPosition, wx.DefaultSize, 0)
        self.bSizer6.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_staticline4 = wx.StaticLine(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        self.bSizer6.Add(self.m_staticline4, 0, wx.EXPAND | wx.ALL, 5)

        fgSizer91 = wx.FlexGridSizer(2, 3, 0, 0)
        fgSizer91.SetFlexibleDirection(wx.BOTH)
        fgSizer91.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText11 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Precission (%)", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText11.Wrap(-1)
        fgSizer91.Add(self.m_staticText11, 0, wx.ALL, 5)

        self.m_staticText111 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Recall (%)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText111.Wrap(-1)
        fgSizer91.Add(self.m_staticText111, 0, wx.ALL, 5)

        self.m_staticText1111 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Accuracy (%)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1111.Wrap(-1)
        fgSizer91.Add(self.m_staticText1111, 0, wx.ALL, 5)

        self.m_textCtrl13 = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, 40),
                                        0)
        fgSizer91.Add(self.m_textCtrl13, 0, wx.ALL, 5)

        self.m_textCtrl131 = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, 40),
                                         0)
        fgSizer91.Add(self.m_textCtrl131, 0, wx.ALL, 5)

        self.m_textCtrl1311 = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, 40),
                                          0)
        fgSizer91.Add(self.m_textCtrl1311, 0, wx.ALL, 5)

        self.bSizer6.Add(fgSizer91, 1, wx.EXPAND, 5)

        self.m_panel2.SetSizer(self.bSizer6)
        self.m_panel2.Layout()
        self.bSizer6.Fit(self.m_panel2)
        self.m_notebook1.AddPage(self.m_panel2, u"Evaluasi", False)

        bSizer1.Add(self.m_notebook1, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.m_panel2.Disable()

        self.Centre(wx.BOTH)
        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, self.process)
        self.m_button8.Bind(wx.EVT_BUTTON, self.openfile)
        self.m_panel2.Bind(wx.EVT_ENTER_WINDOW, self.validation_evaluasi)
        self.m_button4.Bind(wx.EVT_BUTTON, self.penilaian_evaluasi)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def openfile(self, event):
        path = self.m_filePicker2.GetPath()
        with open(path, 'r') as myfile:
            meta = myfile.read()
        self.m_textCtrl1.SetValue(meta)
        self.status == 0

    def process(self, event):
        meta = self.m_textCtrl1.GetValue()
        tingkat = self.m_comboBox2.GetValue()
        if tingkat == '10%':
            tingkat = 0.1
        elif tingkat == '20%':
            tingkat = 0.2
        elif tingkat == '30%':
            tingkat = 0.3
        elif tingkat == '40%':
            tingkat = 0.4
        else:
            tingkat = 0.5
        (term, tf_idf, tf_isf, kalimat, list_stopwords, clustering, paragraph, ringkasan) = peringkasan(meta, tingkat)
        self.list_kalimat_ringkasan = ringkasan
        self.list_kalimat = paragraph
        self.m_textCtrl112.SetValue(tf_idf)
        self.m_textCtrl1121.SetValue(str(list_stopwords))
        self.m_textCtrl11.SetValue(tf_isf)
        self.m_textCtrl14.SetValue(str(clustering))
        self.m_textCtrl111.SetValue(kalimat)
        self.m_panel2.Enable()
        self.m_textCtrl12.SetValue(meta)

        list = ''
        for i in range(0, len(self.list_kalimat_ringkasan)):
            if i == 0:
                list = 'o  ' + self.list_kalimat_ringkasan[i]
            else:
                list = list + '\no  ' + self.list_kalimat_ringkasan[i]

        self.m_textCtrl113.SetValue(list)

    def validation_evaluasi(self, event):
        if self.status == 0:
            print('evaluasi')
            self.status = 1
            self.arr_checkbox = []

            for i in range(0, len(self.list_kalimat)):
                self.arr_checkbox.append(wx.CheckBox(self.m_scrolledWindow5, wx.ID_ANY, self.list_kalimat[i], wx.DefaultPosition,
                                                wx.DefaultSize, 0))
                self.bSizer8.Add(self.arr_checkbox[i], 0, wx.ALL, 5)
                # self.m_scrolledWindow5.SetSizer(self.bSizer8)
            self.m_scrolledWindow5.SetSizer(self.bSizer8)
            self.m_scrolledWindow5.Layout()
            self.bSizer8.Fit(self.m_scrolledWindow5)
            self.bSizer6.Layout()

    def penilaian_evaluasi(self, event):
        list_kalimat_pakar = []
        for i in range(0, len(self.arr_checkbox)):
            if self.arr_checkbox[i].IsChecked():
                print(self.list_kalimat[i])
                list_kalimat_pakar.append(self.list_kalimat[i])

        isi_tp = []
        isi_fp = []
        isi_fn = []
        isi_tn = []

        # precission    = tp/(tp+fp)
        # recall        = tp(tp+fn)
        # accuracy      = tp+tn/(jumlah kalimat keseluruhan)
        print('kalimat pakar')
        print(list_kalimat_pakar)
        print('kalimat ringkasan')
        print(self.list_kalimat_ringkasan)

        for i in list_kalimat_pakar:
            if i in self.list_kalimat_ringkasan:
                isi_tp.append(i)
            else:
                isi_fn.append(i)

        for i in self.list_kalimat_ringkasan:
            if i not in list_kalimat_pakar:
                isi_fp.append(i)

        for i in self.list_kalimat:
            if i not in list_kalimat_pakar and i not in self.list_kalimat_ringkasan:
                isi_tn.append(i)

        tp = len(isi_tp)
        fp = len(isi_fp)
        fn = len(isi_fn)
        tn = len(isi_tn)
        print(tp)
        print(fp)
        print(tn)
        print(fn)
        total = tp+tn+fp+fn

        if tp == 0 and fp == 0:
            precission = 0
        else:
            precission = (tp / (tp + fp)) * 100

        if tp == 0 and fn == 0:
            recall = 0
        else:
            recall = (tp / (tp + fn)) * 100

        accuracy = ((tp+tn)/total) * 100

        self.m_textCtrl13.SetValue(str(precission))
        self.m_textCtrl131.SetValue(str(recall))
        self.m_textCtrl1311.SetValue(str(accuracy))

class MainApp(wx.App):
    def OnInit(self):
        mainFrame = MyFrame1(None)
        mainFrame.Show(True)
        return True


if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()
