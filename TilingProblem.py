```
def tailingProblem(n):
    if n <= 2:
        return n
    if n in dp:
        return dp[n]
    
    dp[n] = tailingProblem(n - 1) + tailingProblem(n - 2)
    return dp[n]

dp = {}
n = tailingProblem(int(input("Enter a number:")))
print(n)
```