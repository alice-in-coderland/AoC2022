with open('input.txt') as f:
	my_program = [line.strip() for line in f.readlines()]


# Part 1


def run_program(program):
	cycle = 0
	signal_strength = 0
	Xregister = 1
	cycles_dict = {'noop': 1, 'addx': 2}
	tot_cycles = sum(cycles_dict[line.split()[0]] for line in program)

	for line in program:
		operation, *arg = line.split()
		for i in range(cycles_dict[operation]):
			cycle += 1
			if cycle in range(20, tot_cycles, 40):
				signal_strength += cycle*Xregister
		if operation == 'addx':
			Xregister += int(*arg)
	return signal_strength


print(f'The sum of signal strengths is {run_program(my_program)}.\n')


# Part 2


def draw_sprite(program):
	cycle = 0
	Xregister = 1
	cycles_dict = {'noop': 1, 'addx': 2}
	CRT = ['']*6
	pixel_lit = '#'
	pixel_dark = '.'

	for line in program:
		operation, *arg = line.split()
		for i in range(cycles_dict[operation]):
			CRT[cycle//40] += pixel_lit if cycle%40 in [Xregister-1, Xregister, Xregister+1] else pixel_dark
			cycle += 1
		if operation == 'addx':
			Xregister += int(*arg)
	return CRT

print('Eight capital letters appear on my CRT:\n')
for line in draw_sprite(my_program):
	print(line)