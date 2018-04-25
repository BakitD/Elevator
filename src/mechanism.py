from elevator import Elevator
from interpreter import Interpreter


class Builder(object):
	def build_elevator(self):
		raise NotImplementedError()

	def build_interpreter(self):
		raise NotImplementedError()

	def create(self):
		raise NotImplementedError()


class Mechanism(object):
	def __init__(self, elevator, interpreter):
		self._elevator = elevator
		self._interpreter = interpreter

	@property
	def elevator(self):
		return self._elevator

	@property
	def interpreter(self):
		return self._interpreter

	def launch(self):
		pass


class MechanismBuilder(Builder):

	def build_elevator(self, floors, height, speed, wait_time):
		return Elevator(floors, height, speed, wait_time)

	def build_interpreter(self):
		return Interpreter()

	def create(self, elevator_args):
		return Mechanism(self.build_elevator(*elevator_args), self.build_interpreter())