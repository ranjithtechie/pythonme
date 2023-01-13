heightlist =[]
nem =int (input ("enter the number of persons "))
count =0
while nem==nem :
  if  count<nem:
    
    height=int (input ("enter your height "))
    count +=1
    heightlist.append(height)
    continue
  else :
    break
  
print (heightlist)

sumof   = sum(heightlist)
    
print (sumof )
print (sumof/len(heightlist))