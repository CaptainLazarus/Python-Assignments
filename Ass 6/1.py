#for plotting dotted graph
import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3,4],[3,4,6,8],'go')
plt.ylabel('Y-Axis')
plt.xlabel('X-Axis')
plt.show()

#plotting a line graph
plt.plot([1,2,3,4],[2,3,4,5])
plt.ylabel('Marks')
plt.axis([1,5,1,6])
plt.show()

#diagram comparision
a=np.arange(2)
plt.plot(a,a,'r--',a,a**2,'g--',a,a**3,'b--')
plt.show()
