import time


from enum import Enum


class States(Enum):
	closed = 'Doors are closed'
	opened = 'Doors are opened'
	passing = 'Elevator is passing by'


class Elevator(object):

	state = property()
	floor = property()

	def __init__(self, floors, height, speed, wait_time):
		self.height = height
		self.speed = speed
		self.wait_time = wait_time

		self._floors = floors
		self._state = States.closed
		self._floor = 0

	@state.getter
	def state(self):
		return self._state

	@state.setter
	def state(self, state):
		if state in (States.closed, States.opened, States.passing):
			self._state = state
		return self._state

	@property
	def floors(self):
		return self._floors

	@floor.getter
	def floor(self):
		return self._floor

	@floor.setter
	def floor(self, floor):
		if 0 <= floor <= self._floors:
			self._floor = floor
		return self._floor

	def possible_floors(self):
		return 0, self._floors

	def destination_time(self, floors):
		return (floors * self.height) / self.speed