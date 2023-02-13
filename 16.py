import random
import itertools
from datetime import timedelta, datetime

teams = ["Команда 1", "Команда 2", "Команда 3", "Команда 4", "Команда 5", "Команда 6", "Команда 7", "Команда 8", 
         "Команда 9", "Команда 10", "Команда 11", "Команда 12", "Команда 13", "Команда 14", "Команда 15", "Команда 16"]

group_size = 4
groups = [teams[i:i + group_size] for i in range(0, len(teams), group_size)]

start_date = datetime(2023, 9, 14)
game_time = datetime.strptime("22:45", "%H:%M")

for i, group in enumerate(groups):
    print(f"Группа {i+1}: {group}")

print("\nРасписание:")
for i, group in enumerate(itertools.combinations(groups, 2)):
    for j, (team1, team2) in enumerate(itertools.product(group[0], group[1])):
        date = start_date + timedelta(weeks=j*2, days=i*3)
        time = game_time
        print(f"{team1} vs {team2}: {date.strftime('%d/%m/%Y')}, {time.strftime('%H:%M')}")