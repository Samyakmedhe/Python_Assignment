


def check(Arr , iLenght , iNo):

    for iCnt in range(iLenght):
        if(Arr[iCnt] == iNo):
            return True
      
    return False

def main():
    
    iSize = int(input("Enter number of Elements : "))
    iNo = int(input("Enter number that you want to check : "))

    Arr = []
    for iCnt in range(iSize):
        iValue = int(input("Enter elements : "))
        Arr.append(iValue)
    
    iRet = check(Arr , iSize , iNo)
    if(iRet == True):
       print(iNo," : Number is Present")
    else:       
        print(iNo," : Number is NOT Present")
    

    
if __name__ =="__main__":
    main()