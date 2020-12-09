# variable.py
# 애완동물 소개해주세요

animal = "강아지"
name = "연탄"
age = 4 
hobby = "산책"
is_adult = age >= 3

print("우리집 "+ animal +" 이름은 "+ name)
hobby = "공놀이"
# print(name + "는 "+ str(age)+"살, " + hobby +"을(를) 좋아함")
print(name,"는 ", age,"살, ", hobby,"을(를) 좋아함")
print(name+" 이는 어른일까요? "+ str(is_adult))
