import sys

def solve():

    input = sys.stdin.readline().strip()

    a = set(input)
    count = len(a)
    if count % 2 == 0 :
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

if __name__ == "__main__":
    solve()