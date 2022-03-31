import numpy as np 
import matplotlib.pyplot as plt
import quimb as qu
Z = qu.gen.operators.ham_heis(6,1,0)
mag_list=[]
for h in np.linspace(0,2,20):
    H = -2*qu.gen.operators.ham_XXZ(6,h,1)
    print(H)
    E,V=np.linalg.eigh(H)
    Gs = V[:,0]
    print(E)
    mag = Gs@Z@Gs
    mag_list.append(mag)
plt.plot(np.linspace(0,2,20),mag_list)
plt.ylabel("Magnetization")
plt.xlabel("Magnetic Field")