#문자열 관련함수

# 1. 문자열의 길이구하기(len)
str = "hahaha"
print("문자열의 길이:", len(str))

# 2. 문자 개수 세기 (count)
str1 = "hihihihihihihih"

print(str1.count('i'))
print(str1.count('h'))

# 3. 위치 알려주기 1 (find)

str2 = "Python World"
print(str2.find('P'))
print(str2.find('W'))

# 4 . 위치 알려주기 2 (index)
print(str2.index('o')) # 문자 'o'가 처음나온 인덱스 위치
#print(str2.index('k')) # 없는문자를 찾으면 에러난다
print(str2.find('k')) # -1 을반환한다

# 5 . 문자열 삽입(join)
str3 = "!"
print(str3.join("okay"))

# 6. 문자열 바꾸기(replace)
str4 = "Life is too short"
print(str4.replace("Life", "Your leg"))

# 7. 문자열 나누기(split)
print(str4.split())
