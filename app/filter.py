import numpy as np
import parsing
from scipy.signal import lfilter

#def filter(a: list[int], b: list[int], signal: parsing.Signal) -> parsing.Signal:
#    y = lfilter(a, b, signal.data)
#    return parsing.Signal(bitrate=signal.bitrate, data=np.array(y))

def filter( a: list[int], b: list[int], signal: parsing.Signal) -> parsing.Signal:
    n = len(signal.data)
    y = [0]*n
    n_a = len(a)
    n_b = len(b)
    for i in range(n):
        for j in range(n_b):
            if 0 <= i - j < n:
                y[i] += b[j] * signal.data[i-j]
        for k in range(1,n_a):
            if 0 <= i - k < n:
                y[i] -= a[k] * y[i-k] 
    
    return parsing.Signal(bitrate=signal.bitrate, data=np.array(y))
    
          
        

