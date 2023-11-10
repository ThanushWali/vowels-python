string=input("enter the string")
count=0
st=string.lower()
for i in st:
    if(i=='a' or i=='e' or i=='o' or i=='i'or i=='u'):
        count=count+1
print(count)
