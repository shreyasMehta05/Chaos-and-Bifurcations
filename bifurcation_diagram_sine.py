import matplotlib.pyplot as plt
import numpy as np

def logisticMap(r, x0, iterations, t_start):
    x = [x0] 
    for _ in range(iterations):
        # lets change the function to x(t+1) = r* sin(x(t))
        # x.append(r * x[-1] * (1 - x[-1]))
        x.append(r * round(np.sin(x[-1]),5))
    return x[t_start:]

r_values = np.linspace(0.0, 4.0, 1000)  # Range of r
x0 = 0.3
iterations = 1000
last = 100  #  the last 100 iterations

plt.figure(figsize=(12, 6))

for r in r_values:
    x = logisticMap(r, x0, iterations, iterations - last)
    plt.plot([r] * len(x), x, ',k', alpha=0.25) 

plt.xlabel('r')
plt.ylabel('x')
plt.title('Bifurcation Diagram of the Logistic Map')
plt.grid()
plt.text(3.5, 0.6, '2023101059', fontsize=12, color='red', ha='center', va='center', backgroundcolor='white', alpha=0.2)

plt.savefig('bifurcation_diagram_sineCurve1.png')  
plt.show()
