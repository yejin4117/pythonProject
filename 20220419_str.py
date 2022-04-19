greeting = 'hello'
to = 'world!'
say_hello = greeting + ', ' + to
print(say_hello)
print(greeting * 5)
print(greeting + '\n' + to)
print("\"" + greeting + "\"")
print('\'' + greeting + '\'')
names = '''양다연
인소리
이예진
'''
print(names)

# *** indexing, slicing
#하나만 꺼내는게 indexing
# -9 -8 -7 -6 -5 -4 -3 -2 -1
#  0  1  2  3  4  5  6  7  8
names = '양다연인소리이예진'
print(names[2]) #'연'
print(names[4]) #'소'
print(names[8]) #'진'
print(names[-1]) #'진'
print(names[-2]) #'예'
print(names[-9]) #'양'
student_number = '2112'
print(student_number[0] + '학년')
print(f'{student_number[0]}학년')
print(f'{student_number[1]}반')

#slicing
#'양다연인소리이예진'
print(names[2:5])   #[2]~[4]
#연인
print(names[2:4])   #[2]~[3]
#소리이
print(names[4:7])   #[4]~[6]
#예진
print(names[7:9])   #[7]~[8]
print(f'{student_number[2:4]}번')
print(f'{student_number[-2:]}번')    #start:end-1    [start:]:끝까지
print(f'{student_number[0:2]}학년반')
print(f'{student_number[0:-2]}학년반')
print(f'{student_number[:-2]}학년반')  #start:end-1    [:end-1]:앞까지
print(f'{student_number[:]}학년반')  #start:end-1    [:]:앞~끝까지

#문자열 함수
print(f'길이: {len(student_number)}') #4
print(f'2의 개수: {student_number.count("2")}')    #2
print(f'{"idle tomboy".upper()}')
print(f'{"idle tomboy".lower()}')
s = "       idle tomboy     "
print(f'{s.strip()}')
print(f'{s.lstrip()}')
print(f'{s.rstrip()}')
print(f'{s.find("o")}') #[13]
print(f'{s.find("z")}') #없으면 -1
print(f'{s.rfind("o")}') #16
print(f'{s.index("d")}') #8
#print(f'{s.index("z")}') #없으면 ValueError: substring not found
print(f'{s.replace("tomboy"," oh my god")}')    #replace하면 바뀐 문자열을 리턴하지만 원본은 바뀌지 않음
print(s)

print('o' in s) #True
print('z' in s) #False

#split, join
ip = '10.253.123.119'
ip_list = ip.split('.')
print(ip_list)
names = '양다연, 최자윤, 임채영, 이예진, 인소리'
name_list = names.split(',')
print(name_list)
print(name_list[2]) #임채영
print(name_list[2:4]) #임채영 이예진
ip_list_str = '::'.join(ip_list)
print(ip_list_str)
name_list_str = ' | '.join(name_list)
print(name_list_str)
print(",".join(name_list))

#format
s = 'name: {}, number: {}, soccer: {}'
print(s.format('손흥민', 7, True))
s = 'name: {1}, number: {2}, soccer: {0}'
print(s.format('손흥민', 7, True))
s = 'name: {name}, number: {n}, soccer: {s}'
print(s.format(name='손흥민', s=True, n=7))
