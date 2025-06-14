def CountRange(iNo):
    iDigits = 0 
    iCount = 0 
    if iNo < 0:
        iNo = - iNo

    while iNo != 0:
        iDigits = iNo % 10
        if iDigits > 3 and iDigits < 7  :
            iCount = iCount + 1
        iNo = iNo // 10

    return iCount
def main():

    iValue = int(input("Enter number : "))
    iRet = CountRange(iValue)

    print("Frequene Between 3 and 7  is : ",iRet)


if __name__ == "__main__":
    main()