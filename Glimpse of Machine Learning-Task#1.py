#0.Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
#1.Read the dataset, convert it to DataFrame and display some from it.
dataset=pd.read_csv("Wuzzuf_Jobs.csv")
dataframe=dataset.iloc[:,0:3].values

#2.Display structure and summary of the data.
dataset.describe()

#3.Clean the data (null, duplications).
dataset.dropna()
dataset.drop_duplicates(keep = "first", inplace = True)

#4.Count the jobs for each company and display that in order (What are the most demanding companies for jobs?).
j=dataset['Company'].value_counts()
print(j)
print("The most demanding companies for jobs : "+j.index[0])

#5.Show step4 in a pie chart.
plt.pie(j,labels=j.index)
plt.show()

#6.Find out what are the most popular job titles.
t=dataset['Title'].value_counts()
print(t)
print("The most popular job titles : "+t.index[0])

#7.Show step 6 in bar chart.
a=list(t.index)
b=list(t.values)
plt.bar(a,b,width=0.4,color='maroon')
plt.xlabel("Job title")
plt.ylabel("The num of job title")
plt.title("The most popular job titles")
plt.show()

#8.Find out the most popular areas?
l=dataset['Location'].value_counts()
print(l)
print("The most popular areas : "+l.index[0])

#9.Show step 8 in bar chart.
x=list(l.index)
y=list(l.values)
plt.bar(x,y,width=0.4,color='red')
plt.xlabel("Location")
plt.ylabel("The num of location")
plt.title("The most popular areas")
plt.show()

#10.Print skills one by one , their count, and order the output to find out the most important skills required.
s=dataset['Skills'].value_counts()
print(s)
print("The most popular areas : "+s.index[0])
