# Konvertere til sekunder, minutter og timer, firee tester

#test1
second = int (input(' Tap in how many seconds: '))

hour = int (second // 3600)
the_rest = int (second % 3600)
minutes =  int( the_rest // 60)
seconds = int(the_rest % 60)

print (f'{hour} time' + ',' + f'{minutes} minutter ' + 'og ' + f'{seconds} sekunder ')

#test2
second2 = int (input(' The seconds here: '))

hour2 = int (second2 // 3600)
the_rest2 = int (second2 % 3600)
minutes2 =  int( the_rest2 // 60)
seconds2 = int(the_rest2 % 60)

print (f'{hour2} time' + ',' + f'{minutes2} minutter ' + 'og ' + f'{seconds2} sekunder ')

#test3
second3 = int (input('How many seconds this time? '))

hour3 = int (second3 // 3600)
the_rest3 = int (second3 % 3600)
minutes3 =  int( the_rest3 // 60)
seconds3 = int(the_rest3 % 60)

print (f'{hour3} time' + ',' + f'{minutes3} minutter ' + 'og ' + f'{seconds3} sekunder ')


#test4
second4 = int (input(' Tap in the seconds here: '))

hour4 = int (second4 // 3600)
the_rest4 = int (second4 % 3600)
minutes4 =  int( the_rest4 // 60)
seconds4 = int(the_rest4 % 60)

print (f'{hour4} time' + ',' + f'{minutes4} minutter ' + 'og ' + f'{seconds4} sekunder ')
