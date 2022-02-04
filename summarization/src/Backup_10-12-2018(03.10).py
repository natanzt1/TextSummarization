from nltk.corpus import stopwords
import math
import wx
import wx.xrc
from summarization_function import *

# filename = "tf_idf.txt"
# with open(filename, 'r') as myfile:
#     meta = myfile.read()

# meta = meta.lower()
# data = meta.split('\n\n')
# paragraph = []
# sentence = []
# jml_paragraph = len(data)
# tf_idf_all = []
#
# # Split Kalimat dan paragraf ====================
# for x in range(0, jml_paragraph):
#     paragraph.append([x, data[x].split('. ')])
#
# # ===============================================
# bobot_all = []
# bobot_kesimpulan_all = []
# kalimat_rank_all = []
# kesimpulan_all = []
# test2 = []
# tf_all = []
# df = []
# df_all = []
# tf_idf_kalimat2 = {}
# # TF ==================================================================================================================================================
# # test berisi teks dari paragraf pertama, bila ingin ambil teks paragraf ke-x, gunakan paragraph[x][1]
# for jml_para in range(0, len(paragraph)):
#     test = paragraph[jml_para][1]
#     bobot = []
#     kalimat_rank = []
#     # Me-rebuild paragraf ke-x dari array kalimat
#     jml_kalimat = len(paragraph[jml_para][1])
#     teks = ''
#     for x in range(0,jml_kalimat):
#         teks = teks+paragraph[jml_para][1][x]+'. '
#
#     # Type dijalankan pada paragraf pertama saja dulu
#     words = function_tokenization(teks)
#     type = function_type(teks, words)
#     type_freq = function_type_freq(type, words)
#
#     # menghitung type di tiap paragraf
#     for k in range(len(type)):
#         type_freq.append(0)
#
#     type_paragraph = []
#
#     i = 0
#     for x in paragraph[jml_para][1]:
#         type_paragraph.append([])
#         for a_type in type:
#             count = 0
#             words = function_tokenization(x)
#             for word in words:
#                 if a_type == word:
#                     count = count+1
#
#             # Frequency tiap term dicatat setelah looping ketiga berhenti
#             # Looping ketiga adalah looping untuk membandingkan term dengan setiap kata pada kalimat
#             type_paragraph[i].append(count)
#         i = i + 1
#     tf_all.append([jml_para, type_paragraph])
#
#     df = []
#     for a_type in type:
#         df_count = 0
#         for x in paragraph[jml_para][1]:
#             words = function_tokenization(x)
#             if a_type in words:
#                 df_count = df_count + 1
#         df.append(df_count)
#     print("--------------------PARAGRAPH %d---------------------"%(jml_para+1))
#     print("========================type========================")
#     print(type)
#     print("========================df========================")
#     print(df)
#     print("========================tf========================")
#     for x in range(jml_kalimat):
#         print(type_paragraph[x])
#     df_all.append(df)
#
#     jml_term = len(tf_all[jml_para][1][0])
#     N = jml_kalimat
#
#     limit = 0
#     print("===================HITUNG TF-IDF====================")
#     for counter in range(0, jml_kalimat):
#         tf_idf_kalimat = 0
#         for counter2 in range(0, jml_term):
#             df = df_all[jml_para][counter2]
#             tf_idf = tf_all[jml_para][1][counter][counter2]*math.log10(N/df)
#             tf_idf_kalimat = tf_idf_kalimat+tf_idf
#         # print("TF IDF")
#         # print(tf_idf_kalimat)
#         bobot.append(tf_idf_kalimat)
#         kalimat_rank.append(paragraph[jml_para][1][counter])
#         tf_idf_kalimat2[paragraph[jml_para][1][counter]] = tf_idf_kalimat
#
#     for x in range(0, len(bobot)):
#         for y in range(x+1, len(bobot)):
#             if bobot[x] < bobot[y]:
#                 sample = bobot[x]
#                 bobot[x] = bobot[y]
#                 bobot[y] = sample
#                 sample_kalimat = kalimat_rank[x]
#                 kalimat_rank[x] = kalimat_rank[y]
#                 kalimat_rank[y] = sample_kalimat
#
#         # tf_idf_kalimat2[] = tf_idf_kalimat
#         # if limit < jml_kesimpulan:
#         #     tf_idf_kalimat2.append(tf_idf_kalimat)
#         # else:
#         #     for counter3 in range(0,jml_kesimpulan):
#         #         if
#
#         # if tf_idf_kalimat2 < tf_idf_kalimat:
#         #     tf_idf_kalimat2 = tf_idf_kalimat
#         #     kesimpulan.append(paragraph[jml_para][1][counter])
#         # print("tf_idf = %f" % tf_idf_kalimat2[counter])
#     bobot_all.append(bobot)
#     kalimat_rank_all.append(kalimat_rank)
#     jml_kesimpulan = N / 2
#     jml_kesimpulan = round(jml_kesimpulan)
#     if jml_kesimpulan == 0:
#         jml_kesimpulan = 1
#
#     kesimpulan_counter = 0
#     kesimpulan = []
#     bobot_kesimpulan = []
#     for x in range(0, jml_kesimpulan):
#         kesimpulan.append(kalimat_rank[x])
#         bobot_kesimpulan.append(bobot[x])
#     kesimpulan_all.append(kesimpulan)
#     bobot_kesimpulan_all.append(bobot_kesimpulan)
#     print("--------------------PARAGRAPH %d--------------------" %(jml_para+1))
#     print("\n\n")
#     # =====================================================================================================================================================
# print(bobot_kesimpulan_all[0])
# print(kesimpulan_all[0])
# print(bobot_all[0])

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
## Class MyFrame2
###########################################################################

