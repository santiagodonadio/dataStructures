city_map = {} # Empty dictionary

cities = ["Medford", "Somerville", "Arlington", "Malden"]
city_map["Massachusetts"] = [] # Defining key in the dict city_map

city_map["Massachusetts"] += cities

state_list = city_map.keys()

print("This is by calling the keys \n", state_list)


city_list = city_map.values()

print("This is by calling the values \n",city_list)

