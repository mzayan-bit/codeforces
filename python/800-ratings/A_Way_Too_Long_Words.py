import sys

input = sys.stdin.readline

def solve():
    word = input().strip()
    length = len(word)
    
    if length > 10:
        print(f"{word[0]}{length - 2}{word[-1]}")
    else:
        print(word)

if __name__ == "__main__":
    n = int(input().strip())
    for _ in range(n):
        solve()