import wx
import random

class GUI(wx.Frame, wx.Panel):

	def __init__(self, parent):

		# wx.Frame.__init__(self, parent, size = (500, 500),
		#	style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
		wx.Frame.__init__(self, None, wx.ID_ANY, "Title")
		self.initFrame()
		self.initPanel()

	def initFrame(self):

		# self.statusbar = self.CreateStatusBar()
		# self.statusbar.SetStatusText('0')
		# self.board = Board(self)
		# self.bard.SetFocus()
		# self.board.start()

		# self.SetTitle("Title")
		self.SetIcon(wx.Icon("resources/icons/myIcon.ico", wx.BITMAP_TYPE_ICO))
		self.Centre()

	def initPanel(self):

		self.panel = wx.Panel(self, wx.ID_ANY)

def main():

	app = wx.App()
	gui = GUI(None)
	gui.Show()
	app.MainLoop()

if __name__ == "__main__":
	main()