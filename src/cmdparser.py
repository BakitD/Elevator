import re


from enum import Enum


class Action(Enum):
	go = 'Go'
	call = 'Call'


class Parser(object):

	def __init__(self):
		self._re_go = re.compile("^go \d+$")
		self._re_call = re.compile("^call \d+$")

	def parse(self, input_str):
		input_str = str(input_str)
		matched = self._re_call.findall(input_str) or self._re_go.findall(input_str)
		if matched:
			cmd, value = matched.pop().split()
			return Action.go if cmd == 'go' else Action.call, int(value)
		return None, None