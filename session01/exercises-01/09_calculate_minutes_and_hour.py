# minutter til timer og minutter

total_minutes1 = float(60)
total_minutes2 = float(90)
total_minutes3 = float(135)
total_minutes4 = float(536)

#variabler time og minutter
hours = int (total_minutes4 // 60)
minutes =  int ( total_minutes4 % 60)

#lager input
input_minute = input('What is the minute?' )
input_minutes = (int (input_minute) // 60)
input_hours = (int(input_minute) % 60 )

#skriver ut begge
print(f'{input_minutes}' + ' timer og ' + f'{input_hours}' + ' minutter')

print(f'{hours}' + ' timer og ' + f'{minutes}' + ' minutter')
