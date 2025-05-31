def CheckZero(iNo):
    Digits = 0 

    while(iNo != 0 ):
        Digits = iNo % 10 
        if (Digits == 0 ):
            return True
        iNo = iNo // 10
    else:
        return False 
   
def main():
    
    bRet = False

    iValue = int(input("Enter Digits : "))

    bRet = CheckZero(iValue)
    if bRet == True:
        print("Its Contain Zero ")
    else:
        print("there is no Zero")

if __name__ =="__main__":
    main()