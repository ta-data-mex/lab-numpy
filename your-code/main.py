#1. Import the NUMPY package under the name np.

import numpy as np 

#2. Print the NUMPY version and the configuration.

print(np.version.version)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.randint(0,9, size=(2,3,5))

#4. Print a.

print(a)

#5. Create a 5x2x3 3-print(b.shape())dimensional array with all values equaling 1.
#Assign the array to variable "b"



b = np.ones((5,2,3), dtype = int)



#6. Print b.

print(b)
print(b.shape)



#7. Do a and b have the same size? How do you prove that in Python code?

if a.size == b.size: 
    print("Son iguales")
else:
    print("No son iguales")


#8. Are you able to add a and b? Why or why not?


print("No soy capaz porque ambos tienen diferentes dimensiones")
print(a.shape)
print(b.shape)



#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

print(c)
print(c.shape)

c = np.reshape(b, (2,3,5))

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = np.add(a,c)
print(d)
print("Lo puedo lograr el metodo add debido a que tengo dos arrays con iguales dimensiones")

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)
print(d)

print("A los valores de A fueron sumados por los valores de b original para obtener una sumatoria que es d")


#12. Multiply a and c. Assign the result to e.

e = np.multiply(a,c)
print(e)

#13. Does e equal to a? Why or why not?

if e.all() == a.all():
    print("Son iguales porque todo numero multiplicado por 1 da el mismo numero")
else:
    print("Son distintos")


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)

print(d_max)
print(d_min)
print(d_mean)


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2,3,5), int)
print(f)


#16

                

for x,ele in enumerate(d):
    for y, ele1 in enumerate(ele):
        for z, ele2 in enumerate(ele1):
            print(ele2)
            if ele2 > d_min and ele2 < d_mean:
                f[x,y,z] = 25
            if ele2 > d_mean and ele2 < d_max:
                f[x,y,z] = 75
            if ele2 == d_mean:
                f[x,y,z] = 50
            if ele2 == d_min:
                f[x,y,z] = 0
            if ele2 == d_max:
                f[x,y,z] = 100
                

            
#17
                
print(d)
print(f) 
    
#18

nueva_lista = np.empty((2,3,5), dtype=object)


for x,ele in enumerate(d):
    for y, ele1 in enumerate(ele):
        for z, ele2 in enumerate(ele1):
            print(ele2)
            if ele2 > d_min and ele2 < d_mean:
                nueva_lista[x,y,z] = "B"
            if ele2 > d_mean and ele2 < d_max:
                nueva_lista[x,y,z] = "D"
            if ele2 == d_mean:
                nueva_lista[x,y,z] = "A"
            if ele2 == d_min:
                nueva_lista[x,y,z] = "C"
            if ele2 == d_max:
                nueva_lista[x,y,z] = "E"
print(nueva_lista)

