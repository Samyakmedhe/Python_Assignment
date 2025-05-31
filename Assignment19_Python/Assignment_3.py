
def Check11(Arr, iLenght ):

    for i in range(iLenght):
        if Arr[i]  == 11 :
            return True
    else:
        return False
    
    print()

def main():
    iSize = int(input("Enter number of elements : "))

    Arr = []
    for iCnt in range(iSize):
        iValue = int(input("Enter elments : "))
        Arr.append(iValue)

    bRet = Check11(Arr , iSize)
    if bRet == True:
        print("Its contain 11 in it")
    else:
        print("there is no 11")

if __name__ == "__main__":
    main()