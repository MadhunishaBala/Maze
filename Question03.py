import random

def maze(rows=6, cols=6, num_barriers=4):
    maze = [['-' for i in range(cols)] for i in range(rows)] #Empty postions are denoted with "-"

    # Start Node
    start_x = random.randint(0, 1)# Start node should be in the first or second column
    start_y = random.randint(0, rows - 1)
    maze[start_y][start_x] = 's'  

    # Goal position
    goal_x = random.randint(cols - 2, cols - 1)  # Goal node should be in the last or one before the last column
    goal_y = random.randint(0, rows - 1)
    maze[goal_y][goal_x] = 'g'

    # Barrier Nodes
    barrier = 0
    while barrier < num_barriers:
        barrier_x = random.randint(0, cols - 1)
        if barrier_x != start_x and barrier_x != goal_x:
            barrier_y = random.randint(0, rows - 1)
            if maze[barrier_y][barrier_x] == '-':
                maze[barrier_y][barrier_x] = 'x' #Barriers are denoted with "x"
                barrier += 1

    return maze, (start_x, start_y), (goal_x, goal_y)

def adjacent(maze, current, barrier):
    x, y = current
    neighbors = []

    # Valid moves: horizontal, vertical, diagonal
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for move in moves:
        new_x, new_y = x + move[0], y + move[1] #Calculates the new x y points
        if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze) and maze[new_y][new_x] != barrier: #checks if its a valid posititon
            neighbors.append((new_x, new_y))

    return neighbors

def dfs(maze, start, goal, barrier='x'):
    stack = [(start, [start], 0)] #Initialized as a list which takes the current position, path taken and the cost
    visited = set()# A set keeps track of the visited nodes
    total_cost = 0

    while stack: #Continues as long as stack is not empty
        current, path, cost = stack.pop()
        x, y = current

        if current == goal: #Checks if current position is goal
            total_cost = cost
            return path, list(visited), total_cost

        if current not in visited: #Checks if the current posititon has not been visited
            visited.add(current)
            
            neighbors = adjacent(maze, current, barrier)
            neighbors.sort()

            for neighbor in neighbors: #Check the neighbors and adds to the stack
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], cost + 1))

    return None, list(visited), total_cost

def manhattan_distance(node, goal):
    x = node[0] - goal[0] if node[0] > goal[0] else goal[0] - node[0]
    y = node[1] - goal[1] if node[1] > goal[1] else goal[1] - node[1]
    return x + y

def sorting(x):
    return x[2]+ x[3] #Sorting based on the addition of total cost and heuristic cost

def a_star(maze, start, goal, barrier='x'):
    stack = [(start, [start], 0, manhattan_distance(start, goal))]
    visited = set()
    find_goal = 0 #Store the total cost to find goal
    heurisitic = 0 #Stores heuristic value

    while stack:
        stack.sort(key=sorting)  
        current, path, cost, heuristic = stack.pop(0)
        x, y = current

        if current == goal: #Checks if current position is goal
            find_goal = find_goal + cost  # Update the time to find the goal
            return path, list(visited), find_goal, heuristic

        if current not in visited: #Checks if the current posititon has not been visited
            visited.add(current)
            neighbors = adjacent(maze, current, barrier)
            neighbors.sort()

            for neighbor in neighbors:
                if neighbor not in visited:
                    neighbor_cost = cost + 1
                    neighbor_heuristic = manhattan_distance(neighbor, goal)
                    stack.append((neighbor, path + [neighbor], neighbor_cost, neighbor_heuristic))

    return None, list(visited), find_goal, heuristic

# Generate maze 
maze,start,goal = maze()

print("Maze:")
for row in maze:
    print(' '.join(row))

# DFS function is called
dfs_path, visited_dfs, cost_dfs = dfs(maze, start, goal)

# Mark the path in the maze for DFS
for x, y in dfs_path:
    maze[y][x] = '*'

# Maze after DFS traversal
print("\nDFS Maze:")
for row in maze:
    print(' '.join(row))

print("\nDFS Results:")
print("Visited Nodes:", visited_dfs)
print("Total Cost to find the goal:", cost_dfs, "minutes")

# A* search function is called
astar_path, visited_astar, time_astar, heuristic_cost = a_star(maze, start, goal)

# Mark the path in the maze for A*
for x, y in astar_path:
    maze[y][x] = '*'

# Maze after A* search 
print("\nA* Maze:")
for row in maze:
    print(' '.join(row))

print("\nA* Results:")
print("Visited Nodes:", visited_astar)
print("Time to find the goal:", time_astar, "minutes")

print("\nFinal Path:")
def path_heuristic(path, goal):
    i = 0
    for node in path:
        x, y = node
        Fheuristic = manhattan_distance(node, goal)
        print(f"Node {i}: ({x}, {y}), Heuristic Cost: {Fheuristic}")
        i += 1
path_heuristic(astar_path, goal)

