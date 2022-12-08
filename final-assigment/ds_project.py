__author__ = '{Navfalbek}'

import queue
import os
from colorama import Fore
import sys


location_name = ["X", "Y", "Z"]

def create_maze():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", " ", " ", "#"])
    maze.append(["Z", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", " ", "#", "#", " ", "#"])
    maze.append(["#", " ", "#", "#", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "X"])
    maze.append(["#", " ", "#", " ", "#", "#", "#", " ", "#"])
    maze.append(["#", "#", "#", "Y", "#", "#", "#", "#", "#"])

    return maze


def print_initial_maze(maze):
    for j, row in enumerate(maze):
        for i, column in enumerate(row):
            print(column + " ", end="")
        print()


def print_resulted_maze(maze, path=""):
    for x, position in enumerate(maze[0]):
        if position == "O":
            start = x

    i = start
    j = 0
    position = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        position.add((j, i))

    print(Fore.GREEN + "Resulted maze\n")

    for j, row in enumerate(maze):
        for i, column in enumerate(row):
            if (j, i) in position:
                print("+ ", end="")
            else:
                print(column + " ", end="")
        print()


def isValid(maze, movements, location_name):
    for x, position in enumerate(maze[0]):
        if position == "O":
            start = x

    i = start
    j = 0
    for move in movements:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


def findEnd(maze, movements, location_name):
    for x, position in enumerate(maze[0]):
        if position == "O":
            start = x

    i = start
    j = 0
    for move in movements:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == location_name:
        print(Fore.GREEN + "\nShort path: " + movements)
        print_resulted_maze(maze, movements)
        return True

    return False



path = queue.Queue()
path.put("")
add = ""
maze = create_maze()

try:
    print_initial_maze(maze)
    print("Home (O)")
    print("\n\tMENU\n1.Hospital (X)\n2.Shop (Y)\n3.Gym (Z)")
    location = int(input("Find the path to: "))

    if location in [1, 2, 3]:
        # location_name = ["X", "Y", "Z"]
        print(type(location_name[location-1]), location_name[location-1])
        while not findEnd(maze, add, location_name[location - 1]):
            add = path.get()
            for j in ["L", "R", "U", "D"]:  # L = left, R = right, U = up, D = down
                put = add + j
                if isValid(maze, put, location_name[location - 1]):
                    path.put(put)
    else:
        os.system("cls")
        sys.exit(Fore.RED + "Program exited")
except ValueError:
    sys.exit(Fore.RED + "Should be inputed integer!")
    os.system("cls")
