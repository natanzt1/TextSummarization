
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
