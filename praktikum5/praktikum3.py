try:
    with open("jafhdr.txt") as file:
        data = file.read()
except FileNotFoundError:
    print("File.e langka bli ketemu cuy!")
    