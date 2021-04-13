'''Dictionaries: kye-value pairs, unordered '''
my_Dic = {"kye": "val", "age": 20, "name": "cod_error"}
# another define method
My_dic = dict(kye="val", age=20, name="coed_error")
# print my_Dic
print(my_Dic)
# print individual kyes value
print(my_Dic["name"])
print(my_Dic["age"])
# insert another new item;
my_Dic["country"] = "Bangladesh"
print(my_Dic)
# Delete any kye value
del my_Dic["age"]
print(my_Dic)
# OR
my_Dic.pop("kye")
print(my_Dic)
# arbitrary delete item
my_Dic.popitem()
print(my_Dic)
if "name" in my_Dic:
    print(my_Dic['name'])
else:
    print("Error")

try:
    print(my_Dic["name"])
except:
    print("Error")
    # print all items
for kye, value in My_dic.items():
  print(kye, value)
#................ user input in dictionary.............#
n = int(input(print("Enter elements no: ")))
dic = {}
for i in range(n):
  kye = int(input(print("Enter kye:")))
  value = int(input(print("Enter value: ")))
  dic.update({kye: value})
print(dic)
