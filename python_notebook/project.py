#!/usr/bin/env python
# coding: utf-8

# In[3]:


def download_files(url, file_name):
    #This function accepts url and file_name as parameters.
    #url from where we have to download the file (got from inspecting the element on page)
    #file_name is the name you want to give to downloaded file on system
    import requests
    response = requests.get(url,allow_redirects=True)
    if response.status_code == 200:
        open('C:/Users/Abhishek/OneDrive/Desktop/Kritika/skyfri/' + file_name + '.csv', 'wb').write(response.content)
    else:
        print(response.url + ' - cannot be reached. Response code: ' + str(response.status_code))
    


# In[4]:


def read_all_files(path):
    #Read the content of all the downloaded files from a local path
    #Store the file contents into a single dataframe
    import pandas as pd 
    import os 
    import glob
    #Read all files present in folder
    csv_files = glob.glob(os.path.join(path, '*.csv')) 
    dfs = []
    #Create separate dataframe for each file and put in a list
    for filename in csv_files:
        dfs.append(pd.read_csv(filename))
        
    #Concat all DF's
    big_frame = pd.concat(dfs, ignore_index=True)
    return big_frame
    
        


# In[9]:


try:
    for month in range(1,13):
        #converting 1 to 01 for all simgle digit months
        month = str("{:02d}".format(month))
        #creating url and downloading files to local
        url_2022 = 'https://data.urbansharing.com/oslobysykkel.no/trips/v1/2022/'+month+'.csv'
        download_files(url_2022, str('2022_'+ month))
        url_2023 = 'https://data.urbansharing.com/oslobysykkel.no/trips/v1/2023/'+month+'.csv'
        download_files(url_2023, str('2023_'+ month))
        #creating df from all the downloaded files
        df = read_all_files('C:/Users/Abhishek/OneDrive/Desktop/Kritika/skyfri/')
        #replacing all the norwegian characters with near english characters
        df_rem_nor = df.replace(['(?i)æ','(?i)ø','(?i)å','(?i)é','(?i)ü'],['ae','oe','aa','ee', 'uu'],regex=True)
except Exception as e:
    print(e)


# In[17]:


print(df_rem_nor[['start_station_name','start_station_description','end_station_name','end_station_description']])


# In[ ]:




