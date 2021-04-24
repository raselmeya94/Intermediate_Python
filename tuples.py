my_tuples=("banana","apple","mango", 10, 15)
#print tuples
print(my_tuples)
#print tuple length
print(len(my_tuples))
# count item in tuples
new_tuples=("banana","apple","mango","banana", "orange", "apple")
for item in new_tuples:
  print(new_tuples.count(item))
#convert tuples to list
convert_list= list(my_tuples)
print(convert_list)
# find any item in my_tuples
if "apple" in my_tuples:
  print("yes")
else:
  print("no")
multi_tuples=(('x', 'y', 'z'), ('b','c','d'), ('e', 'f', 'g'))
print(multi_tuples[0])
print(multi_tuples[1])
print(multi_tuples[2])
# print inner tuple item
print(multi_tuples[0][0]) #---> multi_tuple[0][0]==X

split_tuple='covid19', 2021, 'virus'
name,year,typ= split_tuple;
print(name)
print(typ)
print(year)