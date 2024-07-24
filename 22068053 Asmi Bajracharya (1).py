#!/usr/bin/env python
# coding: utf-8

# # Smart Data Discovery 

# ## Data Preparation

# In[7]:


#importing pandas
import pandas as pd


# #### Write a python program to load data into pandas DataFrame.

# In[8]:


#Loading data into pandas dataframe 
df = pd.read_csv('DataScienceSalaries.csv')


# In[3]:


#viewing dataframe
df


# #### Write a python program to remove unnecessary columns i.e., salary and salary currency.

# In[4]:


#Dataframe before removing unnesessary columns
df


# In[11]:


#removing unnecessary columns 
df.drop(['salary', 'salary_currency'], axis=1, inplace=True)


# In[12]:


#Dataframe after removing unnesessary columns
df


# #### Write a python program to remove the NaN missing values from updated dataframe. 

# In[11]:


#Removing the NaN missing values from updated dataframe. 
df.dropna(inplace=True)


# In[10]:


#checking the dataframe
df


# #### Write a python program to check duplicates value in the dataframe.

# In[12]:


#Checking duplicate values in dataframe
duplicate_rows = df[df.duplicated()]

if not duplicate_rows.empty:
    print("Duplicate rows found:\n", duplicate_rows)
else:
    print("No duplicate rows found.")


# #### Write a python program to see the unique values from all the columns in the dataframe.

# In[14]:


#Checking unique values from all the columns
for column in df.columns:
    unique_values = df[column].unique()
    print(f"Unique values in column '{column}': {unique_values}")


# #### Rename the experience level columns as below.
# SE – Senior Level/Expert
# MI – Medium Level/Intermediate
# EN – Entry Level
# EX – Executive Level

# In[15]:


#Renaming the experience level column
df['experience_level'].replace({
    'SE': 'Senior Level/Expert',
    'MI': 'Medium Level/Intermediate',
    'EN': 'Entry Level',
    'EX': 'Executive Level'
}, inplace=True)


# In[16]:


#checking if it was renamed 
df


# ## Data Analysis

# In[17]:


#before starting with the data analysis we need to remove all the duplicte values
df.drop_duplicates(inplace=True)


# In[18]:


df


# In[94]:


#now we need to remove all the data inconsistencies
df['job_title']=df['job_title'].replace('Principal Data Scientist'
,'Data Scientist Lead')
df['job_title']=df['job_title'].replace(['Machine Learning Engineer','Applied Machine Learning Engineer','Machine Learning Infrastructure Engineer','Machine Learning Software Engineer','Machine Learning Research Engineer','MLOps Engineer'],'ML Engineer')
df['job_title']=df['job_title'].replace('Applied Scientist','Applied Data Scientist')
df['job_title']=df['job_title'].replace(['Compliance Data Analyst','Marketing Data Analyst','Business Data Analyst','Staff Data Analyst','Lead Data Analyst','Data Quality Analyst','Data Operations Analyst','Data Analytics Lead','Financial Data Analyst','BI Analyst','BI Data Analyst','Insight Analyst','Finance Data Analyst','Principal Data Analyst'],'Data Analyst')
df['job_title']=df['job_title'].replace('Business Intelligence Engineer','BI Data Engineer')
df['job_title']=df['job_title'].replace('Data Engineer','Data Science Engineer')
df['job_title']=df['job_title'].replace('Data DevOps Engineer','Data Operations Engineer')
df['job_title']=df['job_title'].replace('Head of Data','Data Lead')
df['job_title']=df['job_title'].replace(['Manager Data Management','Data Management Specialist','Data Science Manager','Data Analytics Manager'],'Data Manager')
df['job_title']=df['job_title'].replace('Data Analytics Specialist','Data Specialist')
df['job_title']=df['job_title'].replace('Applied Machine Learning Scientist','Machine Learning Scientist')
df['job_title']=df['job_title'].replace('Lead Data Scientist','Data Science Lead')
df['job_title']=df['job_title'].replace('Cloud Database Engineer','Cloud Data Engineer')
df['job_title']=df['job_title'].replace(['Head of Machine Learning','Principal Machine Learning Engineer'],'Lead Machine Learning Engineer')
df['job_title']=df['job_title'].replace('Principal Data Engineer','Lead Data Engineer')
df['job_title']=df['job_title'].replace('Data Science Tech Lead','Head of Data Science')


