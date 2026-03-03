t = int(input().strip())

def solve():
    n, x, k = map(int,input().split())
    s = input()

    t1 = -1
    first_zero = 0

    for i in range(n):
        if s[i] == "R": x += 1
        else: x -= 1

        if x == 0:
            t1 = i+1
            break
    
    if t1 == -1 or t1 > k:
        return 0
    
    ans = 1
    new_k = k - t1
    t2 = -1

    for i in range(n):
        if s[i] == "R": x += 1
        else: x -= 1

        if x == 0:
            t2 = i+1
            break
    
    if t2 != -1:
        ans += (new_k // t2)
    
    return ans

    

for _ in range(t):
    print(solve())
