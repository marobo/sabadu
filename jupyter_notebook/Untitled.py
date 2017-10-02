
# coding: utf-8

# ## LIST CONTAINING THE LENGHT OF THE NAME FOR EACH DICT IN INSIDE NAME

# In[1]:


names = ['Ano', 'Ony', 'Nico', 'Mario', 'Nando', 'Pedro']

# a list containing the length of the name for every name inside names
list_of_name_lengths = [len(name) for name in names]
print(list_of_name_lengths)

# a list containing "Hello {name}" for every name inside names
list_of_hello_names = ["Hello {name}".format(name=name) for name in names]
print(list_of_hello_names)

# a list containing "Hello {name}" for every name inside names which is longer than 3 letters
list_of_hello_long_names = ["Hello {name}".format(name=name) for name in names if len(name) > 3]
print(list_of_hello_long_names)


# # Dictionary Comprehensions
# ** Dictionary comprehension are just like comprehensions! But we must give a key and value **

# In[12]:


names = ['Ano', 'Ony', 'Nico', 'Mario', 'Nando', 'Pedro']

# a list containing the length of the name for every name inside names
name_len_dict = {name: len(name) for name in names}
print(name_len_dict)


# ** Dictionary contain key=name value="hello {name}" **
# 
# ** Dictionary contain key=name value="{name} contain a letter 'i' " only if the name contains 'i' **

# In[14]:


name_hello_dict = {name: "Hello {name}".format(name=name) for name in names}
print(name_hello_dict)


# In[ ]:




