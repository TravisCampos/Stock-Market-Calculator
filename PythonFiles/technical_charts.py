'''
Travis Campos
09/21/2019

Stock Market Calculator
'''


# Template Class

class TechnicalChart:
	def __init__(self, chart):
		self.chart = chart

	def print_chart(self):
		print(self.chart)

chart = TechnicalChart("SampleChart")
chart.print_chart()



# Template List

chart_list = [ "chart_1", "chart_2", "chart_3" ]

for element in chart_list:
	print(element)






