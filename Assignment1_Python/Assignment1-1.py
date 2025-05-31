

def Divide(iNo1 , iNo2):
    if iNo1 <= 0:
        return "Wronge Input"
    else:
        idiv = iNo1 // iNo2
    return idiv

def main():
    iRet = 0
    iValue1 = int(input("Enter first number : "))
    iValue2 = int(input("Enter Second number : "))

    iRet = Divide(iValue1 ,iValue2)
    print("Division is : ",iRet)

if __name__ == "__main__":
    main()
