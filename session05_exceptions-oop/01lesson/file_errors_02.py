from pathlib import Path

# Alternative 1 – keep relative path:
# (We did it like this last lesson.)
# data_folder = (Path("..") / "data")
# Alternative 2 - absolute path:
# Some had problems with last lesson's setup.
# Use this instead, with an absolute path:

data_folder= Path(__file__).parent.parent / "data"
path = data_folder/ "number.txt"
print(path)

try:
# Note: 1) path can be in front or as 1st param:
# open(path, ...) or path.open(...)
# 2) default file modus is "r".
    with path.open(encoding="utf-8") as file:
        message = file.read()
    print(message)
except FileNotFoundError:
    print(f"Error, could not find file: {path}")
except ValueError:
    print("The file must contain an integer.")