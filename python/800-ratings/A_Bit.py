import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())
    x = 0
    for _ in range(n):
        statement = input().strip()
        if "++" in statement:
            x += 1
        else:
            x -= 1
    print(x)

if __name__ == "__main__":
    solve()