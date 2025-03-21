from itertools import product
import nltk
from nltk.corpus import words

nltk.download("words")  # Download word list if not already present

def load_dictionary():
    return set(word.upper() for word in words.words() if len(word) >= 4)

def get_neighbors(matrix, x, y):
    """Returns valid neighboring positions (8 directions)."""
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] != "0":
            neighbors.append((nx, ny))
    return neighbors

def find_words(matrix, dictionary):
    """Finds all words that use every letter in the matrix at least once."""
    rows, cols = len(matrix), len(matrix[0])
    found_words = set()
    total_letters = sum(1 for row in matrix for cell in row if cell != "0")
    
    def dfs(x, y, path, visited):
        word = "".join(path)
        if len(visited) == total_letters and word in dictionary:
            found_words.add(word)
        
        for nx, ny in get_neighbors(matrix, x, y):
            if (nx, ny) not in visited:
                dfs(nx, ny, path + [matrix[nx][ny]], visited | {(nx, ny)})
    
    for i, j in product(range(rows), range(cols)):
        if matrix[i][j] != "0":
            dfs(i, j, [matrix[i][j]], {(i, j)})
    
    return found_words

# Example matrix
matrix = [
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "I", "I", "0"],
    ["0", "0", "C", "H", "L", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"]
]

dictionary = load_dictionary()
words = find_words(matrix, dictionary)
print("Words found:", words)