class MixedClass():
    def Subfields():
    print("Sub-fields in AI are:")
    print("Machine Learning")
    print("Neural Network")
    print("Vision")
    print("Robotics")
    print("Speech Processing")
    print("Natural langauge processing")


    def OddEven():
    num=int(input("Enter the Number:"))
    if (num%2 != 0):
        print(num, "is Odd Number")
        val = f"{num } is a Odd Number"
    else:    
        print("is Even Number")
        val = f"{num } is a Even Number"
    return val


  def Marriage(gender,age):
    if (gender.lower() == "male" and age <=20):
        print("Your Gender:", gender)
        print("Your Age:", age)
        print("NOT ELIGIBLE")
        val = "NOT ELIGIBLE"
    elif (gender.lower() == "female" and age <=17):
        print("Your Gender:", gender)
        print("Your Age:", age)
        print("NOT ELIGIBLE")
        val = "NOT ELIGIBLE"    
    else:    
        print("ELIGIBLE")
        val = "ELIGIBLE"    
    return val

  def FindPercentage():
    sub1=int(input("Subject1="))
    sub2=int(input("Subject2="))
    sub3=int(input("Subject3="))
    sub4=int(input("Subject4="))
    sub5=int(input("Subject5="))
    tot = sub1+sub2+sub3+sub4+sub5
    print("Total :", tot)
    Percentage = tot / 5
    print("Percentage :", Percentage)
    return Percentage

  def triangle():
    height =int(input("Height:"))
    breadth =int(input("Breadth:"))
    print("Area Formula: (Height*Breadth)/2")
    Area = (height*breadth)/2
    print("Area of Triangle:",Area)
    height1 =int(input("Height1:"))
    height2 =int(input("Height2:"))
    breadth =int(input("Breadth:"))
    print("Perimeter Formula: Height1+Height2+Breadth")
    Peri = height1+height2+breadth
    print("Perimeter of Triangle:",Peri)