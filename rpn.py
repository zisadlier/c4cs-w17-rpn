#!/usr/bin/env python3

import operator

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'<': operator.lt,
	'>': operator.gt,
}

def calculate(arg):
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
	return stack.pop()

def main():
	while True:
		result = calculate(input('rpn calc> ' ))
		print("Result:", result)

if __name__ == '__main__':
	main()
