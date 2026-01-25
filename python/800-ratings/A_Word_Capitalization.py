import sys

input = sys.stdin.readline

def solve():
 
    word =input().strip()
    result = word[0].upper() + word[1:]
    
    print(result)
    

if __name__ == "__main__":

    solve()