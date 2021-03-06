import numpy as np
import matplotlib.pyplot as plt

mid=np.array([80, 70, 60, 90])
avg=mid.mean()
var=mid.var()
sd=np.sqrt(var)
var1=((mid[0]-avg)**2+(mid[1]-avg)**2+(mid[2]-avg)**2+(mid[3]-avg)**2)/4
np.sqrt(mid.var())
np.sqrt(var1)


plt.figure(1)
n1=np.random.randn(10) # 정규분포
u=np.random.uniform(-1, 1, 10) # 균등분포
u1=np.random.rand(10) # 균등분포

plt.plot(n1,'o:')
plt.plot(u, '*:')
plt.plot(u1, '.:')
plt.grid()

n1=np.random.randn(10000)
c1=np.size(np.where((n1>=-1) & (n1<=1) ))
print('c1 = ', c1)
n2=np.random.randn(10000)*2
c2=np.size(np.where((n2>=-2) & (n2<=2) ))
print('c2 = ', c2)
n3=np.random.randn(10000)+2
c3=np.size(np.where((n3>=1) & (n3<=3) ))
print('c3 = ', c3)
n4=2*np.random.randn(10000)+2
c4=np.size(np.where((n4>=0) & (n4<=4) ))
print('c4 = ', c4)

plt.figure(2)
plt.hist(n1, 100, normed=1)
plt.hist(n2, 100, normed=1)
plt.hist(n3, 100, normed=1)
plt.hist(n4, 100, normed=1)

# draw histogram
import numpy as np
import matplotlib.pyplot as plt


nd=np.random.randn(10)
ud=np.random.uniform(-1, 1, 10)
plt.figure(3)
plt.subplot(2, 1, 1)
plt.hist(nd, 4)
plt.title('Normal and Uniform')
plt.ylabel('Normal')
plt.grid()
plt.subplot(2, 1, 2)
plt.hist(ud, 4)
plt.ylabel('Uniform')
plt.grid()
plt.show()

print("count = " , count, "\nbin_left= ", bin_left)
print("\ncount1 = " , count1, "\nbin_left1= ", bin_left1)
