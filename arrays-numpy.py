# # #Hi this libhary of pythin "Numpy" . From Beggineer to Advanced
# # numpy - A python libhary 

# # why we use arrays instead of list ?
# # numpy is a python libhary 
# # numpy is used for working with arryas
# # numpy is short for numerical python 
# # numpy arrays are stored at one comtinous place in memroy
# unlike lists , so process can acess and efficently
# numpy is faster than list 

# there are some reason which justify the use of numpy !

# reason1 - maths operation is easier 
import numpy as np  # type: ignore
# normal list 
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
# array with 1D 
arr = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
# list multiplication every number by 2 
print(list1 *2) # output > Repate every list 2 time [1,2,3,4,5,1,2,3,4,5]
# array : multiplication every number by 2 
print(arr * 2 ) # actually multiplay number by 2 > [ 2 4 6 8 10]
# It depends on you what you want to do with elements your usage defines what you want to use.

# reason 2 - easier elements wise opeartion 
# normal list 
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
# array with 1D 
arr = np.array([1,2,3,4,5])
arr1 = np.array([6,7,8,9,10])
# list additon of list 1 + list 2 
print(list1 + list2 ) # output > it will join list list in 1 -
#[1,2,3,4,5,6,7,8,9,10]
# array  additon of array 1 + array 2 
print(arr + arr1 ) # output will be it add elements of arr + arr1 >
# [7,9,11,13,15] > genrally at array output commas where not include 
# reason,3 - array are faster than list 
import numpy as np  # type: ignore
big_list = list (range(100000))
big_arr = np.array(range(100000))
# array opeartion are 10x - 100x are faster than list operation 
# print(big_list)
# print(big_arr)

# reason 4 - bulit in math functions 
import numpy as np # type: ignore 
score = np.array([45,88,45,99,72,89])
print(np.sum(score)) # sum operation >438
print(np.mean(score)) # average operation > 73.0
print(np.max(score)) # biggest no in element operation > 99
print(np.min(score)) # samllest element in operation > 45
print(type(score)) # ,class'numpy,ndarray'>

# when we use what ?
# use list for general storeage 
name = ["ayush", " ram", "mahesh", " ranveer"]
mixed = ["shyam", 5.6,55.15,3.14 ]
# use arrays for number and maths operation 
import numpy as np  # type: ignore 
arr = np.array([90,85,90,96])
average = np.mean(arr)
print(average) # 90.25

# keypoints - list are for staring differently type of data.
# arrays are for doing maths on numerial quickly and easiy 

