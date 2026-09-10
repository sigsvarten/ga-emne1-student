# Nedtelling funksjon og løkke


def show_countdown():
    counter = 0
    for loop_counter in range(5, 0, -1):
        print(f'{loop_counter}')

show_countdown()
print('Start!')