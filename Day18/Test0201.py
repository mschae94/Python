"""
omr 카드 만들기
문제 1)  먼저 10자리 정답을 등록합니다  ex) 1234234212
문제 2)  학생수를 입력받습니다  ex) 3
문제 3) 학생이름을 입력합니다 , 학생정답지를 입력합니다
ex) 김철수 , 4234231212
문제 4) 결과를 출력합니다 o x 그리고 정답수
ex) ooooxxxoox  김철수 : 60점
"""
class Student:
    def __init__(self  , number ):
        self.number = number
        print("%d."%self.number , end='')
        self.student_name = input("이름을 입력해주세요 : ")
        while True:
            self.student_answer = input("정답을 입력해주세요(5): ")
            if len(self.student_answer) == 5:
                break
            else:
                print("정답이 5개인지 확인해주세요")
print("***** 정답 입력  *****")
answer = input("정답(5개) 입력: ")
user_count = int(input("사용자는 몇명입니까? "))
user_answer_list = []
for i in range(user_count):
    user_answer_list.append(Student(i+1))
print("*** 채점결과 ***")
for i in user_answer_list:
    result = 0 # 점수
    print(i.number , i.student_name)

    for j in range(5):
        if answer[j] == i.student_answer[j]:
            result +=20
            print('o' , end='')
        else:
            print('x' , end='')
    print(result)