#Q1.
# class Calculator:
#     def __init__(self):
#         self.value=0
#     def add(self,val):
#         self.value+=val
# class UpgradeCalculator(Calculator):
#     def minus(self,val):
#         self.value-=val
# cal=UpgradeCalculator()
# cal.add(10)
# cal.minus(7)
#
# print(cal.value)

#Q2.
# class Calculator:
#     def __init__(self):
#         self.value=0
#     def add(self,val):
#         self.value+=val
# class MaxLimitCalculator(Calculator):
#     def add(self,val):
#         self.value+=val
#         if self.value>100:
#             self.value=100
# cal=MaxLimitCalculator()
# cal.add(50)
# cal.add(60)
#
# print(cal.value)

#Q3. all(),chr(),ord()
# a=all([1,2,abs(-3)-3])
# print(a)
# b=chr(ord('a'))=='a'
# print(b)

#Q4.
#1번째 방법(나-if문 사용)
# a=[1,-2,3,-5,8,-3]
# result=[]
# for i in a:
#     if i>0:
#         result.append(i)
# print(result)
# #2번째 방법(답안지-filter와lambda사용)
# a=[1,-2,3,-5,8,-3]
# list(filter(lambda x:x>0,a))

#Q5. 10진수 16진수 표현
# a=hex(0xea)
# b=int(a,16)
# print(b)

#Q6.map함수
# a=[1,2,3,4]
# b=list(map(lambda x:x*3,a))
# print(b)

#Q7.
#1번째 방법(나-sort와 index사용)
# a=[-8,2,7,5,-3,5,0,1]
# a.sort()
# print(a[0]+a[-1])
#2번째 방법(답안지)
# a=[-8,2,7,5,-3,5,0,1]
# print(max(a)+min(a))

#Q8. 반올림하기
# a=17/3
# print(round(a,4))

#Q9.
# import datetime
# x=datetime.datetime("%y/%m/%d %H:%M:%S")
# print(x)

#Q13. 로또 숫자 추출하기
# import random
# list=[]
# while len(list)<=6:
#     i=random.randint(1,45)
#     list.append(i)
# list.sort()
# print(list)
