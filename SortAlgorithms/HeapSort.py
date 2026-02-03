import time

def heapify(a,n,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if (l < n and a[l] > a[largest]):
        largest = l
    if (r < n and a[r] > a[largest]):
        largest = r
    if (largest != i):
        tam = a[largest]
        a[largest] = a[i]
        a[i] = tam
        heapify(a,n,largest)

def HeapSort(a,n):
    for i in range(n // 2 - 1,-1,-1):
        heapify(a,n,i)
    for i in range(n - 1,-1,-1):
        tam = a[0]
        a[0] = a[i]
        a[i] = tam
        heapify(a,i,0)

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
    HeapSort(a,len(a))
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
