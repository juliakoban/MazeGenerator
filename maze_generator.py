from termcolor import colored
import random
import sys

# symbols used to print out the maze

wall = "w"
passage = "#"
unvisited = "u"

# maze size given with command-line arguments and exception handling

try:
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    if width < 3 or height < 3:
        raise ValueError
except ValueError:
    sys.exit("Width and height of the maze should be positive integers greater than 2!")
except IndexError:
    sys.exit("Give both width and height of the maze!") # not exit


# FUNCTIONS


# initialize empty maze
def init_maze(width, height):
    maze = []
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(unvisited)
        maze.append(line)
    return maze


# print maze
def print_maze(maze):
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if my_maze[i][j] == unvisited:
                print(colored(maze[i][j], "cyan", attrs=["dark"]), end="  ")
            elif maze[i][j] == passage:
                print(colored(maze[i][j], "white", attrs=["reverse"]), end="  ")
            else:
                print(colored(maze[i][j], "blue", attrs=["dark"]), end="  ")
        print("\n")
    


# chceck how many passages surrounds a wall
def surrounding_passages(maze, wall):
    number_of_passages = 0

    if maze[wall[0] - 1][wall[1]] == passage:
        number_of_passages += 1
    if maze[wall[0] + 1][wall[1]] == passage:
        number_of_passages += 1
    if maze[wall[0]][wall[1] - 1] == passage:
        number_of_passages += 1
    if maze[wall[0]][wall[1] + 1] == passage:
        number_of_passages += 1

    return number_of_passages


# make upper cell of the new passage cell a wall
def upper_cell_to_wall(maze, cell, walls_list):
    if cell[0] != 0:
        if maze[cell[0] - 1][cell[1]] != passage:
            maze[cell[0] - 1][cell[1]] = wall
        if [cell[0] - 1, cell[1]] not in walls_list:
            walls_list.append([cell[0] - 1, cell[1]])


# make bottom cell of the new passage cell a wall
def bottom_cell_to_wall(maze, cell, walls_list):
    if cell[0] != height - 1:
        if maze[cell[0] + 1][cell[1]] != passage:
            maze[cell[0] + 1][cell[1]] = wall
        if [cell[0] + 1, cell[1]] not in walls_list:
            walls_list.append([cell[0] + 1, cell[1]])


# make left cell of the new passage cell a wall
def left_cell_to_wall(maze, cell, walls_list):
    if cell[1] != 0:
        if maze[cell[0]][cell[1] - 1] != passage:
            maze[cell[0]][cell[1] - 1] = wall
        if [cell[0], cell[1] - 1] not in walls_list:
            walls_list.append([cell[0], cell[1] - 1])


# make right cell of the new passage cell a wall
def right_cell_to_wall(maze, cell, walls_list):
    if cell[1] != width - 1:
        if maze[cell[0]][cell[1] + 1] != passage:
            maze[cell[0]][cell[1] + 1] = wall
        if [cell[0], cell[1] + 1] not in walls_list:
            walls_list.append([cell[0], cell[1] + 1])


# MAIN

my_maze = init_maze(width, height)

# initilize starting cell and make sure starting cell is not on the edge of the maze
starting_width = random.randint(1, width - 2)
starting_height = random.randint(1, height - 2)
my_maze[starting_height][starting_width] = passage

# create walls list, add walls surrounding passage and mark them as walls
walls = []
walls.append([starting_height, starting_width - 1])
walls.append([starting_height, starting_width + 1])
walls.append([starting_height + 1, starting_width])
walls.append([starting_height - 1, starting_width])

my_maze[starting_height][starting_width - 1] = wall
my_maze[starting_height][starting_width + 1] = wall
my_maze[starting_height + 1][starting_width] = wall
my_maze[starting_height - 1][starting_width] = wall


while walls:
    # pick a random wall
    random_wall = random.choice(walls)

    # check if it is a left wall
    if random_wall[1] != 0:
        if (
            my_maze[random_wall[0]][random_wall[1] - 1] == unvisited
            and my_maze[random_wall[0]][random_wall[1] + 1] == passage
        ):
            # find the number of surrounding passages
            s_passages = surrounding_passages(my_maze, random_wall)

            if s_passages < 2:
                # create new passage
                my_maze[random_wall[0]][random_wall[1]] = passage

                # mark new walls
                upper_cell_to_wall(my_maze, random_wall, walls)
                bottom_cell_to_wall(my_maze, random_wall, walls)
                left_cell_to_wall(my_maze, random_wall, walls)

    # check if it is an upper wall
    if random_wall[0] != 0:
        if (
            my_maze[random_wall[0] - 1][random_wall[1]] == unvisited
            and my_maze[random_wall[0] + 1][random_wall[1]] == passage
        ):
            # find the number of surrounding passages
            s_passages = surrounding_passages(my_maze, random_wall)
            if s_passages < 2:
                # create new passage
                my_maze[random_wall[0]][random_wall[1]] = passage

                # mark the new walls
                upper_cell_to_wall(my_maze, random_wall, walls)
                left_cell_to_wall(my_maze, random_wall, walls)
                right_cell_to_wall(my_maze, random_wall, walls)

    # check the bottom wall
    if random_wall[0] != height - 1:
        if (
            my_maze[random_wall[0] + 1][random_wall[1]] == unvisited
            and my_maze[random_wall[0] - 1][random_wall[1]] == passage
        ):
            # find the number of surrounding passages
            s_passages = surrounding_passages(my_maze, random_wall)
            if s_passages < 2:
                # create new passage
                my_maze[random_wall[0]][random_wall[1]] = passage

                # mark the new walls
                bottom_cell_to_wall(my_maze, random_wall, walls)
                left_cell_to_wall(my_maze, random_wall, walls)
                right_cell_to_wall(my_maze, random_wall, walls)

    # check the right wall
    if random_wall[1] != width - 1:
        if (
            my_maze[random_wall[0]][random_wall[1] + 1] == unvisited
            and my_maze[random_wall[0]][random_wall[1] - 1] == passage
        ):
            # find the number of surrounding passages
            s_passages = surrounding_passages(my_maze, random_wall)
            if s_passages < 2:
                # create new passage
                my_maze[random_wall[0]][random_wall[1]] = passage

                # mark the new walls
                right_cell_to_wall(my_maze, random_wall, walls)
                bottom_cell_to_wall(my_maze, random_wall, walls)
                upper_cell_to_wall(my_maze, random_wall, walls)

    # delete the wall from the list
    for element in walls:
        if element[0] == random_wall[0] and element[1] == random_wall[1]:
            walls.remove(element)


# mark the remaining unvisited passages as walls
for i in range(0, height):
    for j in range(0, width):
        if my_maze[i][j] == unvisited:
            my_maze[i][j] = wall

# set entrance and exit
for i in range(0, width):
    if my_maze[1][i] == passage:
        my_maze[0][i] = passage
        break

for i in range(width - 1, 0, -1):
    if my_maze[height - 2][i] == passage:
        my_maze[height - 1][i] = passage
        break

print_maze(my_maze)
