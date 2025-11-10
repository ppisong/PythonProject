# 반복문
# 정해진 횟수나 조건에 따라
# 특정 코드를 반복적으로 실행하도록 만든 문장

# 만일 Hello, World!!를 1번 출력한다면?
# => print함수 1번만 사용
# print('Hello, World!!')

# 그런데 Hello, World!!를 100번 출력한다면?
# 복붙을 계속할 수 있지만 반복시 출력해야 할 문구가 바뀌면 번거로움


# print(1, end = ',')으로 10까지 반복
# while은 조건에 따라 반복, for는 횟수에 따라 반복
# # s = 0
# # while 1 <= i < 11:
#       i = i + 1
#       s = s + i
# #     print(s)


# for 반복 변수 in range 함수(시작값, 종료값, 증감값) 사용하기 :정수 시퀀스(정수열) 생성

# ex) 1 ~ 10까지 출력하기
# for i in range(1, 11):
#     print(i, end=', ')
# print('')  #end='' 초기화용 코드

# ex) Hello, World!!를 5번 출력하기
# for _ in range(1, 6): #i를 써도 되지만
#     print('Hello, World!!') #in range 앞에 부호는 횟수만 기억하는 것

# ex) 1~100사이 정수 중 3의 배수이지만 2의 배수가 아닌 정수 출력
# 또한 누적합도 계산해서 출력

# sum = 0
# for i in range(1, 101):
#     if i % 3 == 0 and i % 2 !=0:
#        sum += i
#        print(i, end=' ')
# print()
# print(sum)

# sum = 0
# for i in range(3, 101, 3):
#     if i % 2 !=0:
#       print(i, end= ' ' )
# print()
# print(sum)

# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print(sum)

i = 0
sum = 0
while 0 < i <11:
    i = i + 1
    sum = sum + i
print(sum)

# for i in range(1,101,1):
#     if i % 3 == 0 and i % 2 !=0:
#     print(i)
