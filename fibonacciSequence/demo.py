def askNumber():
    
    while True:
        try:
            return int(input("Enter a position in the fibonacci sequence (Fn): "))
        except ValueError:
            print("Enter a whole number")

def fibIterative(n):
    
    # Checking edge cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Define variables to keep track of positions
    fib = [0, 1]
    
    y = 1
    
    while y != n:
        
       fib.append(fib[-1] + fib[-2])
       
       y += 1
    
    
    return fib[-1]

def main():

    while True:
    
        posNumber = askNumber()

        posValue = fibIterative(posNumber)
        
        print(f"At position {posNumber} in the fibonacci sequence the value is {posValue}")
        
        answers = ['y', 'n']
        
        while True:
            
            response = input("Do you want to enter another positionin the fibonacci sequence? (y/n) ").lower()
                
            if response in answers:
                break
            else:
                print("Enter either 'y' or 'n'")
            
        # Out of while looop
        
        if response == 'n':
            break
        
            

    
    
    


if __name__ == "__main__":
    main()
    
