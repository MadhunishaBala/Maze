# Maze solver using DFS and A* algorithms

## **Overview**

Generates a random maze and solves it using Depth-First Search (DFS) and A* search algorithms. The maze is represented as a 2D grid with starting and goal positions, along with optional barrier nodes which are chosen randomly.

## **Script Explanation**
maze(rows=6, cols=6, num_barriers=4): Generates a random maze with a specified number of rows, columns, and barriers.

dfs(maze, start, goal, barrier='x'): Implements Depth-First Search to find a path from the start to the goal in the maze.

a_star(maze, start, goal, barrier='x'): Implements A* search algorithm to find an optimal path from the start to the goal, considering heuristic cost.

## **Results**
After running the script; the generated maze, the solution path for DFS and A* are displayed.

DFS Results
Visited Nodes: List of nodes visited during DFS traversal.
Total Cost to find the goal: Time taken (in minutes) to reach the goal using DFS

A* Results
Visited Nodes: List of nodes visited during A* search.
Time to find the goal: Total time (in minutes) taken to reach the goal using A*

Final Path
Displays the final path found by A* along with heuristic costs for each node.


