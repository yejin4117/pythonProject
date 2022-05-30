#문자열
for ch in "YEJIN":
    print(ch,end='*')
print()
#리스트
for item in ["힙합","발라드"]:
    print(item)

#튜플
for item in (2929,39393):
    print(item)
for a,b in ((12,33),(2,35)):
    print(a,b)

#셋
for item in {"WSM","JAVA","Python"}:
    print(item)

#딕셔너리
pl = {"C":1972, "JAVA":1995, "Python":1991}
for item in pl:
    print(item)
for key in pl.keys():
    print(key)
for val in pl.values():
    print(val)
for key,val in pl.items():
    print(key,val)

#num_list문제
num_list = [-5,127,-13,9,-21,100]
for num in num_list:
    if num > 0:
        print(num)

#짝수, 홀수
num_list = [13,8,7,55,100,2,12,10,17]
for num in num_list:
    if num % 2 == 0:
        print("{}은 짝수이다".format(num))
    else:
        print("{}은 홀수이다".format(num))

holzzak = ["짝수","홀수"]
for num in num_list:
    print("{}은{}이다".format(num,holzzak[num%2]))

#자리수
for num in num_list:
    print('{}은 {}자리수이다'.format(num,len(str(num))))

#아이들 고등학교
idle = {'미연':80,'민니':70,'소연':50,'우기':100,'슈화':40}
for name,score in idle.items():
    if score >= 60:
        print("{}은 합격입니다".format(name))
    else:
        print("{}은 다음 기회에~".format(name))

#range()함수
#range(시작값, 종료값, 단계)
#range(기본값 0, 종료값, 기본값 1)
print(list(range(0,10,1)))
print(list(range(10,-0,-1))) #단계값이 음수면 역순
print(list(range(0,10,5)))

print(list(range(0,10)))
print(list(range(10)))

#리스트
idle = ['미연','민니','소연','우기','슈화']
for member in idle:
    print(member)

for i in range(0,len(idle)):
    print(i+1,idle[i])

# for i,meber in enumerate(idle):
#     print(i+1.member)


#문제
a=0
for i in range(0,201,1):
    if i % 3 == 0:
        a += i
print(a)

a

sum_val = 0
for i in range(500,1000,1):
    sum_val += i
print(sum_val)

print(sum(list(range(500,1000,5))))

#sum()함수,max,min,avg
l = [1,2,3,4,5]
print(sum(l))
print(max(l))
print(min(l))

#구구단 2단
for i in range(1,9,1):
    print('2*{}={}'.format(i,2*i))

#구구단
for i in range(2,10,1):
    for j in range(1,10,1):
        print('{}x{}={}'.format(i,j,i*j))