# In[37]:


#checking if the data inconsistency is removed 
for column in df.columns:
    unique_values = df[column].unique()
    print(f"Unique values in column '{column}': {unique_values}")
    


# In[38]:


#now moving on with the data analytics


# #### Write a Python program to show summary statistics of sum, mean, standard deviation, skewness, and kurtosis of any chosen variable. 

# ##### Sum of salary_in_usd

# In[39]:


df['salary_in_usd'].sum()


# ##### Mean of salary_in_usd

# In[40]:


df['salary_in_usd'].mean()


# ##### Standard deviation of salary_in_usd

# In[41]:


df['salary_in_usd'].std()


# ##### Skewness

# In[42]:


df['salary_in_usd'].skew()


# ##### Kurtosis 

# In[43]:


df['salary_in_usd'].kurtosis()


# #### Write a Python program to calculate and show correlation of all variables. 

# In[95]:


# calculating the correlation 
df.corr(numeric_only = True)


# ## Data Exploration

# #### Write a python program to find out top 15 jobs. Make a bar graph of sales as well.         

# In[58]:


#top 15 jobs 
top_jobs = df['job_title'].value_counts().head(15)


# In[59]:


top_jobs


# In[3]:


#importing matplotlib.pyplot
import matplotlib.pyplot as plt


# In[67]:


#Bargraph for top 15 jobs
top_jobs.plot(kind='bar', color='purple')
plt.title('Top 15 Jobs')
plt.xlabel('Job Title')
plt.ylabel('Frequency')
plt.legend(['Frequency'], loc="upper right")


# #### Which job has the highest salaries? Illustrate with bar graph.

# In[13]:


#sorting values top 5 highest salaries
highest_salaries = df.sort_values(by="salary_in_usd",ascending=False).head(5)
highest_salaries 


# In[14]:


#top 5 highest paid salaries
plt.bar(highest_salaries['job_title'], highest_salaries['salary_in_usd'], color='pink')
plt.title('Top 5 Highest Salaries')
plt.xlabel('Job Title')
plt.ylabel('Salary in USD')
plt.legend(['Salary in USD'], loc='upper right')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# #### Write a python program to find out salaries based on experience level. Illustrate it through bar graph.

# In[80]:


#salaries based on experience level
mean_salary_by_experience = df.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending=False)
mean_salary_by_experience


# In[84]:


#for the bargraph 
mean_salary_by_experience.plot(kind='bar', color='red')
plt.title('Mean Salary by Experience Level')
plt.xlabel('Experience Level')
plt.ylabel('Mean Salary in USD')
plt.legend(['Mean Salary in USD'], loc='upper right')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# #### Write a Python program to show histogram and box plot of any chosen different variables. Use proper labels in the graph.	

# ##### Histogram

# In[92]:


# using the variable salary_in_used to plot the histogram 
plt.hist(df['salary_in_usd'], color='blue', edgecolor='black')
plt.title('Salary Distribution')
plt.xlabel('Salary in USD')
plt.ylabel('Frequency')
plt.legend(['Salary in USD'], loc='upper right')
plt.grid(True)
plt.show()


# ##### Boxplot

# In[93]:


#boxplot for salary in usd
plt.boxplot(df['salary_in_usd'], vert=False, patch_artist=True, showmeans=True)
plt.title('Box Plot of salary_in_usd ')
plt.xlabel('salary_in_usd')


# In[ ]:




