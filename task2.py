import time
names=("Lebron","Kobe","Michael","Shaq","Dennis")
user=(input("Enter a name")).strip()  
count=1
for i in names:
   if i== user:
      count=count-1
      print("That name is on the list")   
   if count>=5:
      print("That name is not on the list") 
   if i!=user:
      count=count+1
      continue 
