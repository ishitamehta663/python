#open file
file = open("geeks.txt", "r")
content = file.read()
print(content)
file.close()

#read file
file = open("geeks.txt", "rb")
content = file.read()
print(content)
file.close()

#write file
file = open("geeks.txt", "w")
file.write("Hello, World!")
file.close()

# Python code to illustrate append() mode
file = open('geek.txt', 'a')
file.write("This will add this line")
file.close()

#close file
file = open("geeks.txt", "r")
# Perform file operations
file.close()
