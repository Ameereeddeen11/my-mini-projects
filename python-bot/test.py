import json
import datetime

birthday_data = '''
{
    "tugilgan kun": {
        "Jake": "03-03",
        "Jon": "12-05",
        "Somebody": "02-22"
    }
}
'''

data = json.loads(birthday_data)
today = datetime.date.today()

closest_date = None
closest_diff = datetime.timedelta(days=365)
closest_person = None

for name, birthday in data["tugilgan kun"].items():
    birthday_date = datetime.datetime.strptime(birthday, "%m-%d").date().replace(year=today.year)
    diff = birthday_date - today
    if 0 <= diff.days < closest_diff.days:
        closest_diff = diff
        closest_date = birthday
        closest_person = name

if data == today:
    print("Dnes má narozeniny:", )
else:
    print("Pro dnešní datum", today.strftime("%m-%d"), "neexistují žádné narozeniny v JSONu. Nejbližší datum je:", closest_date, "a má narozeniny", closest_person)
