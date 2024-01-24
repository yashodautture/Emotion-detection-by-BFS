from collections import deque

class EmotionDetector:
    def __init__(self, matrix):
        # Initialize the EmotionDetector with the provided matrix.
        self.grid = self._convert_matrix_to_grid(matrix)  # Convert the matrix to a grid.
        self.visited_nodes = set()  # Set to store visited nodes during BFS.
        self._extract_visited_nodes()  # Extract visited nodes from the grid.

    def _is_valid_move(self, x, y):
        # Check if a move to coordinates (x, y) is valid within the grid.
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]) and self.grid[x][y] == 1

    def _bfs(self, start_x, start_y):
        # Perform Breadth-First Search starting from (start_x, start_y).
        queue = deque([(start_x, start_y)])
        while queue:
            x, y = queue.popleft()
            if (x, y) not in self.visited_nodes:
                self.visited_nodes.add((x, y))  # Mark the node as visited.
                # Explore neighboring nodes in right, down, left, and up directions.
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_x, new_y = x + dx, y + dy
                    if self._is_valid_move(new_x, new_y):
                        queue.append((new_x, new_y))

    def _convert_matrix_to_grid(self, matrix):
        # Convert a matrix string to a grid of integers.
        rows, cols = 8, 8
        matrix = matrix.replace('\n', '')  # Remove newline characters.
        return [[int(matrix[i * cols + j]) for j in range(cols)] for i in range(rows)]

    def _extract_visited_nodes(self):
        # Extract visited nodes from the grid using BFS.
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 1 and (row, col) not in self.visited_nodes:
                    self._bfs(row, col)  # Start BFS from unvisited nodes.

    def classify_emotion(self):
        # Classify the emotion based on the visited nodes.
        sorted_nodes = sorted(self.visited_nodes, key=lambda node: node[1])
        if not self.visited_nodes:
            return "None"
        if len(set(row for row, _ in self.visited_nodes)) == 1:
            return "Neutral"
        middle_index = len(sorted_nodes) // 2
        # Check for patterns in the visited nodes to determine emotion.
        if all(sorted_nodes[i][0] <= sorted_nodes[i + 1][0] for i in range(middle_index)) or \
                any(sorted_nodes[i][0] > sorted_nodes[i + 1][0] for i in range(middle_index, len(sorted_nodes) - 1)):
            return "Happy"
        if all(sorted_nodes[i][0] >= sorted_nodes[i + 1][0] for i in range(middle_index)):
            return "Sad"

def read_input_file(filename):
    # Read the contents of a file and return it as a string.
    with open(filename, 'r') as file:
        return file.read().strip()

# Read the input file and create an EmotionDetector instance.
matrix = read_input_file(r'm1_input.txt')
detector = EmotionDetector(matrix)

# Print the detected emotion.
print("Detected Emotion:", detector.classify_emotion())
