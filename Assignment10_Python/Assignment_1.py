def CountEven(iNo):
    iDigits = 0 
    iCount = 0 
    if iNo < 0:
        iNo = - iNo

    while iNo != 0:
        iDigits = iNo % 10
        if iDigits % 2  == 0 :
            iCount = iCount + 1
        iNo = iNo // 10

    return iCount
def main():

    iValue = int(input("Enter Number : "))
    iRet = CountEven(iValue)

    print("Frequene of Even Digits is : ",iRet)


if __name__ == "__main__":
    main()