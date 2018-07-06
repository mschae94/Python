def info(name , age , gender = "남자"):
    print("이름은 %s 입니다" % name)
    print("나이는 %d 입니다" % age)

    if gender =="남자":
        print("남자입니다")
    else:
        print("여자입니다")
info("홍길동" , 23)
info("김영자", 20 , "여자")

