#!/usr/bin/env python
# coding: utf-8

# In[ ]:


fh = open("lwfile.txt" , "r")


# In[ ]:


fh.tell()


# In[ ]:


fh.read(2)


# In[ ]:


fh.tell()


# In[ ]:


fh.read(4)


# In[ ]:


fh.read(5)


# In[ ]:


fh.tell()


# In[ ]:


fh.seek(6, 0 )


# In[ ]:


fh.tell()


# In[ ]:


fh.read()


# In[ ]:


fh.tell()


# In[ ]:


fh.close()


# In[ ]:





# In[ ]:


myfile = open("lwfile.txt")


# In[ ]:


for line in myfile:
    print(line.split()[3] , end='\n')
    


# In[ ]:


myfile.close()


# In[ ]:


for  x in myfile:
    if  "rahul" in x:
        print(x)
        


# In[ ]:





# In[ ]:


myfile.read()


# In[ ]:


myfile.close()


# In[ ]:


a = [ 1, 2, 3]


# In[ ]:


for x in a:
    print(x)


# In[ ]:


s = "this is linux world"


# In[ ]:


s


# In[ ]:


for w in s.split():
    print(w)


# In[ ]:


s.split()[3]


# In[ ]:


fh = open("mylw123.txt" , mode="r+")


# In[ ]:


fh.write("byeee")


# In[ ]:


fh.read()


# In[ ]:


fh.close()


# In[ ]:




