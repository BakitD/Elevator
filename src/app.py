

class Application(object):
	def __init__(self, elevator, parser):
		self._elevator = elevator
		self._parser = parser

	@property
	def elevator(self):
		return self._elevator

	@property
	def parser(self):
		return self._parser

	def run(self):
		flag = True
		while flag:
			command, value = self._parser.parse(input())
			print(command, value)
