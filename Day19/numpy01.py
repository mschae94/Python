import numpy as np #
import pandas
data1 = [6 , 5 , 4.4 , 3 , 10 , 2 , 1]
arr1 = np.array(data1)
print(arr1)
print(arr1.shape)
data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2) # 행열을 만들어준다!!!!
print(arr2)
print(arr2.shape)
print(np.zeros((3,5)))
print(np.ones((2,4)))
print(np.arange(15))
print(arr1.dtype) #float 실수 64 저장할수있는크기
print(arr2.dtype) #정수 32
arr3 = np.array([1,2,3,4,5], dtype = np.int64)
print(arr3)
print(arr3.dtype)
float_arr1 = arr3.astype(np.float64)
print(float_arr1)
print(float_arr1.dtype)
# 천만개 (1900~2000 )영화 평점 6400명이
# 손 , 삽 (엑셀), 포크레인 (파이선)
arr4 = np.array([[1,2,3],[4,5,6]])
arr5 = np.array([[6,7,2],[5,2,1]])
print(arr4*arr5)







