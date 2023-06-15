teams = {}
team_seats = {}
team_scores = {}

stats = {}

n = int(input())
for i in range(n):
    line = input().split()
    teams[line[1]] = line[0]
    team_seats[line[1]] = line[2]

while True:
    line = input()
    if line == "":
        break
    line = line.split()
    team_scores[line[0]] = team_scores.get(line[0], []) + [int(line[1])]
    stats[line[1]] = stats.get(line[1], 0) + 1

sorted_scores = sorted(team_scores.items(), key=lambda x: (-len(x[1]), -int(teams[x[0]])))

champion = []
champion_score = len(sorted_scores[0][1])
for team, scores in sorted_scores:
    score = len(scores)
    print(teams[team], team, score)
    if score == champion_score:
        champion += [team_seats[team]]

print(" ".join(champion))

res = []
for i in range(1, 6):
    res.append(f'{i}:{stats.get(str(i), 0)}')
print(" ".join(res))