import heapq

# Graph of places
graph = {
    "Market": {"Municipal Hall": 2, "Terminal": 3},
    "Municipal Hall": {"USM": 4},
    "Terminal": {"USM": 2},
    "USM": {}
}

# Heuristic values
heuristic = {
    "Market": 5,
    "Municipal Hall": 3,
    "Terminal": 2,
    "USM": 0
}

def astar(start, goal):
    open_list = [(0, start)]
    came_from = {}
    cost = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = [goal]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        for neighbor in graph[current]:
            new_cost = cost[current] + graph[current][neighbor]

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current

    return None


# Show available locations
print("Available places:")
for place in graph:
    print("-", place)

# User chooses start and destination
start = input("\nEnter starting place: ")
goal = input("Enter destination: ")

# Check if valid
if start not in graph or goal not in graph:
    print("Invalid place entered.")
else:
    route = astar(start, goal)
    
    if route:
        print("\nShortest Route:", " -> ".join(route))
    else:
        print("No route found.")