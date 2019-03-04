
# coding: utf-8

# In[15]:


from random import randint


# In[16]:


player= input('rock(r),paper(p),scissor(s)? \n')


# In[17]:


print(player,'vs')


# In[18]:


chosen=randint(1,3)


# In[19]:


#print(chosen)


# In[20]:


if chosen==1:
    computer='r'
elif chosen==2:
    computer='p'
else:
    computer='s'


# In[21]:


print(computer)
if player==computer:
    print('draw')
elif player=='r' and computer=='s':
    print('You won!')
elif player=='r' and computer=='p':
    print('lost. better luck next time')
elif player=='p' and computer=='r':
    print('you won!')
elif player=='p' and computer=='s':
    print('lost. better luck next time')


# In[22]:


input("Press enter to exit ;)")

