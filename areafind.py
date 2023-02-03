def calculate_area(name):
   
  name= name.lower()
   
  if name=="rectangle":
    s=int (input("Enter the length of rectangle "))
    b=int(input ("Enter the breadth of rectangle "))
    print ("The area of rectangle is ",s*b)
     
    
  elif name == "square":
    s= int(input("Enter square's side length: "))
       
    sqt_area = s * s
    print("The area of square is ",
          sqt_area)
 
  elif name == "triangle":
    h = int(input("Enter triangle's height length: "))
    b = int(input("Enter triangle's breadth length: "))
       
    tri_area = 0.5 * b * h
    print("The area of triangle is",tri_area)
 
  elif name == "circle":
    r = int(input("Enter circle's radius length: "))
    pi = 3.14
         
    circ_area = pi * r * r
    print("The area of circle is ",circ_area)
         
  
     
  else:
    print("Sorry! This shape is not available")
 

   
print("Calculate Shape Area")
name = input("Enter the name of shape whose area you want to find: ")
   
calculate_area(name)