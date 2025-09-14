memo = {}

def fib(n):
    
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
        
    return memo[n]



def main():
    
    number = int(input("Input a number: "))
    
    result = fib(number)
    
    print(f"The fibonacci of {number} is {result}")
    
if __name__ == "__main__":
    main()