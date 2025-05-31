def Display(iNo):
    
    if iNo == 1:
        print("One")
    elif iNo == 2:
        print("Two")
    elif iNo == 3:
        print("Three")
    elif iNo == 4:
        print("Four")      
    elif iNo == 5:
        print("Five")
    elif iNo == 6:
        print("Six")
    elif iNo == 7:
        print("Seven")
    elif iNo == 8:
        print("Eight")
    elif iNo == 9:
        print("Nine")
    else:
        print("Invalid number ...")

def main():
    
    iValue = int(input("Enter number : "))
    Display(iValue)

    
if __name__ =="__main__":
    main()