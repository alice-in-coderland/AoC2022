with open('input.txt') as f:
    scan = f.read().strip().split('\n')

# scan = '''498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9'''.split('\n')

# Part 1

# get all coordinates of rocks
def get_lines_coords(scan_lines):
    all_linepoints = []

    for line in scan_lines:
        points = [[elem for elem in list(map(int, point.split(',')))] for point in line.split(' -> ')]
        linepoints = []

        for i in range(len(points) - 1):
            x_start, y_start = points[i][0], points[i][1]
            x_end, y_end = points[i + 1][0], points[i + 1][1]

            if x_start == x_end:
                if y_start < y_end:
                    for y in range(y_start, y_end + 1):
                        linepoints.append((x_start, y))
                else:
                    for y in range(y_end, y_start + 1):
                        linepoints.append((x_start, y))
            elif y_start == y_end:
                if x_start < x_end:
                    for x in range(x_start, x_end + 1):
                        linepoints.append((x, y_start))
                else:
                    for x in range(x_end, x_start + 1):
                        linepoints.append((x, y_start))

        all_linepoints.extend(linepoints)

    return set(all_linepoints)


rock_and_sand_coords = get_lines_coords(scan)
# find the lowest point
lowest = 0
for coord in rock_and_sand_coords:
    if coord[1] > lowest:
        lowest = coord[1]


def move_sand():
    xstart, ystart = 500, 0

    x, y = xstart, ystart

    while True:
        # check if sand is falling into the abyss
        if y >= lowest:
            return False
        # check if sand can go straight down
        if (x, y+1) not in rock_and_sand_coords:
            y += 1
        # check if sand can go left diagonally
        elif (x-1, y+1) not in rock_and_sand_coords:
            y += 1
            x -= 1
        # check if sand can go right diagonally
        elif (x+1, y+1) not in rock_and_sand_coords:
            y += 1
            x += 1
        # if not, return the current position
        else:
            return (x, y)


sand_counter = 0

while True:
    match move_sand():
        case False:
            break
        case (x, y):
            rock_and_sand_coords.add((x, y))
    sand_counter += 1

print(f'{sand_counter} units of sand come to rest before sand starts flowing into the abyss below.')


# Part 2

rock_and_sand_coords = get_lines_coords(scan)

# find the lowest point
lowest = 0
for coord in rock_and_sand_coords:
    if coord[1] > lowest:
        lowest = coord[1]

floor = lowest + 2

# add floor
for i in range(0, 1000):
    rock_and_sand_coords.add((i, floor))


def move_sand_again():
    xstart, ystart = 500, 0

    x, y = xstart, ystart

    while True:
        # check if sand can go straight down
        if (x, y+1) not in rock_and_sand_coords:
            y += 1
        # check if sand can go left diagonally
        elif (x-1, y+1) not in rock_and_sand_coords:
            y += 1
            x -= 1
        # check if sand can go right diagonally
        elif (x+1, y+1) not in rock_and_sand_coords:
            y += 1
            x += 1
        # if not, return the current position
        else:
            if y == ystart:
                return None
            return (x, y)


sand_counter = 0

while True:
    sand_counter += 1
    match move_sand_again():
        case None:
            break
        case (x, y):
            rock_and_sand_coords.add((x, y))


print(f'{sand_counter} units of sand come to rest.')


#%%
