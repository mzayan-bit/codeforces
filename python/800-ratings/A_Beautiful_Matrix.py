import sys

input = sys.stdin.readline

def solve():
    for row_index in range(5):
        row_data = list(map(int, input().split()))
        
        if 1 in row_data:
            col_index = row_data.index(1)
            moves = abs(row_index - 2) + abs(col_index - 2)
            
            print(moves)
            return

if __name__ == "__main__":
    solve()