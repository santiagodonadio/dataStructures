import time

time.sleep(.5)

print("\nWelcome to Banana Republic")

time.sleep(1)

print("Right now you are the cashier and are dealing with a customer right now")
time.sleep(1)

print("A line is starting to form")
time.sleep(1)

print("You are bored and decide to come up with names for the five people waiting in line")

customers = []

for i in range(5):
    response = input(f"{i + 1} name: ")
    customers.append(response)
    
print("Right now you have 5 customers in queue")
print(customers)

time.sleep(2)
print("It's busy though, you can't remember if someone is in line")

checkName = input("Enter a name of someone to see if there in line: ")

for i in range(5):
    if(checkName.lower() == customers[i].lower()):
        print(f"Yes there in line and they're at the {i + 1} position")
        break
    elif (i == 4):
        print("Nopeee, they ain't in line bro")
    


