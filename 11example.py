

# 21
salary = int(input('연봉을 입력하세요(만원 단위): '))
isMarried = input('결혼 여부를 입력하세요 (y:결혼, n:미혼)?').lower()
tax  = 0
rate = 0

if isMarried == 'n':   #미혼
    rate = 25          # 연봉 3000 이상시 세율
    if salary < 3000:
        rate = 10
elif isMarried == 'y': #기혼
    rate = 25          # 연봉 6000 이상시 세율
    if salary < 6000:
        rate = 10
else:
    print('성별 오류!!')

tax = salary * (rate / 100)
result = f'''
적용 세율:{rate}%
납부해야 할 세금은 {tax}만원입니다
'''

print(result)

# 23
import random
lotto = str(random.randint(123,987)) #난수 생성

mykey = input('복권 숫자 3자리를 입력하세요(예:123): ')
prize = 0
#lotto = 357
#mykey = 735

match = 0
if lotto[0] == mykey[0] or lotto[1] ==mykey[1] or lotto[0] == mykey[2]:
    match +=1   # match = match +1
if lotto[1] == mykey[0] or lotto[1] == mykey[1] or lotto[1] ==mykey[2]:
    match += 1
if lotto[2] == mykey[0] or lotto[2] == mykey[1] or lotto[2] ==mykey[2]:
    match += 1

if match ==3: prize = 1000000
elif match ==2: prize =10000
elif match ==1: prize = 1000

result = f'''
당첨번호 : {lotto}
당신의 복권번호 : {mykey}
일치한 숫자 객수 : {match}
당첨 금액 : {prize} 원
'''

print(result)

# # 26
import random

# 1~100 사이 임의의 난수 생성
num = random.randint(1,100)
# 사용자로부터 값을 하나 입력 받음
mynum = int(input('1~100사이 숫자를 하나 입력하세요: '))

result = '빙고! 숫자를 맞췄습니다!!'
if num > mynum: result = '추측한 숫자가 작아요1'
elif num < mynum: result = '추측한 숫자가 커요!'

print(f'{num}:{result}')

# 31

card_num = input('앞 6자리 카드번호를 입력하세요: ')
card_num = '11'
card_type = '식별 안됨'
card_bank = '식별 안됨'

if len(card_num) == 6:
    if card_num[:2] == '35':
        card_type = 'JBC카드'
        if card_num[2:] == '6317': card_bank = 'NH농협카드'
        elif card_num[2:] == '6901': card_bank = '신한카드'
        elif card_num[2:] == '6912': card_bank = 'KB국민카드'
        else:card_bank = "은행 정보는 등록되지 않았습니다"
    elif card_num[0] == '4':
        card_type = '비자카드'
        if card_num[1:] == '57973': card_bank = '국민은행'
        else: card_bank = "은행 정보는 등록되지 않았습니다"
    elif card_num[0] == '5':
        card_type = '마스터카드'
        if card_num[1:] == '40926': card_bank = '국민은행'
        else: card_bank = "은행 정보는 등록되지 않았습니다"
    else:card_bank = '올바른 카드 번호가 아닙니다'
else:
    card_type = '카드번호는 6자리여야 합니다'

result =f'카드 종류 및 은행: {card_type} - {card_bank}'

print(result)

# 32
#jumin = input('주민번호를 입력하세요(xxxxxx-yyyyyy)'))

jumin = '650101-1052323'
sum = 0

sum += int(jumin[0]) * 2
sum += int(jumin[1]) * 3
sum += int(jumin[2]) * 4
sum += int(jumin[3]) * 5
sum += int(jumin[4]) * 6
sum += int(jumin[5]) * 7
sum += int(jumin[7]) * 8
sum += int(jumin[8]) * 9
sum += int(jumin[9]) * 2
sum += int(jumin[10]) * 3
sum += int(jumin[11]) * 4
sum += int(jumin[12]) * 5

print(sum)

checker = 11 - sum % 11
print(checker, str(checker)[-1] == jumin[13])