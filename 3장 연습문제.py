#Q1.
# a="Life is too short, you need python"
# if "wife" in a:
#     print("wife")
# elif "python" in a and "you"not in a :
#     print("python")
# elif "shirt"not in a:
#     print("shirt")
# elif "need" in a:
#     print("need")
# else:
#     print("none")

#Q2. 1~1000까지 3의배수 합 구하기
# result=0
# a=1
# while a<1000:
#     if a%3==0:
#         result+=a
#     a+=1
# print(result)

#Q3.* 한 개씩 늘려가며 프린트하기
# n=1
# while n<=5:
#     print('*'*n)
#
#     n+=1

#Q4. for문 이용하여 1~100까지 출력하기
# a=0
# for a in range(1,101):
#     print(a)
#     a+=1

#Q5. for문 사용하여 평균 구하기
# a=[70,60,55,75,95,90,80,85,100]
# total=0
# for score in a:
#     total+=score
# average=total/len(a)
# print(int(average))

#Q6.홀수에만 2를 곱하여 리스트에 저장
# numbers=[1,2,3,4,5]
# result=[]
# for n in numbers:
#     if n%2==1:
#         result.append(n*2)
# print(result)
