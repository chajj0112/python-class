# 과제 1

height_cm = int(input("키를 입력하세요 : "))
standardweight = (height_cm - 100)*0.9
overweight = standardweight*1.2
underweight = standardweight*0.8

print("당신의 신장 :", height_cm)
print("적정 몸무게 :", standardweight)
print("과체중 위험 기준 :", overweight)
print("저체중 위험 기준 :", underweight)