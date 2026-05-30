# name = input()

# file = open("names.txt", "a")
# file.write(f"{name} \n")
# file.close()

# with open("names.txt", "r") as fl:
#     for line in fl:
#         print("hello,", line.strip())

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"hello, {name}!")