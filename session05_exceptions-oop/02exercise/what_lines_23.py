# kva for linjer

try:
    minutes = int(input("Minutes: "))
except ValueError:
    print("Please enter a whole number.")
else:
    print(f"Seconds: {minutes * 60}")
print("Finished")

# Finished blir printa kvar gong fordi den ligger utanfor uttrykket til slutt
# fordi den køyreer om ingen feill oppstår