# Escreva um programa que itere em um dicionário utilizando loops.

superbowl = {
  "LVI": "Los Angeles Rams",
  "LV": "Tampa Bay Buccaneers",
  "LIV": "Kansas City Chiefs",
  "LIII": "New England Patriots",
  "LII": "Philadelphia Eagles",
  "LI": "New England Patriots",
  "50": "Denver Broncos"
}

for key in superbowl:
  print(f"O campeão do Super Bowl {key} foi o {superbowl[key]}")