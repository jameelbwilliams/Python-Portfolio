
#MOVIE DATABASE PART 1 

def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie = {}
    movie[f"name"] = name
    movie[f"director"] = director
    movie[f"year"] = year
    movie[f"runtime"] = runtime
    
    database.append(movie)
    return database

#PART 2 
#MOVIE NAME SEARCH

def find_movies(database: list, search_term: str):
    matches = []
    none = 'There are no matches...'
    for each in database:
        if search_term.lower() in each['name'].lower(): 
            matches.append(each)
    if len(matches) == 0:
        return none
    else:
        return matches
    

databased_movies = []
add_movie(databased_movies, "Gone with the Python", "Victor Pything", 2017, 116)
add_movie(databased_movies, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
print(f'Currently Added: {databased_movies}')
print()
searched_movies = find_movies(databased_movies, 'with')
print(f'Search Results: {searched_movies}')


