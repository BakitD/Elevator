import time


from cmdparser import Action
from elevator import States


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

	def _wait(self, seconds):
		time.sleep(seconds)

	def _destination(self, target_floor):
		if target_floor == self._elevator.floor:
			return target_floor, target_floor, 0
		return self._elevator.floor, target_floor, 1 if target_floor > self._elevator.floor else -1

	def _opening_closing(self):
		if self._elevator.state == States.passing:
			return
		if self._elevator.state == States.opened:
			print('Elevator reopened doors on the {} floor'.format(self._elevator.floor))
		elif self._elevator.state == States.closed:
			print('Elevator opened doors on the {} floor'.format(self._elevator.floor))
		counter = self._elevator.wait_time
		self._elevator.state = States.opened
		while counter > 0:
			self._wait(1)
			print('Waiting with opened doors !')
			counter -= 1
		print('Doors are closed !')
		self._elevator.state = States.closed

	def _handle_call(self, target_floor):
		current, end, inc = self._destination(target_floor)
		if inc == 0:
			self._opening_closing()
		else:
			print('Elevator started from {} floor'.format(current))
			span = abs(current - end)
			sleep_time = self._elevator.destination_time(span) / span
			self._elevator.state = States.passing
			current += inc
			while current != end:
				self._wait(sleep_time)
				print('Elevator passes {} floor'.format(current))
				current += inc
			self._wait(sleep_time)
			print('Elevator arrived on the {} floor'.format(end))
			self._elevator.state = States.closed
			self._elevator.floor = end
			self._opening_closing()

	def run(self):
		_, top = self._elevator.possible_floors()
		while True:
			command, value = self._parser.parse(input('>> '))
			if value and value > top:
				print('Top floor is {}'.format(top))
			elif command in (Action.call, Action.go):
				self._handle_call(value)
			else:
				print('Incorrect command was given')
