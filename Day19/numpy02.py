import numpy as np
arr = np.arange(10)
print(arr)
print(arr[5])
print(arr[5:8])
arr[5:8] = 12
print(arr)
print(arr[:])
arr2d = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]])
print(arr2d)
print(arr2d[2,:])
print(arr2d[1:3,:])
print(arr2d[:,3])
print(arr2d[:,:2])
print(arr2d[3,2])
arr2d[:2,1:3] = 0
print(arr2d)

names = np.array(["kim" , "park" , "ha" , "joe" , "kim"])
data = np.random.rand(5,3)
print(names)
print(data)

print(data[names=="kim",:])
print(data[names=="ha",:])
print(data[:,1] < 0.5)
## print(data[data[:,1] <0.5, : ])##
data[data[:,0] < 0.5 , : ] = 0
print(data)
data[data[:,0] < 0.5 , 1] = 10
print(data)


