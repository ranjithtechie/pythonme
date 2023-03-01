import matplotlib.pyplot as plt
import math
degree = 0
for i in range(91):
    value = (complex(math.cos((math.pi*degree)/180), math.sin((math.pi*degree)/180))) * (complex(4, 0))
    print(value)
    x = value.real
    y = value.imag
    q1 = [0,x] #coordinate of x1,x2
    q2 = [0,y] #coordinate of y1,y2
    plt.xlim(0, 5) #limit of x
    plt.ylim(0, 5) #limit of y
    plt.plot(q1, q2, marker="o", markersize=20, markeredgecolor="pink", markerfacecolor="blue")
    plt.draw()
    plt.pause(0.01)
    plt.clf()
    degree=degree+1
