integer=input(("Enter a number")).strip()
integer=int(integer)
factorial=1
for i in range(1,integer+1):
    factorial= factorial*i
print(str(integer)+"! is "+str(factorial))

