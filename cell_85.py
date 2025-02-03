#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Please enter a sequence of comma-separated numbers")
numbers = input()
numbersList = numbers.split(',')
numberTuple = tuple(numbersList)
print(numbersList, end='')
print(numberTuple)

