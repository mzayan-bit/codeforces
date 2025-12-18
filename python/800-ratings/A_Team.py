import sys

# Fast I/O
input = sys.stdin.readline

def solve():
    try:
        line = input().strip()
        if not line:
            return
        n = int(line)
    except ValueError:
        return
    implemented_count = 0

    for _ in range(n):
        views = list(map(int, input().split()))

        if sum(views) >= 2:
            implemented_count += 1

    print(implemented_count)

if __name__ == "__main__":
    solve()