#while loops

countdown = 10

while countdown > 0:
    print(countdown)
    countdown -= 1

    print('Go!')

# Startverdi: countdown = 5
#Test: countdown > 0
#Endring: countdown -= 1

#Merk: Uten endringen stopper ikke løkka!

number = 1
while number > 5:
    print(number)

    # bug: forgot to increase number