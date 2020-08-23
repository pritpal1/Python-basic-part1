def AlphaP():
    for row in range(7):
        for col in range(5):
            if col == 0 or (col == 4 and (row == 1 or row == 2)) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
                print("*", end="")
            else:
                print(end=" ")
        print()
def AlphaR():
    for row in range(7):
        for col in range(5):
            if col == 0 or (col == 4 and (row == 1 or row == 2)) or (
                    (row == 0 or row == 3) or (row - col == 3) and (col > 0 and col < 4)):
                print("*", end="")
            else:
                print(end=" ")
        print()
def AlphaI():
    for row in range(6):
        for col in range(5):
            if ((row == 0 or row == 5)) or ((col == 2)):
                print("*", end="")
            else:
                print(end=" ")
        print()

AlphaP(),AlphaR(),AlphaI()


