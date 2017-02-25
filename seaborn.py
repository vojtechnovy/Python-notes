import matplotlib.pyplot as plt
import pandas as pd
from  matplotlib import pyplot
import seaborn as sns
seaborn.set(style='ticks')

df=pd.read_excel("C:\\Users\\antonin\\Desktop\\book1.xlsx", "Sheet1")
_genders = ["M","F"]

print(df.head(3))
#df.boxplot(by="Gender", column="Age")
#plt.show()

#df.hist(column='Age', bins=7)
#plt.show()

#plt.hist(df.Age, bins=7)
#plt.show()

#df.plot(kind="scatter", x="Age", y="Sales", color='Red', label='Group 2')
#plt.show()
sns.violinplot(df['Age'], df['Gender']) #Variable Plot
sns.despine()

fg = sns.FacetGrid(data=df, hue='Gender', hue_order=_genders, aspect=1.61)
fg.map(pyplot.scatter, 'Age', 'Sales').add_legend()
plt.show()

# Bar plot, grouped sum of sales by Gender
var = df.groupby('Gender').Sales.sum()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Gender')
ax1.set_ylabel('Sum of Sales')
ax1.set_title("Gender wise Sum of Sales")
var.plot(kind='bar')
plt.show()

# Line plot, grouped sum of sales by BMI
var = df.groupby('BMI').Sales.sum()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('BMI')
ax1.set_ylabel('Sum of Sales')
ax1.set_title("BMI wise Sum of Sales")
var.plot(kind='line')
plt.show()

var = df.groupby(['BMI','Gender']).Sales.sum()
var.unstack().plot(kind='bar',stacked=True,  color=['red','blue'], grid=False)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(df['Age'],df['Sales'], s=df['Income']) # Added third variable income as size of the bubble
plt.show()
