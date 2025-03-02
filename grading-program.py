#User inputs grades
#they finish inputting grades by entering in an empty line


def input_grades():
    pts =[]
    exer = []
    print('SEPERATE SCORES WITH (SPACEBAR)')
    
    while True:
        a = input('Exam points(0-20) and exercises completed(0-100): ')
        if a == '':
            break
        a = a.split()
        if len(a) == 1:
            print('Invalid Entry')
        elif int(a[0]) < 0 or int(a[0]) > 20:
            print('Invalid Entry')
        elif int(a[1]) < 0 or int(a[1]) > 100:
            print('Invalid Entry')
        else:
            pts.append(a[0])
            exer.append(a[1])

    
    print('Statistics: ')
    return pts, exer


def exercise_to_extra_pts(pts, exer):
    x = 0
    extra_pts = 0
    scores = []
    for completions in exer:
        completions = int(completions)
        
        
        if completions < 10:
            extra_pts = 0
        elif completions in range(10, 20):
            extra_pts = 1
        elif completions in range(20, 30):
            extra_pts = 2
        elif completions in range(30, 40):
            extra_pts = 3
        elif completions in range(40, 50):
            extra_pts = 4
        elif completions in range(50, 60):
            extra_pts = 5
        elif completions in range(60, 70):
            extra_pts = 6
        elif completions in range(70, 80):
            extra_pts = 7
        elif completions in range(80, 90):
            extra_pts = 8
        elif completions in range(90, 100):
            extra_pts = 9
        elif completions == 100:
            extra_pts = 10
        full_score = int(pts[x]) + extra_pts
        x += 1
        scores.append(full_score)
    return scores
    
def final_grade(scores):
    grade = ''
    grade_list = []
    for s in scores:
        if s in range(0, 15):
            grade = 0
        elif s in range(15, 18):
            grade = 1
        elif s in range(18, 21):
            grade = 2
        elif s in range(21, 24):
            grade = 3
        elif s in range(24, 28):
            grade = 4
        elif s in range(28, 31):
            grade = 5
        grade_list.append(grade)
    return grade_list

def mean_of_pts(scores):
    numbers = []
    for num in scores:
        num = int(num)
        numbers.append(num)
    mean = sum(numbers) / len(numbers)
    return mean


def grade_output(grade_list):
    y = 5
    while y >= 0:
        x = grade_list.count(y)
        print(f"{y}: {'*' * x}")
        y -= 1
        

def perc_passed(grade_list):
    amt = 0
    for each in grade_list:
        if each > 0:
            amt += 1
    result = amt / len(grade_list)
    return f'{(result * 100): .1f}%'
    

def main(): 
    pts, exer = input_grades()
    scores = exercise_to_extra_pts(pts, exer)
    mean = mean_of_pts(scores)
    grade_list = final_grade(scores)
    final = perc_passed(grade_list)
    print(f'Points average: {mean}')
    print(f'Pass percentage: {final}')
    print('Grade distribution: ')
    grade_output(grade_list)
    
main()
