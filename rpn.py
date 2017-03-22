#!/usr/bin/env python3

import operator
import readline
from termcolor import colored

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'<': operator.lt,
	'>': operator.gt,
}

OP_COLORS = {
	'+': 'green',
	'-': 'cyan',
	'*': 'magenta',
	'/': 'yellow',
	'^': 'blue',
	'<': 'white',
	'>': 'white',
}

def printResult(result):
	if result < 0:
		return colored(str(result), 'red')
	
	return colored(str(result), 'cyan')

def calculate(arg, ls):
	stack = list()
	if isinstance(stack, list):
		pass
	else:
		print('a')
		print('b')
		print('c')
		print('d')
		print('e')
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			stack.append(result)
			ls.append(arg1)
			ls.append(arg2)
			ls.append(operand)
	return stack.pop()

def main():
	while True:
		ls = []
		result = calculate(input('rpn calc> ' ), ls)
		print(str(ls[0]) + ' ' + colored(str(ls[2]), OP_COLORS[str(ls[2])]) + ' ' + str(ls[1]) + ' ' + colored('=', 'blue') + ' ' + printResult(result)) 

if __name__ == '__main__':
	main()
