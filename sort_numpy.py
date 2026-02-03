import time
import numpy as np

avg = 0
for i in range(1,11):
    file_name = str(i)
    f = open(file_name + ".inp",mode = 'r')
    n = int(f.readline())
    s = f.readline()
    a = []
    if (i <= 5):
        a = np.array(list(map(float,s.split())), dtype=np.float32)
    else:
        a = np.array(list(map(int,s.split())), dtype=np.int32)
    start = time.perf_counter()
    a.sort()
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
