import unittest


from src.app import Application
from src.elevator import Elevator
from src.parser import Parser


class TestApplication(unittest.TestCase):

	def setUp(self):
		self.elevator = Elevator(15, 2, 5, 2)
		self.parser = Parser()
		self.app = Application(self.elevator, self.parser)

	def test_properties_change(self):
		with self.assertRaises(AttributeError):
			self.app.elevator = None
		with self.assertRaises(AttributeError):
			self.app.parser = None

	def test_properties_getter(self):
		self.assertEqual(self.app.elevator, self.elevator)
		self.assertEqual(self.app.parser, self.parser)