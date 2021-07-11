# Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# Output : java

file = input("Enter filename: ")

FileSplit = file.split(".")

extension = FileSplit[1]

print(f"The extension of the file {file} is {extension}")
