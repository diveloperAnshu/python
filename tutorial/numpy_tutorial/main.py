import numpy as np
from time import process_time

# python_list=[i for i in range (1000)]
# start_time=process_time()
# python_list=[i+5 for i in range(1000)]
# end_time=process_time()
# print(end_time-start_time)

# np_array=np.array([i for i in range(1000)])
# start_time=process_time()
# np_array+=5
# end_time=process_time()
# print(end_time-start_time) 


a=np.array([1,2,3,4])
print(a)

b=np.array([(1,2,3,4),(3,4,5,6)])
print(b)
print(b.shape)
print(type(b))






c=np.array([(1.2,4,7,8),(1,3,8.9,7)])
print(c.shape)
print(c)





#  create a numpy array with initial valeue as zero
x=np.zeros((4,5),dtype=int)
print(x)


y=np.ones((3,4),dtype=int)
print(y)

# array with a particular value
z=np.full((4,5),0)
print(z)


# create identity matrix;

array=np.eye(4,dtype=int)
print(array)




# create a np array with random values between 10 and 100 only 10 included
aa=np.random.randint(10,100,(3,4))
print(aa)




#  list to np array

list1=[1,2,3,4]
np_array=np.asarray(list1)
print(np_array)


# (.ndim) is used to find the dimension of the np array

 
