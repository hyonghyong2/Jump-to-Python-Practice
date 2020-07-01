#Q1.
# def is_odd(a):
#     if a%2==0:
#         print("짝수입니다.")
#     else:
#         print("홀수입니다.")
#
# print(is_odd(4))

#Q2. 입력으로 들어오는 모든 수의 평균 값 계산
# def avg(*args):
#     total=0
#     for n in args:
#         total+=n
#     return total/len(args)
# print(avg(5,6))

#Q3.
# input1=int(input("첫번째 숫자를 입력하세요: "))
# input2=int(input("두번째 숫자를 입력하세요: "))
# total=input1+input2
# print("두 수의 합은 {} 입니다.".format(total))

#Q4. ,가 있는 경우 공백이 삽입됨!
# print("you" "need" "python")
# print("you"+"need"+"python")
# print("you","need","python")
# print("".join(["you","need","python"]))

#Q5.파일 open & close
# f1=open("test.txt",'w')
# f1.write("Life is too short!")
# f1.close()
#
# f2=open("test.txt",'r')
# print(f2.read())
# f2.close()

#Q6. 파일 내용 수정
# user_input=input("저장할 내용을 입력해주세요.: ")
# f1=open("test.txt",'a')
# f1.write(user_input)
# f1.wirte("\n")
# f1.close()

# f2=open("test.txt",'r')
# print(f2.read())
# f2.close()

#Q7. 파일 내용 수정
# f1=open('test.txt','w')
# f1.write("Life is too short")
# f1.write("\n")
# f1.write("you need java")
# f1.close()
#
# f2=open("test.txt",'r')
# print(f2.read())
# f2.close()
#
# f3=open("test.txt",'r')
# body=f3.read()
# f3.close
#
# body=body.replace('java','python')
#
# f4=open("test.txt",'w')
# f4.write(body)
# f4.close
