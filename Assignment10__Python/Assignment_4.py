def CountRange(iNo):
    iDigits = 0 
    iMulti = 1 
    if iNo < 0:
        iNo = - iNo

    while iNo != 0:
        iDigits = iNo % 10
        iMulti = iMulti * iDigits
        iNo = iNo // 10

    return iMulti
def main():

    iValue = int(input("Enter number : "))
    iRet = CountRange(iValue)

    print("Multipilcation of all Digits : ",iRet)


if __name__ == "__main__":
    main()