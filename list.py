name = ["Dhaka", "Mymensingh", "Noakhali", "Chattogram", "Khulna"]
# All name print
print(name)
# individual name print
print("\n")
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print through reverse side
print("\n")
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
# All name item print through iterative for loop
print("\n")
for item in name:
    print(item)

# create two different list
newlist1 = [1, 2, 3, 4, 5]
print(newlist1)
newlist2 = [6, 7, 8, 9, 10]
print(newlist2)
# add two list
add_list = newlist1 + newlist2
print(add_list)
# another method to print all item of add_list
print(add_list[::])
# reversed all item
print(add_list[::-1])
# print list of item in any range
print(add_list[0:5])
# insert a new item in add_list
add_list.append(11)
print(add_list[:])

#list comprehension
num = [1, 2, 3, 4, 5]
sq = [item * item for item in num]
print(sq)
