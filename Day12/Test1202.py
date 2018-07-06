class Singer:
    base_guitar = "베이스 기타"
    drum = "드럼"
    mic = "마이크"


    def exercise(self ,mic):
        print("노래연습")
        self.mic = mic
    def performance(self):
        print("공연중")

seo = Singer()
print(seo.base_guitar)
print(seo.drum)
print(seo.mic)
seo.exercise()
seo.performance()

