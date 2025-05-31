def Display(iNo):
    iRupees = 70

    iRupees = iRupees * iNo
    return iRupees


def main():
    
    iValue = int(input("Enter number : "))
    iRet = Display(iValue)
    print("Value in INR is : ",iRet)

    
if __name__ =="__main__":
    main()