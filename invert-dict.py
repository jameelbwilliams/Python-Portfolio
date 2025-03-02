#inverts a dictionary

def invert(given: dict):
    new_dict = {}
    for key in given:
        new_dict[(given[key])] = key
    return new_dict
    

s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
print(invert(s))
