# 성적 처리프로그램 V1
# 이름 국어 영어 수학 점수를 변수로 설정
# 총점 평균 학점을 처리한 뒤 결과 출력
# 단 학점은 삼항연산자를 이용해서 계산한다
# 변수 = 참일 때 값 if 조건식 else 거짓일 때 값

# 입력
# 이름 국어 영어 수학 점수를 변수로 설정
name, lang, eng, math, sum, avr = '김민수', 99, 99, 98, 0, 0

# 성적 처리
# 총점 평균 학점을 처리
sum = lang + eng + math
avr = sum / 3
# result = 'A' if (avr >= 90) else 'B'
# result = 'C' if (70 <= avr < 80) else 'D'
# result = 'F' if  avr >==70

grd = ('A' if (avr >=90) else
       'B' if (avr >=90) else
       'C' if (avr >=70) else
       'D' if (avr >=60) else 'F')


# 결과 출력
# 이름 국어 영어 수학 총점 평균 학점 출력
print('총점 :',sum)
print('평균 :',avr)
print('학점 :',grd)

