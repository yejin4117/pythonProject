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

