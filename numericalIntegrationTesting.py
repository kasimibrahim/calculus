import math      #Allows the code to solve equations that contains expressions from the math library

def main():
    file = printIntro() #Introduction ,records the file report name
    lowerLimit, upperLimit, No_shapes, deltaX, isNegative = deltaXfunction() #Records the values required for the approximation
    fxi_values, loop_equation, outfile = yvalues(float(lowerLimit), float(upperLimit), No_shapes, deltaX, file) #Making substitution of x values to get y values
    approximations(fxi_values, deltaX, outfile, isNegative) #User makes choice here: Riemann, Trapezium or Simpson
    

def printIntro():
    print("This program calculates the approximate area under curves")
    print("using Riemann, Simpson, or Trapezoid method")
    print()
    file = input("You will also receive a report on the approximation.\nEnter the name of the report file (include .txt): ")
    while file == "":
        print("Invalid input")
        file = input("Enter the name of the report file (include .txt): ")
    return file;
    
            
def deltaXfunction():
    isNegative = False
    
    is_a_symbol = True
    while is_a_symbol:
        try:
            lowerLimit = input("Enter lower limit value: ")
            while lowerLimit.isalpha() and not lowerLimit.isnumeric():
                print("Invalid input")
                lowerLimit = input("Enter lower limit value: ")
            lowerLimit = float(lowerLimit)
            is_a_symbol  = False
        except ValueError as ve:
            print("Invalid Input. Lower limit should be a number")
        
    is_a_symbol = True
    while is_a_symbol:
        try:
            upperLimit = input("Enter upper limit value: ")
            while upperLimit.isalpha() and not lowerLimit.isnumeric():
                print("Invalid input. Upper Limit must be a number")
                upperLimit = input("Enter upper limit value: ")
            upperLimit = float(upperLimit)
            is_a_symbol = False
        except ValueError as ve:
            print("Invalid input. Upper Limit must be a number")
    
    if  lowerLimit > upperLimit:
        lowerLimit, upperLimit = upperLimit, lowerLimit
        isNegative = True   #When the lowerLimit is greater than the upper limit, Area must be negative

    is_a_symbol = True
    while is_a_symbol:
        try:
            No_shapes = input("How many shapes will you use: ")
            while No_shapes.isalpha() or not No_shapes.isdecimal():
                print("Invalid input. Input must be a whole number")
                No_shapes = input("How many shapes will you use: ")
            No_shapes = float(No_shapes)
            is_a_symbol = False
        except ValueError as ve:
            print("Invalid input. Input must be a whole number")
            
    No_shapes = float(No_shapes)
    deltaX = (upperLimit - lowerLimit) / No_shapes
    return lowerLimit, upperLimit, No_shapes, deltaX, isNegative


def yvalues(lowerLimit, upperLimit, No_shapes, deltaX, file):
    outfile = open(file, "w")
    print("         ", file.upper(),"\n", file= outfile)

    print("Recorded values: \n", "Lower limit:", lowerLimit,"\n","Upper limit:",upperLimit)
    print(" Number of sections(shapes):",No_shapes,"\n", "Width of each section/shape:",deltaX)

    print("Recorded values: \n", "Lower limit:", lowerLimit,"\n","Upper limit:",upperLimit, file= outfile)
    print(" Number of sections(shapes):",No_shapes,"\n", "Width of each section/shape:",deltaX, file= outfile)           

    equation = input("Input equation: ")

    print("\n                 x", "                       ", "  f(x)  \n ------------------------------------------------------------------------")
    print("\n                 x", "                       ", "  f(x)  \n ------------------------------------------------------------------------", file = outfile)    
    
    loop_equation = equation
    me = list(equation)
    fxi_values = []
    interval = ""
    height = ""
    write_next_fx_value = 0
    numbering = 1
    
    while lowerLimit <= upperLimit:
        index = equation.count('x')
        me  = list(equation)
        ##will try if replace can work here: equation.replace('x',str(lowerlimit))...then eval(equation).....then fxi_values.append(eval(equation))
        for ch in range(len(equation)):
            if index > 0:
                if equation[ch] == 'x':
                    me.remove('x')
                    me.insert(ch, str(lowerLimit))
                    index -= 1

        strheight = height.join(me)
        height_value = eval(strheight)
        fxi_values.append(height_value)
        
        print("{3:>4}{2:>12}{0:<19,}{1:>18,}".format(round(lowerLimit,4),round(fxi_values[write_next_fx_value],4),interval,numbering), file = outfile)
        print("{3:>4}{2:>12}{0:<19,}{1:>18,}".format(round(lowerLimit,4),round(fxi_values[write_next_fx_value],4),interval, numbering))
        
        lowerLimit = lowerLimit + deltaX
        write_next_fx_value += 1
        numbering += 1
    return fxi_values, loop_equation, outfile

