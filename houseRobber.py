def f(i, arr, dp):
    if i == 0:
        return arr[0]
    if i == 1:
        return max(arr[0], arr[1])
    if dp[i] != -1:
        return dp[i]
    
    pick = arr[i] + f(i - 2, arr, dp)
    not_pick = f(i - 1, arr, dp)
    
    dp[i] = max(pick, not_pick)
    return dp[i]

def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    
    dp = [-1] * n
    print(f(n - 1, arr, dp))

if __name__ == "__main__":
    main()