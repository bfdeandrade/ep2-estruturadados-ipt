from collections import defaultdict
import heapq

# Define symbols for representation
symbol_map = {
    "0": " ",  # Caminho Livre
    "1": "#",  # Parede
    "2": "S",  # Ponto de inicio
    "3": "E",   # Ponto de destino
    "+": "+"   # Representa o caminho
}

# Define the four possible directions (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Maze:
    def __init__(self, file):
        self.file = file
    
    def criar_maze(self):
        
        file_path = self.file  

        try:
            with open(file_path, "r") as file:
                maze_data = file.readlines()
                maze_data = [line.strip() for line in maze_data]
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")

        print(maze_data)
        return maze_data
maze = Maze("maze.dat")
maze_data = maze.criar_maze()
# Convert the maze data into a list of lists
maze = [list(row) for row in maze_data]


# Find the dimensions of the maze
rows = len(maze)
cols = len(maze[0])

# Create a graph to represent connections between cells
graph = defaultdict(list)

# Helper function to check if a cell is valid
def is_valid_cell(row, col):
    return 0 <= row < rows and 0 <= col < cols and maze[row][col] != "1"

# Build the graph
for row in range(rows):
    for col in range(cols):
        if maze[row][col] != "1":
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if is_valid_cell(new_row, new_col):
                    graph[(row, col)].append((new_row, new_col))

# Dijkstra's algorithm to find the shortest path
def dijkstra(start, end):
    distances = {cell: float('inf') for cell in graph}
    distances[start] = 0
    queue = [(0, start)]
    previous = {}

    while queue:
        current_distance, current_cell = heapq.heappop(queue)

        if current_cell == end:
            break

        if current_distance > distances[current_cell]:
            continue

        for neighbor in graph[current_cell]:
            distance = current_distance + 1
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_cell
                heapq.heappush(queue, (distance, neighbor))

    if end not in previous:
        return None

    # Reconstruct the path
    path = []
    current = end
    while current != start:
        path.append(current)
        current = previous[current]
    path.append(start)
    path.reverse()

    return path, distance

# Find the shortest path from start (S) to end (E)
start = None
end = None

for row in range(rows):
    for col in range(cols):
        if maze[row][col] == "2":
            start = (row, col)
        elif maze[row][col] == "3":
            end = (row, col)

shortest_path, total_distance = dijkstra(start, end)

# Print the maze with the shortest path
if shortest_path:
    for cell in shortest_path:
        row, col = cell
        maze[row][col] = "+"

print("Shortest path:")
print(total_distance)
for row in maze:
    print(" ".join([symbol_map[cell] for cell in row]))