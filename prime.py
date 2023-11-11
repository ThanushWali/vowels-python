num1=int(input("enter the 1st number:"))
num2=int(input("enter the 2nd number:"))
for num in range(num1,num2+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
                print(num)
