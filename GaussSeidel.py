import numpy as np

A = np.array([[5.0, 2, 1], [-1, 4, 2], [2, -3, 10]])
B = np.array([-12.0, 20, 3])
x0 = np.array([0.0, 0, 0])
x = np.array([0.0, 0, 0])
times = 0

while True:
    tempx = x0.copy()
    for i in range(3):
        temp = 0
       
        for j in range(3):
            if i != j:
                temp += x0[j] * A[i][j]
        x[i] = (B[i] - temp) / A[i][i]
        x0[i] = x[i].copy()
    catemp = abs(x-tempx)
    calTemp = max(catemp)
    times += 1
    print("x%d=%s"%(times,x))
  #  print(catemp)
    if calTemp < 1e-5:
        break
    else:
        x0 = x.copy()

print(times)
print(x)
