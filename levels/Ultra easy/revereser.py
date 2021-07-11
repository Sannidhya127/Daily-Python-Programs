# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them


name  = input("Enter full name: ")

nameSplit = name.split(" ")

print(f"{nameSplit[1]} {nameSplit[0]}")