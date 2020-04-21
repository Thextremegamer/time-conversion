h1=int(input("Enter Taken Hours:"))
m1=int(input("Enter Taken Minute:"))
s1=int(input("Enter Taken Second:"))
h2=int(input("Enter Taken Hours:"))
m2=int(input("Enter Taken Minute:"))
s2=int(input("Enter Taken Second:"))
s3=(s1+s2)%60
m3=((m1+m2)%60)+(s1+s2)//60
h3=((h1+h2)+((m1+m2)+(s1+s2)//60)//60)
print(f"{h3}:{m3}:{s3}")
