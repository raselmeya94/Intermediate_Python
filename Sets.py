#Sets: unordered , mutable , no duplicates
myset={1,2,3,4,5};
print(myset)

#check allow duplicates items
myset={1,2,3,4,5,1,2,3,4}
print(myset)

#add new elements

myset.add(6)
myset.add(7)
myset.add(8)
print(myset)

#remove any elements 
myset.remove(8)
myset.discard(7)
print(myset)

# iterate set elements using Loop
for item in myset:
  print(item)


if 1 in myset:
  print("yes")
else:
  print("no")
# erase set
myset.clear()
print(myset)

# union , intesection
odd={1,3,5,7,9}
even={2 ,4 ,6 ,8 ,10}
value={1,2,3,4,5,7}
union_set= odd.union(even)
print(union_set)
intersection_set= even.intersection(value)
print(intersection_set)

# difference of two sets
A={1,2,3,4,5,6,7,8,9,10}
B={5 , 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

diff_AB= A.difference(B)
print(diff_AB)
diff_BA=B.difference(A)
print(diff_BA)


# symmetric difference of two sets

symmetric = A.symmetric_difference(B)
print(symmetric)

# set update

A.update(B)
print(A)

#subset or superset check

setA={1,2,3,4,5}
setB={1,2,3}
print(setB.issubset(setA))
print(setA.issuperset(setB))