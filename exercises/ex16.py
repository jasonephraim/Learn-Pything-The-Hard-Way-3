from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTR-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

Line1 = input("Line 1: ")
Line2 = input("Line 2: ")
Line3 = input("Line 3: ")

print("I'm going to write these to the file.")

target.write(Line1)
target.write("\n")
target.write(Line2)
target.write("\n")
target.write(Line3)
target.write("\n")

print("And finally, we close it.")
target.close()