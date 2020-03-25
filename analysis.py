
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# In[3]:


def get_data(file):
    with open(file, 'r') as f:
        return np.array([float(s) for s in f.readlines()])


# In[33]:


labels = ['A2C / no pen.', 'A2C / death pen.', 'DQN / no pen.', 'DQN / death pen.', 'DQN w/ pen. (save)']
data_folders = ['task3/a2c_nopen_test.txt', 'task3/a2c_small_deathpen_test.txt', 'task3/dqn_nopen_test.txt', 'task3/dqn_small_deathpen_test.txt', 'task3/dqn_save_deathpen_test.txt']


# In[34]:


#data = [a2c_normal, a2c_pen, dqn_normal, dqn_pen]
data = [get_data(a) for a in data_folders]

#matplotlib widget
plt.boxplot(data, labels=labels)
plt.ylabel('Distance run')
#plt.ylim(73, 100)
plt.show()


# In[23]:


plt.plot(get_data('task3/dqn_small_deathpen_test.txt'), 'o')
#plt.plot(get_data('task3/dqn_nopen_train.txt'), 'o')

