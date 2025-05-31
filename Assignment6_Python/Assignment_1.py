def Number(iNo):
    
    if(iNo < 50):
        print("Small")
    elif iNo > 50 and iNo < 100:
        print("Medium")
    else:
        print("large")
    
    
def main():
    
    iValue = int(input("Enter number : "))
    Number(iValue)

    
if __name__ =="__main__":
    main()