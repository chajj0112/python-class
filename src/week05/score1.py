score = int(input("점수를 입력하세요: "))

if score >= 90:
    print("A학점 입니다.")
    print("이해와 성실함이 돋보입니다.")
elif score >= 80:
    print("B학점 입니다.")
    print("안정적인 실력을 갖추셨습니다.")
elif score >= 70:
    print("C학점 입니다.")
    print("주요 내용을 다시 복습해보는 것을 추천합니다.")
elif score >= 60:
    print("D학점 입니다.")
    print("과정을 이수하였으나 보충 학습이 필요합니다.")
else:
    print("F학점 입니다.")
    print("해당 과목의 재수강이나 집중 보충이 필요합니다.")

print("수고하셨습니다.")