


def CircleArea(Radius):
    PI = 3.14
    Area = PI * Radius * Radius

    return Area
def main():

    fValue = 0.0
    fValue = float(input("Enter Radius : "))
    dRet = CircleArea(fValue)
    print("Area of Circle :  ",dRet)

if __name__ =="__main__":
    main()