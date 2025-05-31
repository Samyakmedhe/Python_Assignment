def CountTwo(iNo):
    iDigits = 0 
    iCount = 0 
    if iNo < 0:
        iNo = - iNo

    while iNo != 0:
        iDigits = iNo % 10
        if iDigits == 2 :
            iCount = iCount + 1
        iNo = iNo // 10

    return iCount
def main():

    iValue = int(input("Enter Number : "))
    iRet = CountTwo(iValue)

    print("Frequene of 2 is : ",iRet)


if __name__ == "__main__":
    main()