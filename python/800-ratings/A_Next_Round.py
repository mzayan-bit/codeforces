import sys

input = sys.stdin.readline

def solve():
    first_line = list(map(int, input().split()))
    n = first_line[0]
    k = first_line[1]
    scores = list(map(int, input().split()))
    cutoff_score = scores[k-1]
    advancers = 0
    for s in scores:
        if s >= cutoff_score and s > 0:
            advancers += 1
        else:
            break
            
    print(advancers)

if __name__ == "__main__":
    solve()