#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd


# In[65]:


df = pd.read_excel(r"C:\Users\lucas\Desktop\Programacion 2019\Phyton\Data Cleaning in Pandas\Customer Call List.xlsx")
df


# In[67]:


# FIRST WE DROP THE DUPLICATES, and we asign the new DF to the variable
df = df.drop_duplicates()
df


# In[69]:


# WE DROP THE COLUMNS THAT WE DONT NEED. And asign the new data to re variable DF
df = df.drop(columns = "Not_Useful_Column")
df


# In[71]:


# WE CLEAN THE LAST_NAME COLOUMB, and asign the new data to the COLUMN ALONG, NOT ALL THE DATAFRAME (DF)
#df["Last_Name"] = df["Last_Name"].str.lstrip("...")
#df["Last_Name"] = df["Last_Name"].str.lstrip("/")
#df["Last_Name"] = df["Last_Name"].str.rstrip("_")
df["Last_Name"] = df["Last_Name"].str.strip("123._/")
df


# In[141]:


# NOW WE WANT TO CLEAN THE PHONE_NUMBER COLUMN

#1° WE REPLACE THE THINGS THAT WE DONT NEED LIKE ": _ - /, ETC"
#df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]', '', regex=True)

#2° WE SET THE NUMBERS HOW WE WANTED: 123-456-7890 , BUUUUT WE ARE GOING TO CHANGE THE NUMBER DATA TYPE TO STRINGS TO DO THIS, THAT WHY WE APPLY THE 
# 3RD CODE. 
#df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

#3° WE CONVERT THE NUMBER DATA TYPE TO STRING DATA TYPE 
# df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))

#4° NOW WE APPLY THE SETTING OF --- LIKE WE WANT TO
#df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

#5° WE REMOVE THE "NAN--" VALUES AND LET A BLANK SPACE
#df["Phone_Number"] = df["Phone_Number"].str.replace('nan--','')

#6° WE REMOVE THE "NA--" VALUES AND LET A BLANK SPACE
df["Phone_Number"] = df["Phone_Number"].str.replace('Na--','')
df


# In[151]:


# NOW WE WANT 3 DIFFERENTS COLUMNS FOR THE ADDRESS, STATE, AND ZIP CODE
df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(',', n=2,  expand=True)
df


# In[155]:


# NOW WE WANT TO STANDARIZED ALL VALUES YES=Y  NO=N
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes','Y')

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No','N')

df["Paying Customer"] = df["Paying Customer"].str.replace('Yes','Y')

df["Paying Customer"] = df["Paying Customer"].str.replace('No','N')

df


# In[159]:


# WE REMOVE THE N/A AND NaN VALUES WITH A BLANK SPACE
df=df.fillna('')
df = df.replace('N/a','')
df


# In[161]:


# NOW WE WANT TO REMOVE THE ROWS OF CLIENTS THAT DOESN´T WANT TO BE CALL BY THE CALL-CENTER
#WE APPLY A LOOP IN SEARCH FOR THE "Y" IN THE "DO_NOT_CALL" COLUMN AND DROP THE ENTIRE ROW
for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)

df


# In[163]:


# WE WANT TO DROP THE ROWS THAT HAS NO PHONE VALUE, BECAUSE WE CANT CALL IT
for x in df.index:
    if df.loc[x, "Phone_Number"] == '':
        df.drop(x, inplace=True)

df


# In[ ]:


# FINALLY WE  RESET THE INDEX VALUE AND ERASE THE OLD INDEX
df = df.reset_index(drop=True)
df

