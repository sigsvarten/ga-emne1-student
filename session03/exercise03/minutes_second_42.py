# konvertere til sekunder

def convert_to_minutes_to_seconds(minutes):
    to_seconds = minutes  * 60
    return to_seconds

seconds = convert_to_minutes_to_seconds(99)
seconds_2 = convert_to_minutes_to_seconds(2.5)
seconds_3 = convert_to_minutes_to_seconds(10)

print(f'{seconds}')
print(f'{seconds_2}')
print(f'{seconds_3}')
