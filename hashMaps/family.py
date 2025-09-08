
def Main():
    
    family_dict_location = {
        
        "Santiago": ["Worcester", "Medford"],
        "Mom": ["Medford"],
        "Dad": ["Medford"],
        "Camila": ["Medford", "New Hampshire"],
        "James": ["Somerville"],
        "Bill": ["Medford"]

    }
    
    print("Hi, this is a list of people:", ", ".join(family_dict_location.keys()))

    response = input("Enter a name to see where they are living at: ").title()
    
    while response not in family_dict_location:
        print("Invalid")
        response = input("Enter a valid name: ").title()
    
    print(response, " lives at ", ", ".join(family_dict_location[response]))
        
    
Main()
    
