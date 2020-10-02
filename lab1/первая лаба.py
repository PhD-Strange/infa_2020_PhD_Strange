#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
x = np.array([1,10,1000])
y = np.log((np.exp(1 / (np.sin(x) + 1)))/(5/4 + x**(1/5)))/np.log(1 + x**2)
print(y)


# In[6]:


import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-5.0, 5.01, 0.010)
plt.plot(x, x*x - x - 6, x, x*0)
plt.grid(True)
plt.show()


# In[3]:


import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10.0, 10.01, 0.01)
y = np.log((x**2 + 1)*np.exp(-abs(x)/10))/np.log(1 + np.tan(1/(1 + (np.sin(x))**2)))
plt.plot(x, y)
plt.grid(True)
plt.show()


# In[4]:


import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10.0, 10.01, 0.01)
plt.plot(x, eval(input()))
plt.grid(True)
plt.show()


# In[5]:


import numpy as np
x = [1,2,3,4,5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
plt.errorbar(x, y, xerr=0.05, yerr=0.1, linestyle = 'none')
p, v = np.polyfit(x, y, deg = 3, cov = True)
plt.grid()
p_f = np.poly1d(p)
x_arr = np.arange(0.0, 6.0, 0.1)
plt.plot(x_arr, p_f(x_arr))


# In[11]:


import numpy as np
import matplotlib.pyplot as plt

a, b = 3, 0.5
n_max = int(1/b)**5
pi = np.pi
x_s = np.arange(-2, 2.01, 0.01)
y_s = []

for x in x_s:
    y0 = np.cos(x*pi)
    y = y0
    n = 1
    for n in range(n_max) :        
        y += b**n * np.cos(a**n * x * pi)
        n += 1
        
    y_s.append(y)
        
plt.errorbar(x_s, y_s)
plt.grid(True)
plt.show()


# In[ ]:




