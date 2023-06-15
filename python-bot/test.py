import json
file_path2 = open('C:/Users/Amir/Desktop/Python/bot/birthdays.json', 'r')
birthday = json.load(file_path2)
from datetime import datetime, date

now = datetime.now()
month_day = now.strftime("%m-%d")
print(birthday)
print(month_day)
for b in birthday:
    if month_day == b:
        print("Hello")
    else:
        #date_differt = [(d - month_day).days for d in b]
        #min_day = min(date_differt)
        #print("Not today but for ", min_day)
        date_difference = [(month_day - d).days for d in b]
        min_days = min(date_difference)
        print(min_days)