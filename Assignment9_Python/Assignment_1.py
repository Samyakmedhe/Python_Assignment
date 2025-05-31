


def DisplayDigits(iNo):
    Digits = 0 

    if iNo <= 0:
        iNo = - iNo
    
    while(iNo != 0 ):
        Digits = iNo % 10 
        print(Digits)
        iNo = iNo // 10 
   
def main():
    
    iValue = int(input("Enter Digits : "))

    DisplayDigits(iValue)

if __name__ =="__main__":
    main()