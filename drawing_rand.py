# Random drawing
from random import randint
from datetime import datetime


now = datetime.now()
#Enter in your csv file
file_name = input('Please enter in your csv file name: ')

def plr_list(lst):
    
    log = open('log.txt', 'a+')
    try:
        with open(lst, 'r') as reader:
            dict_list = []
            for line in reader:
                dict_list.append(line)
            dict_len = len(dict_list)
            rand = randint(0, dict_len)
            print(rand)
            print(now.month, now.day, now.year)
        log.write(str('{}{}{}-{}:{}:{},'.format(now.year, now.month, now.day, now.hour, now.minute, now.second ))) + log.write(dict_list[rand -1])
        return 'The Winner is: \n' +  dict_list[rand -1]
    except FileNotFoundError:
        print('You have enter:', file_name, '\n\n**Please check spelling and try again.**', )
    else:
        print('else')
players_list = file_name

print(plr_list(players_list))