class frameMain(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(779, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"label"), wx.VERTICAL)

        self.m_staticText9 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Corpus", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        sbSizer2.Add(self.m_staticText9, 0, wx.ALL, 5)

        self.corpus_text = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.Size(725, 150), wx.TE_MULTILINE)
        sbSizer2.Add(self.corpus_text, 0, wx.ALL, 5)

        self.m_button4 = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer2.Add(self.m_button4, 0, wx.ALL, 5)

        gSizer4 = wx.GridSizer(0, 2, 0, 0)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Perangkingan", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer6.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.perangkingan_text = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.Size(350, 180), wx.TE_MULTILINE)
        bSizer6.Add(self.perangkingan_text, 0, wx.ALL, 5)

        gSizer4.Add(bSizer6, 1, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText6 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Kesimpulan", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer8.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.kesimpulan_text = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.Size(350, 180), wx.TE_MULTILINE)
        bSizer8.Add(self.kesimpulan_text, 0, wx.ALL, 5)

        gSizer4.Add(bSizer8, 1, wx.EXPAND, 5)

        sbSizer2.Add(gSizer4, 1, wx.EXPAND, 5)

        bSizer5.Add(sbSizer2, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button4.Bind(wx.EVT_BUTTON, self.SUBMIT_FUNCTION)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def SUBMIT_FUNCTION(self, event):
        meta = self.corpus_text.Value
        meta = meta.lower()
        data = meta.split('\n\n')
        paragraph = []
        sentence = []
        jml_paragraph = len(data)
        tf_idf_all = []

        # Split Kalimat dan paragraf ====================
        for x in range(0, jml_paragraph):
            paragraph.append([x, data[x].split('. ')])

        # ===============================================
        bobot_all = []
        bobot_kesimpulan_all = []
        kalimat_rank_all = []
        kesimpulan_all = []
        test2 = []
        tf_all = []
        df = []
        df_all = []
        tf_idf_kalimat2 = {}
        # TF ==================================================================================================================================================
        # test berisi teks dari paragraf pertama, bila ingin ambil teks paragraf ke-x, gunakan paragraph[x][1]
        for jml_para in range(0, len(paragraph)):
            test = paragraph[jml_para][1]
            bobot = []
            kalimat_rank = []
            # Me-rebuild paragraf ke-x dari array kalimat
            jml_kalimat = len(paragraph[jml_para][1])
            teks = ''
            for x in range(0,jml_kalimat):
                teks = teks+paragraph[jml_para][1][x]+'. '

            # Type dijalankan pada paragraf pertama saja dulu
            words = function_tokenization(teks)
            type = function_type(teks, words)
            type_freq = function_type_freq(type, words)

            # menghitung type di tiap paragraf
            for k in range(len(type)):
                type_freq.append(0)

            type_paragraph = []



            i = 0
            for x in paragraph[jml_para][1]:
                type_paragraph.append([])
                for a_type in type:
                    count = 0
                    words = function_tokenization(x)
                    for word in words:
                        if a_type == word:
                            count = count+1

                    # Frequency tiap term dicatat setelah looping ketiga berhenti
                    # Looping ketiga adalah looping untuk membandingkan term dengan setiap kata pada kalimat
                    type_paragraph[i].append(count)
                i = i + 1
            tf_all.append([jml_para, type_paragraph])



            df = []
            for a_type in type:
                df_count = 0
                for x in paragraph[jml_para][1]:
                    words = function_tokenization(x)
                    if a_type in words:
                        df_count = df_count + 1
                df.append(df_count)



            print("--------------------PARAGRAPH %d---------------------"%(jml_para+1))
            print("========================type========================")
            print(type)
            print("========================df========================")
            print(df)
            print("========================tf========================")
            for x in range(jml_kalimat):
                print(type_paragraph[x])
            df_all.append(df)

            jml_term = len(tf_all[jml_para][1][0])
            N = jml_kalimat

            limit = 0
            print("===================HITUNG TF-IDF====================")
            for counter in range(0, jml_kalimat):
                tf_idf_kalimat = 0
                for counter2 in range(0, jml_term):
                    df = df_all[jml_para][counter2]
                    tf_idf = tf_all[jml_para][1][counter][counter2]*math.log10(N/df)
                    tf_idf_kalimat = tf_idf_kalimat+tf_idf
                # print("TF IDF")
                # print(tf_idf_kalimat)
                bobot.append(tf_idf_kalimat)
                kalimat_rank.append(paragraph[jml_para][1][counter])
                tf_idf_kalimat2[paragraph[jml_para][1][counter]] = tf_idf_kalimat

            for x in range(0, len(bobot)):
                for y in range(x+1, len(bobot)):
                    if bobot[x] < bobot[y]:
                        sample = bobot[x]
                        bobot[x] = bobot[y]
                        bobot[y] = sample
                        sample_kalimat = kalimat_rank[x]
                        kalimat_rank[x] = kalimat_rank[y]
                        kalimat_rank[y] = sample_kalimat

                # tf_idf_kalimat2[] = tf_idf_kalimat
                # if limit < jml_kesimpulan:
                #     tf_idf_kalimat2.append(tf_idf_kalimat)
                # else:
                #     for counter3 in range(0,jml_kesimpulan):
                #         if

                # if tf_idf_kalimat2 < tf_idf_kalimat:
                #     tf_idf_kalimat2 = tf_idf_kalimat
                #     kesimpulan.append(paragraph[jml_para][1][counter])
                # print("tf_idf = %f" % tf_idf_kalimat2[counter])
            bobot_all.append(bobot)
            kalimat_rank_all.append(kalimat_rank)
            jml_kesimpulan = N / 2
            jml_kesimpulan = round(jml_kesimpulan)
            if jml_kesimpulan == 0:
                jml_kesimpulan = 1

            kesimpulan_counter = 0
            kesimpulan = []
            bobot_kesimpulan = []
            for x in range(0, jml_kesimpulan):
                kesimpulan.append(kalimat_rank[x])
                bobot_kesimpulan.append(bobot[x])
            kesimpulan_all.append(kesimpulan)
            bobot_kesimpulan_all.append(bobot_kesimpulan)
            print("--------------------PARAGRAPH %d--------------------" %(jml_para+1))
            print("\n\n")
            # =====================================================================================================================================================
        kesimpulan_result = []
        perangkingan_result = []
        perangkingan_value = "========================================"
        for x in range(0, len(bobot_all)):
            perangkingan_value = perangkingan_value + "\n\nPARAGRAPH %d" % (x + 1)
            for y in range(0, len(bobot_all[x])):
                perangkingan_value = perangkingan_value + "\n" + kalimat_rank_all[x][y] + " : %f\n" % bobot_all[x][y]
                perangkingan_result.append([kalimat_rank_all[x][y], bobot_all[x][y]])
            perangkingan_value = perangkingan_value+"========================================"
        kesimpulan_value = "========================================"
        for x in range(0, len(bobot_kesimpulan_all)):
            kesimpulan_value = kesimpulan_value+"\n\nPARAGRAPH %d" % (x+1)
            for y in range(0, len(bobot_kesimpulan_all[x])):
                kesimpulan_value = kesimpulan_value+"\n"+kesimpulan_all[x][y]+" : %f\n"%bobot_kesimpulan_all[x][y]
                kesimpulan_result.append([kesimpulan_all[x][y], bobot_kesimpulan_all[x][y]])
            kesimpulan_value = kesimpulan_value + "========================================"

        self.perangkingan_text.SetValue(perangkingan_value)
        self.kesimpulan_text.SetValue(kesimpulan_value)

class MainApp(wx.App):
 def OnInit(self):
  mainFrame = frameMain(None)
  mainFrame.Show(True)
  return True


if __name__ == '__main__':
 app = MainApp()
 app.MainLoop()


