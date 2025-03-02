import csv

compromised_users = []

#open the csv file with usernames and passwords as dictionaries
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  

  #add list of users to compromised list
  for password_row in password_csv:
    compromised_users.append(password_row['Username'])
  print(compromised_users)

#open new file in write mode and write each compromised user inside
with open('compromised_users.txt', 'w') as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user)

with open('compromised_users.txt') as compromised_user_file:   
  print(compromised_user_file.readline())


#creating a message to the boss in JSON
import json

#open the json file, create a dict, and put it in the file
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {'recipient': 'The Boss', 'message': 'Mission Success'}
  json.dump(boss_message_dict, boss_message)


#save the hacker's signature
slash_null_sig = '''
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/

'''

#write the hacker signature to the passwords file
with open('passwords.csv', 'w') as new_passwords_obj:
  new_passwords_obj.write(slash_null_sig)


#cut the code from lines 6 - 14 and run this to see the new contents
with open('passwords.csv') as new_passwords_obj:
  print(new_passwords_obj.read())
