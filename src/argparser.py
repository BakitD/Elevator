import argparse


FLOOR_MIN = 5
FLOOR_MAX = 20


class ArgParser(object):

	def check_floors(self, value):
		try:
			ivalue = int(value)
			if not FLOOR_MIN <= ivalue <= FLOOR_MAX:
				raise Exception
		except Exception:
			raise argparse.ArgumentTypeError("Number of floors should be integer between {} and {}".format(FLOOR_MIN, FLOOR_MAX))
		return ivalue

	def check_height(self, value):
		try:
			ivalue = float(value)
			if not ivalue > 0:
				raise Exception
		except Exception:
			raise argparse.ArgumentTypeError("Height should be positive float")
		return ivalue

	def check_speed(self, value):
		try:
			ivalue = float(value)
			if not ivalue > 0:
				raise Exception
		except Exception:
			raise argparse.ArgumentTypeError("Speed should be positive float")
		return ivalue

	def check_wait_time(self, value):
		try:
			ivalue = float(value)
			if not ivalue >= 1:
				raise Exception
		except Exception:
			raise argparse.ArgumentTypeError("Time between opening and closing door should be positive float")
		return ivalue


	def parse(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('-floors', action='store', dest='floors', type=self.check_floors,
							required=True, help='Number of floors (integer)')
		parser.add_argument('-height', action='store', dest='height', type=self.check_height,
							required=True, help='Distance between floors (float)')
		parser.add_argument('-speed', action='store', dest='speed', type=self.check_speed,
							required=True, help='Eelevator speed (float)')
		parser.add_argument('-wait_time', action='store', dest='wait_time', type=self.check_wait_time,
							required=True, help='Time between opening and closing doors (float)')
		args = parser.parse_args()
		return args.floors, args.height, args.speed, args.wait_time
