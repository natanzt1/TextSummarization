import wx
import wx.xrc
import wx.grid
from summarization_function import *

###########################################################################
## Class MyFrame2
###########################################################################

class frameMain(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1280, 750), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"label"), wx.VERTICAL)

        self.m_staticText9 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Judul", wx.DefaultPosition,wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        sbSizer2.Add(self.m_staticText9, 0, wx.ALL, 5)

        self.corpus_text = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,wx.Size(1250, 30), wx.TE_MULTILINE)
        sbSizer2.Add(self.corpus_text, 0, wx.ALL, 5)

        self.m_staticText91 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Text", wx.DefaultPosition,wx.DefaultSize, 0)
        self.m_staticText91.Wrap(-1)
        sbSizer2.Add(self.m_staticText91, 0, wx.ALL, 5)

        self.corpus_text1 = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(1250, 100), wx.TE_MULTILINE)
        sbSizer2.Add(self.corpus_text1, 0, wx.ALL, 5)

        self.m_button4 = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer2.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_staticText911 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Hasil Rangkuman", wx.DefaultPosition,wx.DefaultSize, 0)
        self.m_staticText911.Wrap(-1)
        sbSizer2.Add(self.m_staticText911, 0, wx.ALL, 5)

        self.corpus_text2 = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(1250, 100), wx.TE_MULTILINE)
        sbSizer2.Add(self.corpus_text2, 0, wx.ALL, 5)

        bSizer5.Add(sbSizer2, 1, wx.EXPAND, 5)


        self.m_staticText912 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Perhitungan Fuzzy",
                                             wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText912.Wrap(-1)
        sbSizer2.Add(self.m_staticText912, 0, wx.ALL, 5)

        self.m_grid2 = wx.grid.Grid(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid2.CreateGrid(5, 5)
        self.m_grid2.EnableEditing(True)
        self.m_grid2.EnableGridLines(True)
        self.m_grid2.EnableDragGridSize(False)
        self.m_grid2.SetMargins(0, 0)

        # Columns
        self.m_grid2.EnableDragColMove(False)
        self.m_grid2.EnableDragColSize(True)
        self.m_grid2.SetColLabelValue(0, u"Himpunan Fuzzy Input")
        self.m_grid2.SetColLabelValue(1, u"Domain Fuzzy Input")
        self.m_grid2.SetColLabelValue(3, u"Himpunan Fuzzy Output")
        self.m_grid2.SetColLabelValue(4, u"Domain Fuzzy Output")
        self.m_grid2.SetColLabelSize(30)
        self.m_grid2.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid2.EnableDragRowSize(True)
        self.m_grid2.SetRowLabelSize(80)
        self.m_grid2.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        self.m_grid2.SetColSize(0, 150)
        self.m_grid2.SetColSize(1, 200)
        self.m_grid2.SetColSize(3, 150)
        self.m_grid2.SetColSize(4, 200)
        self.m_grid2.SetCellValue(0, 0, "Sangat Rendah")
        self.m_grid2.SetCellValue(1, 0, "Rendah")
        self.m_grid2.SetCellValue(2, 0, "Sedang")
        self.m_grid2.SetCellValue(3, 0, "Tinggi")
        self.m_grid2.SetCellValue(4, 0, "Sangat Tinggi")
        self.m_grid2.SetCellValue(0, 1, "0-0.225")
        self.m_grid2.SetCellValue(1, 1, "0.1-0.45")
        self.m_grid2.SetCellValue(2, 1, "0.325-0.675")
        self.m_grid2.SetCellValue(3, 1, "0.55-0.9")
        self.m_grid2.SetCellValue(4, 1, "0.775-1")
        self.m_grid2.SetCellValue(0, 3, "Tidak Penting")
        self.m_grid2.SetCellValue(1, 3, "Sedang")
        self.m_grid2.SetCellValue(2, 3, "Penting")
        self.m_grid2.SetCellValue(0, 4, "0-0.4")
        self.m_grid2.SetCellValue(1, 4, "0.1-0.9")
        self.m_grid2.SetCellValue(2, 4, "0.6-1")

        # Label Appearance

        # Cell Defaults
        self.m_grid2.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        sbSizer2.Add(self.m_grid2, 0, wx.ALL, 5)




        self.m_grid1 = wx.grid.Grid(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid1.CreateGrid(100, 8)
        self.m_grid1.EnableEditing(True)
        self.m_grid1.EnableGridLines(True)
        self.m_grid1.EnableDragGridSize(False)
        self.m_grid1.SetMargins(0, 0)

        # Columns
        self.m_grid1.SetColSize(0, 460)
        self.m_grid1.SetColSize(1, 130)
        self.m_grid1.SetColSize(2, 130)
        self.m_grid1.SetColSize(3, 130)
        self.m_grid1.SetColSize(4, 130)
        self.m_grid1.SetColSize(5, 130)
        self.m_grid1.SetColSize(6, 130)
        self.m_grid1.SetColSize(7, 80)
        self.m_grid1.EnableDragColMove(False)
        self.m_grid1.EnableDragColSize(True)
        self.m_grid1.SetColLabelSize(30)
        self.m_grid1.SetColLabelValue(0, u"Kalimat")
        self.m_grid1.SetColLabelValue(1, u"Fitur 1")
        self.m_grid1.SetColLabelValue(2, u"Fitur 2")
        self.m_grid1.SetColLabelValue(3, u"Fitur 3")
        self.m_grid1.SetColLabelValue(4, u"Fitur 4")
        self.m_grid1.SetColLabelValue(5, u"Fitur 5")
        self.m_grid1.SetColLabelValue(6, u"Fitur 6")
        self.m_grid1.SetColLabelValue(7, u"Fuzzy Output")
        self.m_grid1.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid1.EnableDragRowSize(True)
        self.m_grid1.SetRowLabelSize(80)
        self.m_grid1.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellFont(wx.Font(8, 70, 90, 90, False, wx.EmptyString))
        self.m_grid1.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        sbSizer2.Add(self.m_grid1, 0, wx.ALL, 5)

        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button4.Bind(wx.EVT_BUTTON, self.SUBMIT_FUNCTION)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def SUBMIT_FUNCTION(self, event):
        judul =self.corpus_text.Value
        meta = self.corpus_text1.Value
        all_split_kalimat = function_split_teks(meta)
        paragraph = all_split_kalimat[1]
        all_split_kalimat = all_split_kalimat[0]

        all_split_kalimat2 = function_split_teks_tanpa_type_no_lowercase(meta)
        paragraph2 = all_split_kalimat2[1]
        all_split_kalimat2 = all_split_kalimat2[0]

        kalimat_terpanjang = function_kalimat_terpanjang(all_split_kalimat)

        fitur1 = function_fitur1(judul, paragraph)
        # print (fitur1)
        result1 = function_fuzzy(fitur1)
        # print("Result1")
        # print(result1)

        fitur2 = function_fitur2(kalimat_terpanjang, all_split_kalimat)
        # print (fitur2)
        result2 = function_fuzzy(fitur2)
        # print("Result2")
        # print(result2)

        fitur3 = function_fitur3(paragraph)
        # print(fitur3)
        result3 = function_fuzzy(fitur3)
        # print("Result3")
        # print(result3)

        fitur4 = function_fitur4(paragraph)
        # print(fitur4)
        result4 = function_fuzzy(fitur4)
        print("Result4")
        print(result4)

        fitur5 = function_fitur5(meta)
        # print(fitur5)
        result5 = function_fuzzy(fitur5)
        # print("Result5")
        # print(fitur5)

        fitur6 = function_fitur6(meta)
        # print(fitur6)
        result6 = function_fuzzy(fitur6)
        # print("Result6")
        # print(result6)

        fuzzy_output = function_fuzzy_output(result1, result2, result3, result4, result5, result6)
        print(fuzzy_output)
        result = function_rule_fuzzy(result1, result2, result3, result4, result5, result6)
        index1 = result[0]
        index2 = result[1]

        i = 0
        self.m_grid1.ClearGrid()
        for x in range(0, len(paragraph)):
            for y in range(0, len(paragraph[x])):
                hasil = function_convert(result1[x][y])
                hasil2 = function_convert(result2[x][y])
                hasil3 = function_convert(result3[x][y])
                hasil4 = function_convert(result4[x][y])
                hasil5 = function_convert(result5[x][y])
                hasil6 = function_convert(result6[x][y])
                self.m_grid1.SetCellValue(i, 0, paragraph[x][y])
                self.m_grid1.SetCellValue(i, 1, "%s (%f)" %(hasil, fitur1[x][y]))
                self.m_grid1.SetCellValue(i, 2, "%s (%f)" %(hasil2, fitur2[x][y]))
                self.m_grid1.SetCellValue(i, 3, "%s (%f)" %(hasil3, fitur3[x][y]))
                self.m_grid1.SetCellValue(i, 4, "%s (%f)" %(hasil4, fitur4[x][y]))
                self.m_grid1.SetCellValue(i, 5, "%s (%f)" %(hasil5, fitur5[x][y]))
                self.m_grid1.SetCellValue(i, 6, "%s (%f)" %(hasil6, fitur6[x][y]))
                self.m_grid1.SetCellValue(i, 7, fuzzy_output[x][y])
                i += 1


        self.m_grid1.Update()

        kesimpulan = ''
        for x in range(0, len(index1)):
            a = index1[x]
            b = index2[x]
            if x == 0:
                kesimpulan = paragraph[a][b]
            else:
                kesimpulan = kesimpulan+'. '+paragraph[a][b]
        self.corpus_text2.SetValue(kesimpulan)


class MainApp(wx.App):
 def OnInit(self):
  mainFrame = frameMain(None)
  mainFrame.Show(True)
  return True


if __name__ == '__main__':
 app = MainApp()
 app.MainLoop()


