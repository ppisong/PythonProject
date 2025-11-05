

# 문자열 포매팅 사용하기 전
say = 'World'
print('Hello,' + say + '~!!')
say = 'Python'
print('Hello,' + say + '~!!')

# 문자열 포매팅 1 - %
print('Hello,%s~!!' % say)
# %s외의 다른 코드를 미리 알아야 하는 불편함
name, weight, age = '홍길동', 74.3, 60
print('이름 : %s, 몸무게 : %.1fkg, 나이: %d세' % (name, weight, age))

# 문자열 포매팅 2 - .format
print('Hello,{0}~!!'.format(say))
print('이름 :{0}, 몸무게 :{1:.2f}kg, 나이: {2}세'.format(name, weight, age))
print('이름 :{}, 몸무게 :{:.2f}kg, 나이: {}세'.format(name, weight, age))

# 문장열 포매팅 3 -f포매팅
print(f'Hello,{say}~!!')
print(f'이름 :{name}, 몸무게 :{weight:.2f}kg, 나이: {age}세')
