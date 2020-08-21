'''
Travis Campos
09/21/2019

Stock Market Calculator
'''


# Template Class

class WebData:
	def __init__(self, data):
		self.data = data

	def print_data(self):
		print(self.data)

data = WebData("SampleWebData")
data.print_data()



# Template List

web_list = [ "api_1", "api_2", "api_3" ]

for element in web_list:
	print(element)






