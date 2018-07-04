'''
https://letscodepython.com/blog/2017/12/27/building-guis-wxpython/
'''

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
		self.textbox = wx.TextCtrl(self, style = wx.TE_RIGHT | wx.WANTS_CHARS)
		box.Add(self.textbox, flag = wx.EXPAND | wx.TOP | wx.BOTTOM, border = 4)

		grid = wx.GridSizer(5, 4, 2, 2)

		buttons = [
			'7', '8', '9', '/',
			'4', '5', '6', '*',
			'1', '2', '3', '-',
			'0', '.', 'C', '+',
			'='
		]

		for label in buttons:
			button = wx.Button(self, -1, label)
			grid.Add(button, 0, wx.EXPAND)
			self.Bind(wx.EVT_BUTTON, self.on_button_press, button)

		self.Bind(wx.EVT_KEY_UP, self.on_key_press)

		box.Add(grid, proportion = 1, flag = wx.EXPAND)
		self.SetSizer(box)

	def on_button_press(self, event):
		# Get label of button
		label = event.GetEventObject().GetLabel()

		# Get the input from the TextCtrl
		calculation = self.textbox.GetValue()

		# Handle the event based on the button pressed
		if label == '=': # Calculate the result of the input in the TextCtrl
			# Ignore an empty calculation
			if not calculation:
				return

			result = eval(calculation)

			# Show the result
			self.textbox.SetValue(str(result))
		elif label == 'C': # Clear the TextCtrl
			self.textbox.SetValue('')
		else: # 0-9 (and .)
			# Add the label of the button press on the current calculation in the TextCtrl
			self.textbox.SetValue(calculation + label)

	def on_key_press(self, event):
		print("Detected key press and release")

if __name__ == "__main__":
	app = wx.App()
	gui = Interface(None, title = "Calculator")
	gui.Show()
	app.MainLoop()