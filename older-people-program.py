
#returns a list of those older than specified year

def older_people(people: list, yr: int):
    older_ppl = []
    for each in people:
        year = each[1]
        if year < yr:
            older_ppl.append(each[0])
    return older_ppl
    
    
p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]


yr = int(input('Please type in a year: '))
print(f'Everyone born before {yr}: ')
print(older_people(people, yr))





#lists the oldest person in the list

def oldest_person(people: list):
    listed_years = []
    for each in people:
        listed_years.append(each[1])
    x = min(listed_years)
    for each in people:
        if x == each[1]:
            return each[0]
    

    
p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

print(oldest_person(people))
