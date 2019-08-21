import matplotlib.pyplot as plt
import numpy as np 


def Square():
    arr = list(map(float, input().split(',')))
    yval = list(map(float, input().split(',')))
    newarr = [i**2 for i in arr]
    print(newarr)
    
    fit = np.polyfit(newarr,yval,1)
    fit_fn = np.poly1d(fit) 

    
    m,b = np.polyfit(newarr, yval, 1)
    print("y=" +str(m) + "x + " +str(b))


    plt.plot([newarr], [yval], linewidth=2.0)
    plt.plot(newarr,yval, 'yo', newarr, fit_fn(newarr), '--k')
    plt.axis([0, max(newarr), 0, max(yval)])
    
    plt.show()


Square()