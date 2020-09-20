


def play(a,b,arr):
    count=0
    for i in range (0,b):
        print(arr[0][i],end=" ")
    for i in range(1,b):
        print()
        print(arr[i][b-1],end=" ")
    for i in  range(a-2,-1):
        print()
        print(arr[a-1][i],end=" ")
    for i in range(b-2,0):
        print()
        print(arr[b-1][i],end=" ")
    for i in range(2,b-2):
        print()
        print(arr[1][i],end=" ")
    for i in range (2,a-2):
        print()
        print(arr[a-2][i],end=" ")
    print(arr[2][1],end=" ")
    




row=int(input("Enter the no. of rows: "))
column=int(input("Enter the mo. of columns: "))
count=1
arr=[]
for  i in range (0,row):
    l=[]
    for j in range (0,column):
        l.append(count)
        count=count+1
    arr.append(l)
print(arr)
play(row,column,arr)
