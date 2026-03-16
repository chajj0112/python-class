# 과제 2

import turtle

radius = int(input("그리고자 하는 원의 반지름을 입력해주세요 : "))

t = turtle.Turtle()
t.width(5)
t.color("blue")
t.circle(radius)

turtle.done()