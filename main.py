num=24
print("the table of 24 is")
for i in range(1,11):
    mul = num*i
    print(mul)


#star pattern

n=int(input("enter the number of rows "))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")1
        
    print("\n")

#while loops

num=1
sum=0
while(num<=10):
    sum= sum+num
    num= num+1
print("the total sum is" , sum)

#prime number

num=int(input("enter the number "))
flag=False
if num>1:
    for i in range(2,num):
        if(num % i==0):
            flag=True
            break

    if flag:
      print("the number is not prime")
    else:
      print("the number is prime")