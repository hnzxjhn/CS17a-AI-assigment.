import heapq

# Maze grid (0 = free path, 1 = wall)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  # top-left corner
goal = (4, 4)   # bottom-right corner

# Heuristic function (Manhattan distance)
def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# Get valid neighbors
def neighbors(node):
    x, y = node
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    result = []
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
            result.append((nx, ny))
    return result

# A* algorithm
def astar(start, goal):
    open_list = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = [goal]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        for neighbor in neighbors(current):
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current

    return None

# Find path
path = astar(start, goal)

# Print maze with path
if path:
    print("Path found:")
    for i in range(len(maze)):
        row = ""
        for j in range(len(maze[0])):
            if (i,j) == start:
                row += "S "
            elif (i,j) == goal:
                row += "G "
            elif (i,j) in path:
                row += "* "
            elif maze[i][j] == 1:
                row += "# "
            else:
                row += ". "
        print(row)
else:
    print("No path found.")