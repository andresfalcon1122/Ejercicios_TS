import random
import numpy as np

def duplic(a, size):
    print("Repeating elements are ",
          end='')
    for i in range(0, size):
        for j in range(i + 1, size):
            if a[i] == a[j]:
                print(a[i], end=' ')

            # Driver code


a = np.random.randint(10, size=(10))
print("mi lista:",a)
arr_size = len(a)
print(arr_size)
print("mi lista:",a)
duplic(a, arr_size)
