#!/usr/bin/env python
# coding: utf-8

# In[20]:


#function to shift inputted strings by length of words forward if even and backwards if odd
#use encrypt = false to decrypt (reverse)
alpha="abcdefghijklmnopqrstuvwxyz"
punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''


# In[59]:


def encrypter(text, encrypt=True):
    new_string = []
    split_by_space = text.split(" ")
    
    for words in split_by_space:
        new_letters = []
        word = list(words)
        if not((len(word)%2) == 0 ^ encrypt == True):
            modifier = len(word)
        else:
            modifier = -len(word)
        #print(modifier)
        
        for char in word:
            print(char)
            if alpha.find(char) != -1:  
                if alpha.find(char)+modifier >= len(alpha):
                    shifted = alpha[alpha.find(char)+modifier-26]
                elif alpha.find(char)+modifier < 0:
                    shifted = alpha[alpha.find(char)+modifier+26]
                else:
                    shifted = alpha[alpha.find(char)+modifier]
                    
            else:
                shifted = char
            new_letters.append(shifted)
            
        new_word = "".join(new_letters)
        new_string.append(new_word)
    print(" ".join(new_string))


# In[ ]:




