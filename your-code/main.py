#1. Import the NUMPY package under the name np.
import numpy as np


#2. Print the NUMPY version and the configuration.
print(np.version.version)
1.17.2


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a = np.random.random((2,3,5))

#Segunda manera de generar random arrays 
np.array((2,3,5))

#4. Print a.

print(a)

[[[0.87518155 0.97160302 0.74320166 0.52388431 0.23212673]
  [0.49494077 0.0479125  0.93681344 0.1634494  0.83706916]
  [0.21275378 0.11567146 0.85040991 0.89222066 0.22173655]]

 [[0.66351454 0.39961527 0.74214677 0.09326884 0.98651048]
  [0.34882669 0.88676666 0.80927674 0.69553686 0.43548238]
  [0.90895205 0.92070078 0.15513116 0.09261683 0.75755615]]]

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))


#6. Print b.

print(b)

[[[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]]
#7. Do a and b have the same size? How do you prove that in Python code?

print(a.size)
print(b.size)

30
30

#8. Are you able to add a and b? Why or why not?

#No se pueden agregar porque no tienen la misma forma 

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = np.reshape(b,(2,3,5))
print(c)

[[[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]

 [[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]]


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = np.add(a,c)
print(d)

[[[1.87518155 1.97160302 1.74320166 1.52388431 1.23212673]
  [1.49494077 1.0479125  1.93681344 1.1634494  1.83706916]
  [1.21275378 1.11567146 1.85040991 1.89222066 1.22173655]]

 [[1.66351454 1.39961527 1.74214677 1.09326884 1.98651048]
  [1.34882669 1.88676666 1.80927674 1.69553686 1.43548238]
  [1.90895205 1.92070078 1.15513116 1.09261683 1.75755615]]]

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

#Los dos arreglos son iguales porque tienen la misma forma es un arreglo de 3 dimensiones con 30 elementos. 
print(a)
print(d)

[[[0.87518155 0.97160302 0.74320166 0.52388431 0.23212673]
  [0.49494077 0.0479125  0.93681344 0.1634494  0.83706916]
  [0.21275378 0.11567146 0.85040991 0.89222066 0.22173655]]

 [[0.66351454 0.39961527 0.74214677 0.09326884 0.98651048]
  [0.34882669 0.88676666 0.80927674 0.69553686 0.43548238]
  [0.90895205 0.92070078 0.15513116 0.09261683 0.75755615]]]
[[[1.87518155 1.97160302 1.74320166 1.52388431 1.23212673]
  [1.49494077 1.0479125  1.93681344 1.1634494  1.83706916]
  [1.21275378 1.11567146 1.85040991 1.89222066 1.22173655]]

 [[1.66351454 1.39961527 1.74214677 1.09326884 1.98651048]
  [1.34882669 1.88676666 1.80927674 1.69553686 1.43548238]
  [1.90895205 1.92070078 1.15513116 1.09261683 1.75755615]]]

#12. Multiply a and c. Assign the result to e.

e = np.multiply(a, c) 
print(e)
[[[0.87518155 0.97160302 0.74320166 0.52388431 0.23212673]
  [0.49494077 0.0479125  0.93681344 0.1634494  0.83706916]
  [0.21275378 0.11567146 0.85040991 0.89222066 0.22173655]]

 [[0.66351454 0.39961527 0.74214677 0.09326884 0.98651048]
  [0.34882669 0.88676666 0.80927674 0.69553686 0.43548238]
  [0.90895205 0.92070078 0.15513116 0.09261683 0.75755615]]]

#13. Does e equal to a? Why or why not?
print(a)
print(e)
[[[0.87518155 0.97160302 0.74320166 0.52388431 0.23212673]
  [0.49494077 0.0479125  0.93681344 0.1634494  0.83706916]
  [0.21275378 0.11567146 0.85040991 0.89222066 0.22173655]]

 [[0.66351454 0.39961527 0.74214677 0.09326884 0.98651048]
  [0.34882669 0.88676666 0.80927674 0.69553686 0.43548238]
  [0.90895205 0.92070078 0.15513116 0.09261683 0.75755615]]]
[[[0.87518155 0.97160302 0.74320166 0.52388431 0.23212673]
  [0.49494077 0.0479125  0.93681344 0.1634494  0.83706916]
  [0.21275378 0.11567146 0.85040991 0.89222066 0.22173655]]

 [[0.66351454 0.39961527 0.74214677 0.09326884 0.98651048]
  [0.34882669 0.88676666 0.80927674 0.69553686 0.43548238]
  [0.90895205 0.92070078 0.15513116 0.09261683 0.75755615]]]



#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = d.max()
d_min = d.min()
d_mean = d.mean()

print(d_max)

print(d_min)

print(d_mean)

1.9865104765777961
1.0479125005961147
1.5671625702060197

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty([2,3,5])


for i, a in enumerate(d):
    for j, b in enumerate(a):
        for k, c in enumerate(b):
            if c == d_min:
                f[i][j][k] = 0
            elif c > d_min and c < d_mean:
                f[i][j][k] = 25
            elif c == d_mean:
                f[i][j][k] = 50
            elif c > d_mean and c < d_max:
                f[i][j][k] = 75
            elif c == d_max:
                f[i][j][k] =100 

print(f)

[[[ 75.  75.  75.  25.  25.]
  [ 25.   0.  75.  25.  75.]
  [ 25.  25.  75.  75.  25.]]

 [[ 75.  25.  75.  25. 100.]
  [ 25.  75.  75.  75.  25.]
  [ 75.  75.  25.  25.  75.]]]



"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""


"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""