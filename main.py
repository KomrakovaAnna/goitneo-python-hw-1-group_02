from datetime import datetime
from collections import defaultdict
import calendar


def get_birthdays_per_week(users):
    today = datetime.today().date()
    birthdays_list = defaultdict(list)
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            (birthday.replace(year=today.year + 1))
        delta_days = (birthday_this_year - today).days
        delta_days_with_week_days = delta_days
        if delta_days == -1 or delta_days == -2:
            delta_days_with_week_days = 0
        if 0 <= delta_days < 5:
            if calendar.day_name[delta_days_with_week_days] in birthdays_list:
                birthdays_list[calendar.day_name[delta_days_with_week_days]].append(
                    name
                )
            else:
                birthdays_list[calendar.day_name[delta_days_with_week_days]] = [name]
    for key, value in dict(birthdays_list).items():
        print("{}: {}".format(key, ", ".join(value)))


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 12, 3)},
    {"name": "Jan Koum", "birthday": datetime(1985, 12, 3)},
    {"name": "Jill Valentine", "birthday": datetime(1955, 12, 7)},
    {"name": "Kim Kardashian", "birthday": datetime(1955, 10, 28)},
]
get_birthdays_per_week(users)
