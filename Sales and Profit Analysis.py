import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Generate sample data
data = {
    'Year': [2010, 2011, 2012, 2013, 2014],
    'Sales': [100, 150, 200, 250, 300],
    'Profit':[25, 50, 75, 100, 125]
    }
df = pd.DataFrame(data)

#Create a figure and axis
fig, ax = plt.subplots(figsize=(10,6))

#Plot bar chart for Sales
sns.lineplot(x='Year', y='Sales', data=df, color='skyblue', ax=ax)

# Plot line plot for Profit
sns.lineplot(x='Year', y='Profit', data=df, marker='o', color='red', ax=ax)

#Set labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Amount')
ax.set_title('Sales and Profit Over Years')

#Show the plot
plt.show()
