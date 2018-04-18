my_input = open("dirty.txt", "r")
output = open("input.txt", "w")

output.write("1000\n")

for line in my_input:
    line = line.strip("\n").strip(" ")
    output.write(line + ", ")

output.write("\n248\n4")
