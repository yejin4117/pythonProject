# #1)휴대전화번호 입력하면 -, /, 띄여쓰기 없애고 숫자만 풀력하자
phone_number = '010-7240-4658'
for n in phone_number:
    if n == '-' or n == '/' or n == ' ':
        continue
    print(n, end='')
print()

#>> 01072404658
print('-'*20)

#2) 학번 -> 학번,반,학과,번호 출력하기
# student_number = '2210' #2학년 2반 뉴미디어 소프트웨어과 10번
student_number = input('학번을 입력하시오 : ')
print(print(f'{student_number[0:1]}학년'))
print(print(f'{student_number[1:2]}반 뉴미디어 소프트웨어과'))
print(print(f'{student_number[2:4]}번'))

print('-'*20)

# # #3) N-sum
# # number = 331
# # #>>7
# # number = 523523
# # #>>20
#
# #4) 369게임(1~100)
# #>>1 2 짝 4 5 짝 ... 짝짝 100
# for i in range (1,101):
#     print(i)
#     if i % 3 == 0:
#         print("짝")
#     elif i % 6 == 0:
#         print("짝")
#     elif i % 9 == 0:
#         print("짝")
