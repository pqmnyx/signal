import parsing

def filter( a: list[int], b: list[int], signal: parsing.Signal) -> parsing.Signal:
    n = len(signal.data)
    y = [0]*n
    n_a = len(a)
    n_b = len(b)
    for i in range(n):
        for j in range(n_b):
            if 0 <= n - j < n:
                y[i] += b[j] * signal.data[n-j]
        for k in range(1,n_a):
            if 0 <= n - k < n:
                y[i] -= a[k] * y[n-k] 
    return parsing.Signal(bitrate=signal.bitrate, data=y)
    
          
        

