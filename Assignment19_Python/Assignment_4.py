
def Frequency11(Arr, iLenght ):

    iCount = 0
    for i in range(iLenght):
        if Arr[i]  == 11 :
            iCount = iCount + 1
   
    
    return iCount

def main():
    iSize = int(input("Enter number of elements : "))

    Arr = []
    for iCnt in range(iSize):
        iValue = int(input("Enter elments : "))
        Arr.append(iValue)

    iRet = Frequency11(Arr , iSize)
    print("11 contain ",iRet,"times in it")
if __name__ == "__main__":
    main()