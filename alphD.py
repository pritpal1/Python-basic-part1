for row in range(6):
    for col in range(5):
        if(row!=0 and row!= 5 and(col==0 or col==4 )) or ((row==0 or row==5) and (col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()