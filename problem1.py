box=(input("Enter width/height of box")).strip()
box=int(box)
for i in range(0,box):
    if i<box:
        print("*",end='')
        print("*"*box)
