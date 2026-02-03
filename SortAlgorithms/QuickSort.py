import time
import random

def QuickSort(a, l, r):
    pivot_idx = (l + r) // 2
    pivot = a[pivot_idx]
    i = l
    j = r
    while (i < j):
        while (a[i] < pivot):
            i = i + 1
        while (a[j] > pivot):
            j = j - 1
        if (i <= j):
            tam = a[i]
            a[i] = a[j]
            a[j] = tam
            i = i + 1
            j = j - 1
    if (i < r):
        QuickSort(a,i,r)
    if (l < j):
        QuickSort(a,l,j)

avg = 0
for i in range(1,11):
    file_name = str(i)
    f = open(file_name + ".inp",mode = 'r')
    n = int(f.readline())
    s = f.readline()
    a = []
    if (i <= 5):
        a = list(map(float,s.split()))
    else:
        a = list(map(int,s.split()))
    start = time.perf_counter()
    QuickSort(a,0,len(a) - 1)
    elapsed = time.perf_counter()
    f.close()
    f = open(file_name + ".out",mode = 'w')
    for i in range(len(a)):
        f.write(str(a[i]))
        f.write(" ")
    f.close()
    avg = avg + (elapsed-start)*1000
    print("Done!",round((elapsed-start)*1000,4),"ms")

print("Average:",round(avg / 10.0,4))
