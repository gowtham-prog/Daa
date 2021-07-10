import random
import timeit
import math
import matplotlib.pyplot as pl
def partition(arr, beg, end):
    pivot=arr[end]
    left=beg
    right=end-1
    global comp
    while(1):
        while left<=right and arr[left]<=pivot:
            left+=1
            comp+=1
        while left<=right and arr[right]>=pivot:
            right-=1
        comp+=1
        if(left<right):
            arr[left], arr[right]=arr[right], arr[left]
            comp+=1
        else:
            comp+=1
            break
    arr[end], arr[left]=arr[left], arr[end]
    return left
def partition_rand(arr, beg, end):
    randpivot = random.randrange(beg, end)
    arr[end], arr[randpivot]=arr[randpivot], arr[end]
    return partition (arr, beg, end)
def quickSort(arr, beg, end):
    if beg<end:
        p=partition_rand(arr, beg, end)
        quickSort(arr, beg,p-1)
        quickSort(arr,p+1, end)
timeList=[]
compList=[]
for i in range (200):
    comp=1
    arr=[]
    for j in range(0,i):
        n = random.randint(1,100)
        arr.append(n)
    beg = timeit.default_timer()
    quickSort(arr,0,i-1)
    end = timeit.default_timer()
    total=end-beg
    timeList.append(total)
    compList.append(comp)
timelist = [x * 1000 for x in timeList]
avgtime=0
for i in timeList:
    avgtime+=i
avgtime/=200
n=[*range(1, 201, 1)]
nn=[]
for x in n:
    nn.append(math.pow(x,2))
nnn=[]
for x in n:
    nnn.append(x*math.log(x,2))
print("Time required:", avgtime)
pl.plot(compList, n, color='green', linewidth=5, label='Quicksort time')
pl.plot(nn, n, color='black', linewidth=3, label='n^2')
pl.plot(nnn,n, color='red', linewidth=3, label='nlogn')
pl.title('Quick Sort Running time')
pl.xlabel('value of time')
pl.ylabel('value of n')
pl.legend()
pl.show()

