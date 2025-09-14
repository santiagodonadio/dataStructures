def fib(n):
    
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]



def main():
    
    number = int(input("Input a number: "))
    
    result = fib(number)
    
    print(f"The fibonacci of {number} is {result}")
    
if __name__ == "__main__":
    main()