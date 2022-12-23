monkeyjob = open('input.txt').read().strip().split('\n')


# create a dictionary of the monkeyjob
monkeys = {}
for line in monkeyjob:
	key = line.split(':')[0].strip()
	value = line.split(':')[1].strip()
	try:
		value = int(value)
		monkeys[key] = value
	except:
		operation = value.split(' ')
		monkeys[key] = operation


startmonkey = 'root'


def monkeywork(monkey):
	if type(monkeys[monkey]) == int:
		return monkeys[monkey]
	else:
		operation = monkeys[monkey]
		match operation[1]:
			case '+':
				return monkeywork(operation[0]) + monkeywork(operation[2])
			case '-':
				return monkeywork(operation[0]) - monkeywork(operation[2])
			case '*':
				return monkeywork(operation[0]) * monkeywork(operation[2])
			case '/':
				return monkeywork(operation[0]) / monkeywork(operation[2])
			case '=':
				return monkeywork(operation[0]) == monkeywork(operation[2])


# part 1
print(f'The monkey named root will yell: {int(monkeywork(startmonkey))}.')

# part 2

monkeys[startmonkey][1] = '='


# create a tree for which monkyes are dependent on which other monkeys
def monkeytree(monkey):
	if type(monkeys[monkey]) == int:
		return [monkey]
	else:
		othermonkeys = monkeys[monkey]
		# print(othermonkeys)
		return [monkey] + monkeytree(othermonkeys[0]) + monkeytree(othermonkeys[2])


monkey1 = monkeys[startmonkey][0]
monkey2 = monkeys[startmonkey][2]
value = 0

if 'humn' in monkeytree(monkey1):
	value = monkeywork(monkey2)
	workingmonkey = monkey1
elif 'humn' in monkeytree(monkey2):
	value = monkeywork(monkey1)
	workingmonkey = monkey2


def find_human_value(value, wmonkey):
	if wmonkey == 'humn':
			return int(value)
	else:
		operation = monkeys[wmonkey]
		if 'humn' in monkeytree(operation[0]):
			tval = monkeywork(operation[2])
			wmonkey = operation[0]

			match operation[1]:
				case '+':
					value -= tval
				case '-':
					value += tval
				case '*':
					value /= tval
				case '/':
					value *= tval

		elif 'humn' in monkeytree(operation[2]):
			tval = monkeywork(operation[0])
			wmonkey = operation[2]

			match operation[1]:
				case '+':
					value -= tval
				case '-':
					value = tval - value
				case '*':
					value /= tval
				case '/':
					value = tval / value

		return find_human_value(int(value), wmonkey)


monkeys['humn'] = find_human_value(value, workingmonkey)
answer = monkeys['humn']
print(f'The number I yell to pass root\'s equality test: {answer}.')
print(f'The test is pased: {monkeywork(startmonkey)}.')
