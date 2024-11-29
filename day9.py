import numpy as np
myarr = np.array([3,4,5,5])
listarr = np.array([[2,3,5],[5,6,8],[7,8,3]])
print(listarr)
print(listarr.shape)
print(listarr.size)
rng = np.arange(16)
print(rng)

lspace = np.linspace(1,4,4)
print(lspace)

emmp = np.empty((4,6))
print(emmp)

emp_like  = np.empty_like(lspace)
print(emp_like)




