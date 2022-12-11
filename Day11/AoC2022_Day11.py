import re
import math

with open('input.txt') as f:
	notes = f.read().split('\n\n')

# # Part 1
# RELIEF = 3

# Part 2
RELIEF = 1


class Monkey:
	def __init__(self, starting_items, operation, test, next_monkey_true, next_monkey_false):
		self.operation = operation
		self.test = test
		self.items = starting_items
		self.next_monkey = {True: next_monkey_true, False: next_monkey_false}

	def inspect(self):
		if type(self.operation[1]) == int:
			match self.operation[0]:
				case '*':
					self.items = [item*int(self.operation[1]) for item in self.items]
				case '+':
					self.items = [item+int(self.operation[1]) for item in self.items]
		else:
			match self.operation[0]:
				case '*':
					self.items = [item*item for item in self.items]
				case '+':
					self.items = [item+item for item in self.items]

	def test_items(self):
		self.items = [item//RELIEF for item in self.items]
		return zip([self.next_monkey[not item % self.test] for item in self.items], self.items)

	def __repr__(self):
		return f'items: {self.items}\noperation: {self.operation[0]}{self.operation[1]}\ntest: divisible by {self.test}\nnext monkeys: {self.next_monkey}\n'


monkeys = []

for note in notes:
	starting_items = [int(item) for item in re.findall(r'\d+', note.splitlines()[1])]
	op = re.findall(r'([+*])', note.splitlines()[2])[0]
	opval = re.findall(r'(\S+)', note.splitlines()[2])[-1]
	try:
		opval = int(opval)
	except ValueError:
		pass
	operation = [op, opval]
	test = int(re.findall(r'divisible by (\d+)', note)[0])
	next_monkey_true = int(re.findall(r'to monkey (\d)', note)[0])
	next_monkey_false = int(re.findall(r'to monkey (\d)', note)[1])
	monkey = Monkey(starting_items, operation, test, next_monkey_true, next_monkey_false)
	monkeys.append(monkey)

# Part 1
#
# inspections = [0]*len(monkeys)
#
# for i in range(20):
# 	for monkey in monkeys:
# 		if monkey.items:
# 			inspections[monkeys.index(monkey)] += len(monkey.items)
# 			monkey.inspect()
# 			nxt_mnkys = monkey.test_items()
# 			for nxt_mnky, item in nxt_mnkys:
# 				monkeys[nxt_mnky].items.append(item)
# 			monkey.items = []
#
# monkey_business = sorted(inspections)[-1]*sorted(inspections)[-2]
# print(monkey_business)

# Part 2

rem = math.lcm(*[monkey.test for monkey in monkeys])
inspections = [0]*len(monkeys)

for i in range(10000):
	for monkey in monkeys:
		if monkey.items:
			inspections[monkeys.index(monkey)] += len(monkey.items)
			monkey.inspect()
			nxt_mnkys = monkey.test_items()
			for nxt_mnky, item in nxt_mnkys:
				item = item % rem
				monkeys[nxt_mnky].items.append(item)
			monkey.items = []


monkey_business = sorted(inspections)[-1]*sorted(inspections)[-2]
print(monkey_business)
