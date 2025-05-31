
def CheckEven(iNo):
    if iNo % 2 == 0 :
        return True
    else:
        return False  

def main():

    iValue = 0
    bRet = False

    iValue = int(input("Enter number : "))
    bRet = CheckEven(iValue)
    if bRet == True :
        print(iValue,"is Even number ")
    else:
         print(iValue,"is Odd number ")

if __name__ =="__main__":
    main()
