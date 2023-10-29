# %%
# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# Importing dataset
df = pd.read_csv('Indian_Startup_Data.csv')

# # %%
# import pandas as pd

# # Assuming you have read your dataset into a DataFrame named 'df'
# # Replace 'Count' with the actual column name containing the count
# new_df = df.loc[df.index.repeat(df['Count'])]

# # Reset the index of the new DataFrame
# new_df.reset_index(drop=True, inplace=True)

# # new_df = df.drop(columns=['S No.'])

# # Print the new DataFrame
# new_df


# # %%
# new_df = new_df.drop(columns=['S No.'])
# new_df


# # %%
# df.head(15)

# # %%
# mask = (new_df['Year'] >= 2018) & (new_df['Year'] <= 2023)

# # %%
# df = new_df[mask]

# # %%
# df

# # %%
# # Checking for Null values
# (df.isnull().sum() / df.shape[0] * 100).sort_values(ascending = False).round(2).astype(str) + ' %'

# # %%
# # Assuming 'category_column' is the name of the column by which you want to categorize the dataset

# Get unique values in the 'category_column'
unique_categories = df['State'].unique()

# Create a dictionary to store subsets of the data based on unique values
category_dict = {}

# Iterate through unique categories and create subsets
for category in unique_categories:
    category_dict[category] = df[df['State'] == category]

# Now, 'category_dict' contains subsets of the data categorized by 'category_column'
# Each key in the dictionary corresponds to a unique category value, and the corresponding value is a DataFrame subset.


# %%

# Count the number of startups founded in each year
startup_counts = df['Year'].value_counts().sort_index()

# 'startup_counts' is now a Series that contains the count of startups for each year
print(startup_counts)

# %%
unique_industries = df['Industry'].unique()

# Create a separate line graph for each unique industry
for industry in unique_industries:
    industry_data = df[df['Industry'] == industry]
    industry_counts = industry_data['Year'].value_counts().sort_index()
    
    # Set up the figure and axes for each plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create the line plot with whole number years on the x-axis
    x = range(2018, 2024)
    y = [industry_counts.get(year, 0) for year in x]
    ax.plot(x, y, marker='o', linestyle='-')
    
    # Customize the plot
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Companies')
    ax.set_title(f'Number of Companies Formed per Year in {industry} (2018-2023)')
    
    # Show each plot
    plt.show()

# %% [markdown]
# +++++++
# covid question
# +++++++

# %%
# Group the data by industry and year, and count the number of companies
grouped = df.groupby(['Industry', 'Year']).size().unstack(fill_value=0)

# Calculate the decrease in percentage from 2019 to 2020 for industries with non-zero values in 2019
grouped['Decrease_Percentage'] = ((grouped[2019] - grouped[2020]) / grouped[2019]) * 100

# Filter for companies with a decrease in percentage and non-zero value in 2019
decreased_companies = -1*grouped[(grouped['Decrease_Percentage'] > 0) & (grouped[2019] > 0)]

# Print or further process the 'decreased_companies' DataFrame
print(decreased_companies)




# %%
# Group the data by industry and year, and count the number of companies
grouped = df.groupby(['Industry', 'Year']).size().unstack(fill_value=0)

# Calculate the decrease in percentage from 2019 to 2020 for industries with non-zero values in 2019
grouped['Decrease_Percentage'] = (((grouped[2019] - grouped[2020]) / grouped[2019]) * 100)

# Filter for companies with a decrease in percentage and non-zero value in 2019
decreased_companies = -1*grouped[(grouped['Decrease_Percentage'] > 0) & (grouped[2019] > 0)]
decreased_companies.head()

# Create a new dataframe with the industry and the corresponding decrease percentage
decreased_df = pd.DataFrame({'Industry': decreased_companies.index, 'Decrease_Percentage': decreased_companies['Decrease_Percentage']})


print(decreased_df)





# %%
decreased_df.info()


import random

def plot(df,x,y):
    fig, ax = plt.subplots(figsize=(10, 6))
    df_sorted = df.sort_values(y, ascending=False)
    ax.bar(df_sorted[x], df_sorted[y], color='green')
    ax.set_xticklabels(df_sorted[x], rotation=75)
    ax.xaxis.set_ticks_position('top')
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(f'{y} vs {x}')

    return fig

# %%
plot(decreased_df,'Industry','Decrease_Percentage')







