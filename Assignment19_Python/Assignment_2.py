
def FrequencyEven(Arr, iLenght ):

    iCountEven = 0
    iCountOdd = 0
    for i in range(iLenght):
        if Arr[i] %  2 == 0 :
            iCountEven = iCountEven + 1 
        else:
            iCountOdd = iCountOdd + 1 
    
    iDiff = iCountEven - iCountOdd
    return iDiff
    

def main():
    iSize = int(input("Enter number of elements : "))

    Arr = []
    for iCnt in range(iSize):
        iValue = int(input("Enter elments : "))
        Arr.append(iValue)

    iRet = FrequencyEven(Arr , iSize)
    print("Result is : ",iRet)

if __name__ == "__main__":
    main()