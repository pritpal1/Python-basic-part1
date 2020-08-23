num = int(input("Enter a number to Know it is prime or not?"))
for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
else:
    print("prime")

