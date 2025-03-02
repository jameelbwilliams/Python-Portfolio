#PART 1 OF PHONEBOOK

def phonebook():
    thisdict = {}
    while True:
        command = input('Command (1 search, 2 add, 3 quit): ')
        if command == '1':
            name = str(input('name: '))
            print(thisdict[name])
        elif command == '2':
            name = str(input('name: '))
            number = input('number: ')
            thisdict[name] = number
            print('ok!')
        elif command == '3':
            break
        else:
            print('invalid entry')
    
    print('quitting...')
    
phonebook()


#PART 2 OF PHONEBOOK

def phonebook():
    thisdict = {}
    while True:
        command = input('Command (1 search, 2 add, 3 quit): ')
        if command == '1':
            name = str(input('name: '))
            if name in thisdict: 
                for each in thisdict[name]:
                    print(f"number: {each}")
            else:
                print(f"{name} is not in the phonebook")
        elif command == '2':
            name = str(input('name: '))
            if name not in thisdict:
                thisdict[name]= []
            number = input('number: ')
            thisdict[name].append(number)
            print('ok!')
        elif command == '3':
            break
        else:
            print('invalid entry')
    
    print('quitting...')
    
phonebook()

