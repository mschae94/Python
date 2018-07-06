#학점처리 (2단계)


#학생 이름 , 성적은 국어 한개만
#100 이상 예외처리
# 96 <= 점수 A+
# 93 <= 점수 A
# 90 <= 점수 A-
# 86 <= 점수 B+
# 83 <= 점수 B
# 80 <= 점수 B-

# 59 이하 F

name = input("이름")
score = int(input("국어"))
hak = score // 10
op = score % 10
result = ""
if hak <= 10 :
    if hak == 9 or hak == 10:
        result = 'A'
    elif hak == 8 :
        result = 'B'
    else :
        result = 'F'
    if hak >= 6:
        if op >=6 or hak ==10:
            result += '+'
        elif op < 4:
            result += '-'
    print("이름: %s" % name)
    print("학점: %s" % result)
























# name =input("이름을 입력하세요")
# score = int(input("국어"))
# hak = score // 10
# op = score % 10
#
# result = ""
#
# if hak <= 10:
#     if hak == 9 or hak == 10:
#         result = 'A'
#
#     if hak >= 6:
#         if op >= 6 or hak == 10:
#             result += '+'
#         elif op < 4:
#             result += '-'
#
#     print("이름 : %s" % name)
#     print("학점 : %s" % result)