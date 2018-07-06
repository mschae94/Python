#딕셔너리 관련 함수들...
a = dict()
print(a)
a1 = dict()
a1["one"] = "첫번째"
print(a1)
a2 = {"HP": "010-0101-0101" , "AGE": 20, "NAME": "김철수"}
keyList = a2.keys()
print(keyList)
for i in keyList:
    print(i)
valueList = a2.values()
print(valueList)
for i in valueList:
    print(i)
item = a2.items()
print(item)
for i in item:
    print(i)
age = a2["AGE"]
print(age)
age = a2.get("AGE")
print(age)
#gender = a2["GENDER"]
#print(gender)
gender = a2.get("GENDER")
print(gender)
confirm = "gender" in a2
print(confirm)
confirm = "AGE" in a2
print(confirm)


