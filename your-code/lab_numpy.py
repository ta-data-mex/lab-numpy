
#1. Import the NUMPY package under the name np.
import numpy as np
print("\n ---Ejercicio 2---\n")
#2. Print the NUMPY version and the configuration.
print("The version of numpy is: ",np.version.version)
print("The configuration of numpy is: ",np.__config__)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
print("\n ---Ejercicio 3---\n")
a= np.random.randint(0,10,(2,3,5))
a = np.random.random((2,3,5))
a = np.random.random_sample((2,3,5))
print("Se creó la variable a")
#4. Print a.
print("\n ---Ejercicio 4---\n")
print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
print("\n ---Ejercicio 5---\n")
b = np.ones((5,2,3))
print("Se creó la variable b")
#6. Print b.
print("\n ---Ejercicio 6---\n")
print(b)

#7. Do a and b have the same size? How do you prove that in Python code?
print("\n ---Ejercicio 7---\n")
print("Do a and b have the same size? ",a.size == b.size)
print("Do a and b have the same shape? ",a.shape == b.shape)

#8. Are you able to add a and b? Why or why not?
print("\n ---Ejercicio 8---\n")
try:
  print(np.add(a,b))
except:
  print("No podemos usar el método add con a y b, porque estos tienen diferentes formas (2,3,5) (5,2,3)")

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
print("\n ---Ejercicio 9---\n")
c = b.reshape(2,3,5)
print(c)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
print("\n ---Ejercicio 10---\n")
d = np.add(a,c)
print(d)
print("El ejercicio funciona debido a que ahora tienen la misma forma")

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print("\n ---Ejercicio 11---\n")
print("variable a\n")
print(a)
print("\n")
print("variable d\n")
print(d)
print(  "\n")
print("Ahora a y d tienen la misma forma y por ende, tienen el mismo número de valores")

#12. Multiply a and c. Assign the result to e.
print("\n ---Ejercicio 12---\n")
e = np.multiply(a,c)
print(e)

#13. Does e equal to a? Why or why not?
print("\n ---Ejercicio 13---\n")

print("la variable a es igual a la variable e, debido a que la variable e es la variable a multiplicada por 1")

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
print("\n ---Ejercicio 14---\n")
d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)
print("El valor máximo de d es: ",d_max)
print("El valor mínimo de d es: ",d_min)
print("El promedio de d es: ",d_mean)

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
print("\n ---Ejercicio 15---\n")
f = np.empty((2,3,5))
print(f)

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
print("\n ---Ejercicio 16---\n")

for i,x in enumerate(d):
  for j,y in enumerate(x):
    for k,z in enumerate(y):
      if z > d_min and z < d_mean:
        f[i,j,k] = 25
      if z > d_mean and z < d_max:
        f[i,j,k] = 75  
      if z == d_mean:
        f[i,j,k] = 50
      if z == d_max:
        f[i,j,k] = 100
      if z == d_min:
        f[i,j,k] = 0
print("Se rellena el array f")
print("\n ---Ejercicio 17---\n")

print(f)
