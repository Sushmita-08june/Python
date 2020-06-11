#Printing letters in pattern
button = 'c'
while button!='q':
    a = input("Enter the capital alphabet : ")
    while ord(a) not in range(65,91):
       a = input("Kindly enter capital letter :")
    Height = int(input("Enter the height which should be odd num and greater than 5 : "))
    while Height % 2 == 0 or Height<=5:
        Height = int(input("Kindly enter the height which should be odd num and greater than 5 : "))
    
    Width = Height - 2

    if a == "A":
        for row in range(Height):
            for col in range(Width):
                if ((col==0 or col==(Width-1)) and (row!=0 and row!=1)) or (col==(Width//2) and row ==0) or (row==1 and (col==1 or col==(Width-2))) or row==(Height//2):
                    print("*",end="")
                else:
                    print(end=" ")
            print()
       
    if a == "B":
        for row in range(Height):
            for col in range(Width):
                if col == 0 or (col == (Width-1) and (row!=0 and row!=(Height//2) and row!=(Height-1))) or ((row ==0 or row ==(Height//2) or row == (Height-1)) and (col>0 and col<(Width-1))):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if a == "C":
        for row in range(Height):
            for col in range(Width):
                if (col == 0 and (row!=0 and row!=(Height-1))) or ((row == 0 or row == (Height-1)) and (col<Width and col>0)):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if a == "D":
        for row in range(Height):
            for col in range(Width):
                if col == 0 or (col==(Width-1) and (row!=0 and row!=(Height-1))) or ((row == 0 or row == (Height-1)) and (col>0 and col<(Width-1))):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if a == "E":
        for row in range(Height):
            for col in range(Width):
                if col==0 or (row==0 or row ==(Height//2) or row == (Height-1)) and (col<Width):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if a == "F":
        for row in range(Height):
            for col in range(Width):
                if col == 0 or (row == 0 and col<Width) or (row ==(Height//2) and col<(Width-2)):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if a == "G":
        for row in range(Height):
            for col in range(Width):
                if (col == 0 and (row!=0 and row!=(Height-1))) or ((row==0 or row ==(Height-1)) and (col<(Width-1) and col>0)) or (col>(Width//2) and row ==(Height//2)) or (col==(Width-1) and (row!=0 and row!=((Height//2)-1) and row!=(Height-1))):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if a == "H":
        for row in range(Height):
            for col in range(Width):
                if col==0 or col==(Width-1) or (row==(Height//2) and (col<Width)):
                    print("*",end="")
                else:
                    print(end=" ")
            print()
            
    if a == "I":
        for row in range(Height):
            for col in range(Width):
                if col==(Width//2) or ((row==0 or row ==(Height-1)) and (col<Width)):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if a == "J":
        for row in range(Height):
            for col in range(Width):
                if (col==(Width//2) and row!=(Height-1)) or (row ==0 and col<Width) or (col==0 and (row>=((Height//2)+1) and row!=(Height-1))) or (0<col<=((Width//2)-1) and row==(Height-1)):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if a == "K":
        i=0
        j=Width-1
        for row in range(Height):
            for col in range(Width):
                if col==0 or ((Height//2)<row==col+2 and col>1):
                    print("*",end="")
                elif (row==i and col==j):
                    print("*",end="")
                    i=i+1
                    j=j-1
                else:
                    print(end=" ")
            print()

    if a == "L":
        for row in range(Height):
            for col in range(Width):
                if col==0 or (row==(Height-1) and col<Width):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if a == "M":
        Width = Height*2
        for row in range(Height):
            for col in range(Width):
               if (col==0 or col==Width-1) or (row==col) or row+col==(Width-1):
                   print("*",end="")
               else:
                print(end=" ")
            print()

    if a == "N":
        Width=Width+2
        for row in range(Height):
            for col in range(Width):
                if col==0 or col==(Width-1) or (row==col and col==row):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if a == "O":
        for row in range(Height):
            for col in range(Width):
                if ((col==0 or col==(Width-1)) and (row!=0 and row!=(Height-1))) or ((row==0 or row==(Height-1)) and (0<col<Width-1)):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if a == "P":
        for row in range(Height):
            for col in range(Width):
                if (col == 0 and row!=0) or (row==0 and 0<col<(Width-1)) or (0<row<(Height//2) and col==(Width-1)) or (row==(Height//2) and 0<col<(Width-1)):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if a == "Q":
        for row in range(Height):
            for col in range(Width):
                if ((col==0 or col==(Width-2)) and (row!=0 and row!=(Height-2))) or ((row==0 or row==(Height-2)) and (0<col<Width-2)) or (row==(Height-3) and col==(Width-3)) or (row==(Height-1) and 0<col>(Width-2)):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if a == "R":
        for row in range(Height):
            for col in range(Width):
                if (col == 0 and row!=0) or (col==(Width-1) and (row!=0 and row!=(Height//2))) or (row==0 and 0<col<(Width-1)) or (0<row<(Height//2) and col==(Width-1)) or (row==(Height//2) and 0<col<(Width-1)):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if a == "S":
        for row in range(Height):
            for col in range(Width):
                if (col==0 and 0<row<(Height//2)) or (row==0 and 0<col<Width) or (row==(Height//2) and 0<col<(Width-1)) or (col==(Width-1) and (Height-1)>row>(Height//2)) or (row==Height-1 and col<(Width-1)):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if a == "T":
        for row in range(Height):
            for col in range(Width):
                if (row==0 and col<Width) or (col==(Width//2) and row<Height):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if a == "U":
        for row in range(Height):
            for col in range(Width):
                if ((col==0  or col==(Width-1)) and row!=(Height-1)) or (row==(Height-1) and 0<col<(Width-1)):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if a == "V":
        Width = Height*2
        for row in range(Height):
            for col in range(Width):
               if (row==col) or row+col==(Width-1):
                   print("*",end="")
               else:
                print(end=" ")
            print()
            
    if a == "W":
        Width = (Height*2)-1
        for row in range(Height):
            for col in range(Width):
               if (col==0 or col==Width-1)  or (row+col==(Width//2)) or (col-row==(Width//2)):
                   print("*",end="")
               else:
                print(end=" ")
            print()
            
    if a == "X":
        Width = Width + 4
        for row in range(Height):
            for col in range(Width):
               if (row==col) or row+col==(Height-1):
                   print("*",end="")
               else:
                print(end=" ")
            print()

    if a == "Y":
        Width = Width + 4
        for row in range(Height):
            for col in range(Width):
               if (row==col and col<Width//2) or row+col==(Height-1):
                   print("*",end="")
               else:
                print(end=" ")
            print()

    if a == "Z":
        Width = Width + 2
        for row in range(Height):
            for col in range(Width):
               if ((row==0 or row==(Height-1)) and col<Width) or row+col==(Height-1):
                   print("*",end="")
               else:
                print(end=" ")
            print()

    
    button = input("Would you like to continue or quit, 'c' to continue and 'q' to quit : ")
