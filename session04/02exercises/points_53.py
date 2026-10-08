#oppdatere poengtavle

scoreboard = {
    'Steven': 6461,
    'Mika': 2664,
    'Mia': 5647,
    'James': 4545
}

print(scoreboard['Steven'])

scoreboard['Mia'] = 4568
scoreboard['Lee'] = 4985

for names, values in scoreboard.items():
    print(names,values)
