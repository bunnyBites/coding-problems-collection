from collections import defaultdict

def find_tournament_winner(competitions, results):
  competition_hash = defaultdict(int)

  for idx in range(len(results)):
    result = results[idx]
    competition = competitions[idx]

    if result == 1:
      competition_hash[competition[0]] += 1
    else:
      competition_hash[competition[1]] += 1

  print(dict(competition_hash))

  max_value = max(competition_hash.values())

  return [competition for competition, result in competition_hash.items() if result == max_value][0]
