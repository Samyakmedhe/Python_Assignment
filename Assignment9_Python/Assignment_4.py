def CountFour(iNo):
    iDigits = 0 
    iCount = 0 
    if iNo < 0:
        iNo = - iNo

    while iNo != 0:
        iDigits = iNo % 10
        if iDigits == 4 :
            iCount = iCount + 1
        iNo = iNo // 10

    return iCount
def main():

    iValue = int(input("Enter Number : "))
    iRet = CountFour(iValue)

    print("Frequene of 4 is : ",iRet)


if __name__ == "__main__":
    main()