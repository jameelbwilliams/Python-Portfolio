#PART 1 (COMPLETED)

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ' ']
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]


letter_to_points = dict(zip(letters, points))

player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'LexiCon': ['ERASER', 'BELLY', 'HUSKY'], 'ProfReader': ['ZAP', 'COMA', 'PERIOD']}

player_to_points = {}


def score_word(word: str):
    point_total = 0
    for each in word.upper():
      point_total += letter_to_points.get(each, 0)
  
    return point_total

for player, words in player_to_words.items():
    player_points = 0
  
    for word in words:
      player_points += score_word(word)
    
    player_to_points[player] = player_points

print(player_to_points)




#UPDATED VERSION

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ' ']
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]


letter_to_points = dict(zip(letters, points))

player_to_words = {}

player_to_points = {}


def add_players():
    x = 1
    amount = int(input('How many players? '))
    while x <= amount:
        name = str(input(f"Player {x}'s Name: "))
        if name not in player_to_words:
            player_to_words[name] = []
            x += 1
    
    return player_to_words


def add_words(player_to_words: dict):
    for name in player_to_words:
        for rounds in range(1, 4):
            word = str(input(f"{name}'s Word {rounds}: "))
            player_to_words[name].append(word)

    
    return player_to_words



def score_word(word: str):
    point_total = 0
    for each in word.upper():
      point_total += letter_to_points.get(each, 0)
  
    return point_total


def player_score(player_to_words: dict):
    for player, words in player_to_words.items():
        player_points = 0
  
        for word in words:
            player_points += score_word(word)
    
        player_to_points[player] = player_points
    
    for name, score in player_to_points.items():
        print(f"{name} finished with a score of: {score}")
    

    
print("Welcome to 3-round Scrabble!")
add_players()
add_words(player_to_words)
print()
player_score(player_to_words)
