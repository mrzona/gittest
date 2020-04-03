from sys import argv
script, filename = argv

print(f"We are going to erase {filename}.")
print("if you dont want than hit CTRL-C. (^C).")
print("If you do want that, hit Return.")

input("?")

print("opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("NOw Im going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Im going to write the to a file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally , we close it")
target.close