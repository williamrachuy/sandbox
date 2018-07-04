import wx

class Interface(wx.Frame):
	def __init__(self, parent, title):
		super(Interface, self).__init__(parent, title = title)
		try:
			self.SetIcon(wx.Icon("resources/icons/myIcon.ico", wx.BITMAP_TYPE_ICO))
		except Exception as e:
			print("Error importing icon at " + "resources/icons/myIcon.ico")
		self.setup()

	def setup(self):
		box = wx.BoxSizer(wx.VERTICAL)
		grid = wx.GridSizer(1, 4, 10, 10)

		grid.AddMany([
			(wx.Button(self, label = "+"), 0, wx.EXPAND),
			(wx.Button(self, label = "-"), 0, wx.EXPAND),
			(wx.Button(self, label = "*"), 0, wx.EXPAND),
			(wx.Button(self, label = "/"), 0, wx.EXPAND)
		])

		box.Add(grid, proportion = 1, flag = wx.EXPAND)
		self.SetSizer(box)

if __name__ == "__main__":
	app = wx.App()
	gui = Interface(None, title = "Calculator")
	gui.Show()
	app.MainLoop()