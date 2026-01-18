import sys

input = sys.stdin.readline

def solve():
    s = input().strip()
    numbers = s.split('+')
    numbers.sort()
    
    print('+'.join(numbers))

if __name__ == "__main__":
    solve()