#Q1.
# x="a:b:c:d"
# y=x.split(":")
# print(y)
# z="#".join(y)
# print(z)

#Q2.
#1번째 방법(나-if문 활용-비효율적임)
# a={'A':90,'B':80}
# if 'k' in a.keys()==True:
#     print(a)
# else:
#     print('70')
# print(a['C'])
#2번째방법(get메소드-훨씬 간단함)
# a={'A':90,'B':80}
# print(a.get('C',70))

#Q3.둘의 차이: id-extend로 리스트 추가 하는 것이 더 효율적!
# a=[1,2,3]
# a=a+[4,5]
# # print(a)
# print(id(a))

# b=[1,2,3]
# b.extend([4,5])
# # print(b)
# print(id(b))

#Q4.리스트 내 합구하기
#1번째 방법(나-for i in A 구문-덜 효율적)
# A=[20,55,67,82,45,33,90,87,100,25]
# B=[]
# for i in A:
#     if i>=50:
#         B.append(i)
# print(sum(B))
#2번쨰 방법(답안지-while구문-더 효율적)
# A=[20,55,67,82,45,33,90,87,100,25]
# result=0
# while A:
#     mark=A.pop()
#     if mark>=50:
#         result+=mark
# print(result)

#Q5.다시해보기.....!(피보니치함수)
# def Fibonacci_numbers(n):
#     # result=[]
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#          while 2<=n<=10:
#              return Fibonacci_numbers(n)+Fibonacci_numbers(n+1)
#          print(Fibonacci_numbers(n))
# Fibonacci_numbers(5)

#Q6.리스트 내 숫자의 합
# a=input("총합을 구하는 숫자를 넣어주세요.: ")
# b=a.split(',')
# sum=0 #빼먹지 말자!!
# for i in b:
#     sum+=int(i)
# print(sum)

#Q7.구구단 만들기
# a=int(input("구구단을 출력할 숫자를 입력하세요(2~9): "))
# for n in range(1,9):
#     print(a*n,' ',end='')

#Q8.파일 수정하
# f1=open('abc.txt','r')
# lines=f1.readlines()
# f1.close()
# lines.reverse()
#
# f2=open('abc.txt','w')
# for line in lines:
#     line=line.strip()
#     f2.write(line)
#     f2.write('\n')
# f2.close()

#Q9.
# f1=open("sample.txt",'a')
# f1.write("\n")
# f1.write("40")
# f1.close()

#Q10.
# class Calculator:
#     def __init__(self,numbers):
#         self.numbers=numbers
#     def add(self):
#         result=0
#         for i in self.numbers:
#             result+=i
#         return result
#     def avg(self):
#         total=self.add()
#         return total/len(self.numbers)
#
# cal1=Calculator([1,2,3,4,5])
# print(cal1.add())
# print(cal1.avg())

#Q11.
