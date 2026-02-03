import time

def merge(a,l,mid,r):
    n1 = mid - l + 1
    n2 = r - mid
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = a[l + i]
    for i in range(n2):
        R[i] = a[mid + i + 1]
    i = 0
    j = 0
    k = l
    while (i < n1 and j < n2):
        if (L[i] <= R[j]):
            a[k] = L[i]
            i = i + 1
        else:
            a[k] = R[j]
            j = j + 1
        k = k + 1
    while (i < n1):
        a[k] = L[i]
        i = i + 1
        k = k + 1
    while (j < n2):
        a[k] = R[j]
        j = j + 1
        k = k + 1

def MergeSort(a,l,r):
    if (l < r):
        mid = (l + r) // 2
        MergeSort(a,l,mid)
        MergeSort(a,mid + 1,r)
        merge(a,l,mid,r)

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
    MergeSort(a,0,len(a) - 1)
    elapsed = time.perf_counter()
    f.close()
    f = open(file_name + ".out",mode = 'w')
    for i in range(len(a)):
        f.write(str(a[i]))
        f.write(" ")
    f.close()
    avg = avg + (elapsed-start)*1000
    print(a == sorted(a),"Done!",round((elapsed-start)*1000,4),"ms")

print("Average:",round(avg / 10.0,4))
