import sys

input = sys.stdin.readline

def solve():
    m, n = map(int, input().split())
    c=(m*n)/2
    c=int(c)
    print(c)
if __name__ == "__main__":
    solve()