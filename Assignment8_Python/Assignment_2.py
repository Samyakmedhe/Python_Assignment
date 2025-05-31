
def RectArea(Wigth , Height):
    Area = Wigth * Height

    return Area

def main():
    
    fValue1 = float(input("Enter Wigth : "))    
    fValue2 = float(input("Enter Height : "))

    dRet = RectArea(fValue1, fValue2)
    print("Area of Rectangle : ",dRet)
    

if __name__ =="__main__":
    main()