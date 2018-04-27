import unittest


from src.parser import Parser, Action


class TestParser(unittest.TestCase):

	def setUp(self):
		self.parser = Parser()

	def test_correct_commands(self):
		self.assertEqual(
				(Action.call, '100500'),
				self.parser.parse('call 100500')
		)

		self.assertEqual(
				(Action.go, '21'),
				self.parser.parse('go 21')
		)

	def test_correct_incorrect(self):
		commands = (
			'call  100', ' call100', ' call 100 ', 'call 100 ',
			'call a', 'call', 'c', '100', 'call 999a', 'call -1', 'call',
			'go  100', ' go100', ' go 100 ', 'go 100 ',
			'go a', 'go', 'c', '100', 'go 99 go9a', 'go -1', 'go'
			'call go', 'go call', '', '1', '100500'
			)

		for cmd in commands:
			self.assertEqual((None, None), self.parser.parse(cmd))
