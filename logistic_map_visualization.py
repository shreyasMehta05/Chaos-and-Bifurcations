import matplotlib.pyplot as plt
import math as m
import numpy as np
def logisticMap(r, x0, iterations, t_start, t_end,printX=False,s=""):
    print(s)
    x = [x0] 
    mp = {}
    for _ in range(iterations):
        x.append(r * x[-1] * (1 - x[-1]))
        # mp[round(x[-1],2)] = mp.get(round(x[-1],2),0) + 1
    
    # print(mp)
    # print("len" + str(len(mp))+ " \n")
    # // sort the keys based on the values(descending order)
    # sorted_keys = sorted(mp, key=mp.get, reverse=True)
    # print(sorted_keys)
    # print(end='\n')
    x = x[t_start:t_end]
    return x

# Parameters
x0 = 0.8
iterations = 100000
list1 = logisticMap(3.5, x0, iterations, 100, 120,True,"r = 3.5")
list2 = logisticMap(3.84, x0, iterations, 100, 120,True,"r = 3.84")

plt.figure(figsize=(12, 6))
plt.plot(range(100, 120), list1, label='r = 3.5')
plt.plot(range(100, 120), list2, label='r = 3.84')
plt.xlabel('Iteration (t) for initial state (x0) = 0.8')
plt.ylabel('x')
plt.legend()
plt.title('Logistic Map for r = 3.5 and r = 3.75 (t = 100 to t = 120)')
plt.text(110, 0.5, '2023101059', fontsize=12, color='red', ha='center', va='center', backgroundcolor='white', alpha=0.2)
plt.show()
x0 = 0.8
list3 = logisticMap(3.7, x0, iterations, 100, 180,True,"r = 3.7")
plt.figure(figsize=(12, 6))
plt.plot(range(100, 180), list3, label='r = 3.7')
plt.xlabel('Iteration (t)')
plt.ylabel('x')
plt.legend()
plt.text(110, 0.5, '2023101059', fontsize=12, color='red', ha='center', va='center', backgroundcolor='white', alpha=0.2)
plt.title('Logistic Map for r = 3.7 (t = 100 to t = 180) with x0 = 0.8')
plt.savefig('logistic_map_2023101059_last1.png')
plt.show()
