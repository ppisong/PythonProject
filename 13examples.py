
# 23 복권 - 반복문으로 재작성
# import random
# lotto = str(random.randint(123,987)) #난수 생성
# mykey = input('복권 숫자 3자리를 입력하세요(예:123): ')
# prize = 0
#
# match = 0
# for i in range(0,3):
#    if lotto[i] == mykey[0] or lotto[i] == mykey[1] or lotto[i] == mykey[2]:
#     match +=1   # match = match +1
# if match ==3: prize = 1000000
# elif match ==2: prize =10000
# elif match ==1: prize = 1000
# result = f'''
# 당첨번호 : {lotto}
# 당신의 복권번호 : {mykey}
# 일치한 숫자 객수 : {match}
# 당첨 금액 : {prize} 원
# '''
# print(result)#

# 24 구구단 - 반복문으로 재작성

# result는 문자열로 설정
# f'==={dan}단===\n'
# dan=int(input('출력할 구구단 단수를 입력하세요(1~9)'))
# result = f'==={dan}단===\n'
# for i in range(1, 10):
#     result += f'{dan} * {i} = {dan * 1}\n'
# print(result)

#
# import random
# num = random.randint(1,100)
# result = ''
#
# for _ in range(1, 26):
#     mynum = int(input('1~100사이 숫자를 하나 입력하세요: '))
#     result = '빙고! 숫자를 맞췄습니다'
#     if num > mynum: result = '추측한 숫자가 작아요'
#     elif num < mynum: result = '추측한 숫자가 커요'
#     elif num == mynum: break
#     print(result)
#
# print(f'{num}:{result}')

# 30 구구단 테이블 -반복문으로 재작성
result = f' '

for i in range(1, 10):
    result += f'{i}|  { i*1:3d} { i*2:3d} { i*3:3d} { i*4:3d}\
             { i*5:3d} { i*6:3d} { i*7:3d} {i*8:3d} { i*9:3d}\n'
print(result)


# 32 주민번호 검사 -반복문으로 재작성
# jumin = '650101-1052323'
# sum = 0
# for i in range(0, 13):
#     if i < 6:
#        sum = sum + int(jumin[i]) * (i + 2)
#     elif 6 < i < 9:
#        sum = sum + int(jumin[i]) * (i + 1)
#     elif 8 < i < 13:
#        sum = sum + int(jumin[i]) * (i - 7)
# print(sum)
# checker = 11 - sum % 11
# print(checker, str(checker)[-1] == jumin[13])

#
#
# sum += int(jumin[1]) * 3
# sum += int(jumin[2]) * 4
# sum += int(jumin[3]) * 5
# sum += int(jumin[4]) * 6
# sum += int(jumin[5]) * 7
# sum += int(jumin[7]) * 8
# sum += int(jumin[8]) * 9
# sum += int(jumin[9]) * 2
# sum += int(jumin[10]) * 3
# sum += int(jumin[11]) * 4
# sum += int(jumin[12]) * 5