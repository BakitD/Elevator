import os


from mechanism import MechanismBuilder
from parser import Parser


def main(*args, **kwargs):
	cmd_args = Parser()
	mechanism = MechanismBuilder().create(cmd_args.parse())
	mechanism.launch()


if __name__ == '__main__':
	main()