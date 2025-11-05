# 실습시 고정폭 글꼴을 사용할 것!!
print('*   *   **   ****   ****  *   *')
print('*   *  *  *  *   *  *   * *   *')
print('***** *    * ****   ****   * * ')
print('*   * ****** *  *   *   *   *  ')
print('*   * *    * *   *  *    *  *  ')

print('   /////')
print('  | o o |')
print(' (|  ^  |)')
print('  | [_] | ')
print('   -----')

print('            +---+')
print('            |   |')
print('        +---+---+')
print('        |   |   |')
print('    +---+---+---+')
print('    |   |   |   |')
print('---+---+---+---+')
print('|   |   |   |   |')
print('+---+---+---+---+')

print('        /\_/\      ____')
print("       ( ' ' )    /hello\ ")
print('       (  -  )   < Junior|')
print('        | | |     \Coder!/')
print('       (__|__)      ____')

# 이름 몸무게 나이를 변수로 선언하고 초기화하는 문장
# ctrl + bar,
name = '송평인'
weight = 74
age = 60
print(name, weight, age)

# 표현식 연습
x, y, z = 10, 20, 30
print(3 * x)
print(3 * x + y)
print((x + y)/ 7)
print(((3 * x) + y)/(z + 2))

# c언어와 달리 정수를 정수로 나눠도 알아서 실수로 출력
# 정확한 연산이 필요할 경우엔 수학 관련 라이브러리 사용해야 함
number = (1 / 3) * 3
print(number, 1 / 3, (1 / 3 ) * 3)

print(7 / 3)
print(7 // 3)
print(7 % 3)

result = 11
result /=2  #복합연산자(순서 때문에 이런 모습)
print(result)

x = 2.5; y = -1.5; m = 18; n =4 # x , y, m, n =2.5, -1.5, 18, 4
print(x + n * y - (x + n) * y)
print(m / n + m % n)
print(5 * x - n / 5)
print(1 - (1 - (1 - (1 - n))))