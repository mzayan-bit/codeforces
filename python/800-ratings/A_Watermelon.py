import sys

input = sys.stdin.readline

def solve():
    w = int(input().strip())

    if w % 2 == 0 and w > 2:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()