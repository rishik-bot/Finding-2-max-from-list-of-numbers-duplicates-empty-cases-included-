#!/usr/bin/env python
# coding: utf-8

# In[25]:


# Read the input list
import ast
input_str = input()
input_list = ast.literal_eval(input_str)

# Write your code here
list1=list(set(input_list))
max1=list1[0]
max2=0
if len(list1)<=1:
    print("not present")
else:
    for i in range(1,len(list1)):
        if list1[i]>=max1:
            max2=max1
            max1=list1[i]
        else:
            max2=list1[i]
    print(max2)
            


# In[26]:


#method2

# Read the input list
import ast
input_str = input()
input_list = ast.literal_eval(input_str)

# Write your code here
list1=list(set(input_list))

if len(list1)<=1:
    print("not present")
else:
    del list1[list1.index(max(list1))]
    print(max(list1))


# In[ ]:




