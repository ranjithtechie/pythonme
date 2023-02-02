def secdelmt(tupoflst):
    return tupoflst[1]
7
num=int (input ("Enter a number of tuples  "))

lst1=[]
lst2=[]
for i in range (1,num+1):
    
        

    num1=int(input("Enter the first element"))
    num2=int(input ("Enter the second element "))
    lst2.append(num2)
    lst1.append(num1)
    
     

 
tupoflst=list(zip(lst1,lst2))
print ("The entered list of tuples is ",tupoflst)
tupoflst.sort()
print("The sorted list is ",tupoflst)
option=int(input("Do you want to sort by another instance :1 for yes and 0 for no  "))

if option==0:
    print ("END")
elif   option==1:
    otoption =int(input ("How you want to sort 0 for reverse and 2 for second element"))
    if otoption==0: 
        tupoflst.sort(reverse=True)
        print(tupoflst)
    elif otoption==2:
        tupoflst.sort(key =secdelmt )
        print (tupoflst)
    else :
        print("option not applicable")
else:
    print("option not applicable")