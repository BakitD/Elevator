import os


from argparser import ArgParser
from app import Application
from elevator import Elevator
from cmdparser import Parser


def main():
	args = ArgParser()
	
	app = Application(Elevator(*args.parse()), Parser())
	app.run()


if __name__ == '__main__':
	main()