'''
Travis Campos
09/21/2019

Stock Market Calculator
'''


# Template Class

class UserInterface:
	def __init__(self, interface):
		self.interface = interface

	def print_interface(self):
		print(self.interface)

interface = UserInterface("SampleInterface")
interface.print_interface()



# Template List

interface_list = [ "interface_1", "interface_2", "interface_3" ]

for element in interface_list:
	print(element)






