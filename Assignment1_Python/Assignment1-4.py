

def Divisible(iNo):

    if iNo % 5 == 0:
        return True
    else:
        return False

def main():
    iret = 0
    iValue = int(input("Enter number : "))

    iret = Divisible(iValue)
    if iret == True:
        print(iValue,"is Divisible by 5 ")
    else:
        print(iValue,"is Not Divisible by 5 ")
    

if __name__ =="__main__":
    main()