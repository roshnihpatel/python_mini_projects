import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "O", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):
    magenta= curses.color_pair(1)
    cyan = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", magenta)
            else:
                stdscr.addstr(i,j*2, value, cyan)

def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    # breadth first search
    q = queue.Queue()
    #path
    q.put([start_pos]) 

    visited = set()

    while not q.empty():
        path = q.get()
        row, col = path[-1]

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == end:
            return path
        neighbours = find_neighbours(maze, row, col)
        for neighbour in neighbours:
            if neighbour in visited:
                continue
            neighbour_row, neighbour_col = neighbour
            if maze[neighbour_row][neighbour_col] == "#":
                continue
            
            q.put(path + [neighbour])
            visited.add(neighbour)
        

def find_neighbours(maze, row, col):
    neighbours = []
    if row > 0: # up
        neighbours.append((row - 1, col))
    if row + 1 < len(maze): # down
        neighbours.append((row + 1, col))
    if col > 0: # left
        neighbours.append((row, col - 1))
    if col < len(maze[0]): # right
        neighbours.append((row, col + 1))
    return neighbours

def main(stdscr):
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    
    find_path(maze, stdscr)
    stdscr.getch()

wrapper(main)