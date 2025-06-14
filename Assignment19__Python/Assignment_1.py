
def FrequencyEven(Arr, iLenght ):

    iCount = 0
    for i in range(iLenght):
        if Arr[i] %  2 == 0 :
            iCount = iCount + 1 
    return iCount
    

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