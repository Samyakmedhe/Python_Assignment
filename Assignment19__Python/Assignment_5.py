
def Frequency11(Arr, iLenght, ifind ):

    iCount = 0
    for i in range(iLenght):
        if Arr[i]  == ifind :
            iCount = iCount + 1
   
    
    return iCount

def main():
    iSize = int(input("Enter number of elements : "))
    iNo = int(input("Enter number you want find : "))
    Arr = []
    for iCnt in range(iSize):
        iValue = int(input("Enter elments : "))
        Arr.append(iValue)

    iRet = Frequency11(Arr , iSize, iNo)
    print(iNo,"contain ",iRet,"times in it")
if __name__ == "__main__":
    main()