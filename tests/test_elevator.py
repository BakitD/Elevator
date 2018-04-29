import unittest


from src.elevator import Elevator, States


class ElevatorTestCase(unittest.TestCase):


	def setUp(self):
		self.height = 3
		self.floors = 15
		self.wait_time = 120.0
		self.speed = 1.5
		self.elevator = Elevator(self.floors,
						self.height,
						self.speed,
						self.wait_time
		)


	def test_initial_state(self):
		e = self.elevator
		self.assertEqual(e.height, self.height)
		self.assertEqual(e.floors, self.floors)
		self.assertEqual(e.wait_time, self.wait_time)
		self.assertEqual(e.speed, self.speed)
		self.assertEqual(e.state, States.closed)
		self.assertEqual(e._floor, 0)


	def test_possible_floors(self):
		self.assertEqual((0, self.floors), self.elevator.possible_floors())


	def test_change_state_to_incorrect(self):
		e = self.elevator
		self.assertEqual(e.state, States.closed)

		e.state = 'Incorrect state type or value'
		self.assertEqual(e.state, States.closed)

		e.state = 2
		self.assertEqual(e.state, States.closed)
		e.state = 3
		self.assertEqual(e.state, States.closed)

		e.state = str()
		self.assertEqual(e.state, States.closed)


	def test_change_state_to_correct(self):
		e = self.elevator

		e.state = States.closed
		self.assertEqual(e.state, States.closed)

		e.state = States.opened
		self.assertEqual(e.state, States.opened)

		e.state = States.passing
		self.assertEqual(e.state, States.passing)

		e.state = States.closed
		self.assertEqual(e.state, States.closed)


	def test_properties_change(self):
		e = self.elevator

		with self.assertRaises(AttributeError):
			e.floors = []
