#find elf with the most calories
calories_file = open("advent of code python edition.txt", "r")
elf_list = []
calorie = 0;
#read data into list
for elf in calories_file.readlines():
    if elf.isspace():
        elf_list.append(calorie)
        calorie = 0
    else:
        calorie = int(elf) + calorie
calories_file.close()

elf_list.sort()
elf_list.reverse()
max = elf_list[0]
#answer
print(max)

#alternate solution
# max = elf_list[0]
# for e in elf_list:
#     if e > int(max):
#         max = e

#find top three elves
top_three = int(elf_list[0]) + int(elf_list[1]) + int(elf_list[2])
#answer
print(top_three)

