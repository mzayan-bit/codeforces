import sys

input = sys.stdin.readline

def solve():
    s1 = input().strip().lower()
    s2 = input().strip().lower()

    if s1 < s2:
        print("-1")
    elif s1 > s2:
        print("1")
    else:
        print("0")

if __name__ == "__main__":
    solve()