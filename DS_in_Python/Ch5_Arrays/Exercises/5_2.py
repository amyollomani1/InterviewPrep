import sys 
data=[]
b = 0
for k in range(10):
    if(b != sys.getsizeof(data)):
        b = sys.getsizeof(data)
        print( 'Length: {0:3d}; Size in bytes: {1:4d}'.format(k, b)) 
    data.append(None) # increase length by one
    