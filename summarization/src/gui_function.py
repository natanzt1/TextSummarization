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