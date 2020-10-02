integer=(input("Enter a number")).strip()
integer=int(integer)
series=1
print("the sum of the series is",end=' ')
for i in range(1,integer+1):
    print(series,end='')
    series=series+1