def riemann(fxi_values, deltaX, outfile, isNegative):
    fxi_area = []
    l_or_r = input("Press l for left riemann or r for right riemann: ")
    

    while l_or_r[0] != "l" and l_or_r[0] != "L" and l_or_r[0] != "r" and l_or_r[0] != "R":
        print("Invalid input")
        l_or_r = input("Press l for left riemann or r for right riemann: ")
        
    if l_or_r[0] == "r" or l_or_r[0] == "R":
        riemannArea = 1 * (sum(fxi_values) - fxi_values[0]) * deltaX
    elif l_or_r[0] == "l" or l_or_r[0] =="L":
        riemannArea = 1 * (sum(fxi_values) - fxi_values[len(fxi_values)-1]) * deltaX

    if isNegative:
        riemannArea = -1 * riemannArea
        print("Riemann approximation: " , round(riemannArea,4), file = outfile)
        print("Approximate integral will be negative since upper limit is", file = outfile)
        print("smaller than lower limit. Therefore read values from bottom", file = outfile)
        print(riemannArea)
        outfile.close()
    
    else:
        print("Riemann approximation: " , round(riemannArea,4), file = outfile)
        print(riemannArea)
        outfile.close()
        
    return riemannArea

                                                                                        
def trapezoid(fxi_values, deltaX, outfile, isNegative):                                 
    trapezoidArea = 0
    if len(fxi_values) != 2:
        for each_value in range(1, len(fxi_values)-1):
            trapezoidArea += fxi_values[each_value]
    trapezoidArea = 0.5*(fxi_values[0] + 2*trapezoidArea + fxi_values[-1])*deltaX
    
    if isNegative:
        print("Trapezium approximation: " , round(-1 * trapezoidArea, 4), file = outfile)
        print("Approximate integral will be negative since upper limit is", file = outfile)
        print("smaller than lower limit. Therefore read values from bottom", file = outfile)
        outfile.close()
        print(trapezoidArea)
        return trapezoidArea
    else:
        print("Trapezium approximation: " , round(trapezoidArea, 4), file = outfile)
        outfile.close()
        print(trapezoidArea)
        return trapezoidArea

def simpsons(fxi_values, deltaX, outfile, isNegative):
    
    simpsonArea = 0
    for each_value in range(1, len(fxi_values)-1):
        if each_value % 2 == 0:
            simpsonArea += 2 * fxi_values[each_value]
        else:
            simpsonArea += 4 * fxi_values[each_value]
    
    if isNegative:
        simpsonArea = -1*(1/3 * deltaX * (fxi_values[0] + simpsonArea + fxi_values[-1]))
        print("Simpson approximation: " , round(simpsonArea,4), file = outfile)
        print("Approximate integral will be negative since upper limit is", file = outfile)
        print("smaller than lower limit. Therefore read values from bottom", file = outfile)
        outfile.close()
        print(simpsonArea)
        return simpsonArea
    else:
        simpsonArea = 1/3 * deltaX * (fxi_values[0] + simpsonArea + fxi_values[-1])
        print("Simpson approximation: " , round(simpsonArea,4), file = outfile)
        outfile.close()
        print(simpsonArea)
        return simpsonArea
    
def approximations(fxi_values, deltaX, outfile, isNegative):
    choice = input("Which approximation do you wish to use: \n1. Riemann\n2. Trapezuim\n3. Simpsons\n>> ")
    if choice == "1":
       riemannArea = riemann(fxi_values, deltaX, outfile, isNegative)
    elif choice == "2":
        trpazoidArea = trapezoid(fxi_values, deltaX, outfile, isNegative)
    elif choice == "3":
        simpsonsArea  = simpsons(fxi_values, deltaX, outfile, isNegative)
    else:
        print("\nInvalid choice\n")
        approximations(fxi_values, deltaX, outfile, isNegative)

    
if __name__ == "__main__": main()
            
        
