def CountDiff(iNo):
    iDigits = 0 
    iSum1 = 0
    iSum2 = 0
    if iNo < 0:
        iNo = - iNo

    while iNo != 0:
        iDigits = iNo % 10
        if iDigits % 2 == 0:
            iSum1 = iSum1 + iDigits
        else:
            iSum2 = iSum2 + iDigits
        iNo = iNo // 10
    iDiff = iSum1 - iSum2

    return iDiff
def main():

    iValue = int(input("Enter number : "))
    iRet = CountDiff(iValue)

    print("Difference between Even and odd  : ",iRet)


if __name__ == "__main__":
    main()