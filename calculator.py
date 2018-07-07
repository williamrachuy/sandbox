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

		self.textbox = wx.TextCtrl(self, style = wx.TE_RIGHT)
		box.Add(self.textbox, flag = wx.EXPAND | wx.TOP | wx.BOTTOM, border = 4)

		grid = wx.GridSizer(5, 4, 2, 2)

		buttons = [
			'7', '8', '9', '/',
			'4', '5', '6', '*',
			'1', '2', '3', '-',
			'0', '.', 'C', '+',
			'='
		]

		self.clearFlag = False

		for label in buttons:
			button = wx.Button(self, -1, label)
			grid.Add(button, 0, wx.EXPAND)
			self.Bind(wx.EVT_BUTTON, self.on_button_press, button)

		box.Add(grid, proportion = 1, flag = wx.EXPAND)

		self.SetSizer(box)

	def on_button_press(self, event):

		# Get label of button
		label = event.GetEventObject().GetLabel()
		print("Label: " + label)

		# Get the input from the TextCtrl
		calculation = self.textbox.GetValue()

		# Handle the event based on the button pressed
		if label == '=': # Calculate the result of the input in the TextCtrl

			self.clearFlag = True			

			# Ignore an empty calculation
			if not calculation:
				return

			try:
				# Calculate the result
				result = float(eval(calculation))
			except SyntaxError as err: # Catch any input errors
				wx.LogError("Invalid syntax({}). Please check your input and try again.".format(calculation))
				return
			except NameError as err: # Catch any manually typed errors
				wx.LogError("There was an error. Plase check your input and try again.")
				return

			# Show the result
			self.textbox.SetValue(str(result))

		elif label == 'C': # Clear the TextCtrl
			self.textbox.SetValue('')
			self.clearFlag = False

		elif self.clearFlag == True and label.isdigit() == True:
			self.textbox.SetValue(label)
			self.clearFlag = False

		else: # 0-9 (and .)
			# Add the label of the button press on the current calculation in the TextCtrl
			self.textbox.SetValue(calculation + label)
			self.clearFlag = False

if __name__ == "__main__":
	
	app = wx.App()
	gui = Interface(None, title = "Calculator")
	gui.Show()
	app.MainLoop()