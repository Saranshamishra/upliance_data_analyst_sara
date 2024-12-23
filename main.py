# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YZ89_6m67PPJSDtLE784R8L3X_x4QJO6
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = '/Assignment.xlsx'
user_details = pd.read_excel(file_path, sheet_name='UserDetails.csv')
cooking_sessions = pd.read_excel(file_path, sheet_name='CookingSessions.csv')
order_details = pd.read_excel(file_path, sheet_name='OrderDetails.csv')

# 1. Check and Handle Missing Values
# Summarize missing values for each dataset
print("Missing Values:\n")
print("UserDetails:")
print(user_details.isnull().sum())
print("\nCookingSessions:")
print(cooking_sessions.isnull().sum())
print("\nOrderDetails:")
print(order_details.isnull().sum())

# Handling missing values in OrderDetails (e.g., fill with median or drop rows)
order_details['Rating'] = order_details['Rating'].fillna(order_details['Rating'].median())

# 2. Check for Duplicates
print("\nDuplicate Rows:")
print(f"UserDetails: {user_details.duplicated().sum()} duplicates")
print(f"CookingSessions: {cooking_sessions.duplicated().sum()} duplicates")
print(f"OrderDetails: {order_details.duplicated().sum()} duplicates")

# 3. Standardize Column Names
# Convert column names to lowercase and replace spaces with underscores
user_details.columns = user_details.columns.str.lower().str.replace(' ', '_')
cooking_sessions.columns = cooking_sessions.columns.str.lower().str.replace(' ', '_')
order_details.columns = order_details.columns.str.lower().str.replace(' ', '_')

# 4. Ensure Data Types are Consistent
# Convert dates to datetime format
user_details['registration_date'] = pd.to_datetime(user_details['registration_date'])
cooking_sessions['session_start'] = pd.to_datetime(cooking_sessions['session_start'])
cooking_sessions['session_end'] = pd.to_datetime(cooking_sessions['session_end'])
order_details['order_date'] = pd.to_datetime(order_details['order_date'])

# Convert numerical columns to appropriate types
user_details['total_orders'] = user_details['total_orders'].astype(int)
cooking_sessions['duration_(mins)'] = cooking_sessions['duration_(mins)'].astype(int)
order_details['amount_(usd)'] = order_details['amount_(usd)'].astype(float)

# Save cleaned datasets for review
user_details.to_csv('cleaned_user_details.csv', index=False)
cooking_sessions.to_csv('cleaned_cooking_sessions.csv', index=False)
order_details.to_csv('cleaned_order_details.csv', index=False)

print("Data Cleaning Complete!")

# Step 2: Merge Datasets
# Merging UserDetails and CookingSessions on user_id
user_cooking_data = pd.merge(user_details, cooking_sessions, on='user_id', how='inner')

# Merging the above with OrderDetails on session_id
merged_data = pd.merge(user_cooking_data, order_details, on='session_id', how='inner')

# Save merged dataset for analysis
merged_data.to_csv('merged_dataset.csv', index=False)

print("Datasets Merged Successfully!")

# Step 3: Analyze Relationships
# Analyzing connections between cooking sessions and user orders
# 1. Investigate patterns in session participation and subsequent ordering behavior
participation_rate = merged_data.groupby('user_id_x')['session_id'].nunique() / user_details['total_orders']
print("\nParticipation Rate per User:")
print(participation_rate)

# 2. Repeat orders analysis
repeat_orders = merged_data.groupby('user_id_x')['order_id'].nunique().apply(lambda x: x > 1).sum()
print("\nRepeat Orders:")
print(repeat_orders)

# 3. Trends in session participation rates
daily_sessions = merged_data.groupby(merged_data['session_start'].dt.date)['session_id'].nunique()
print("\nDaily Session Participation:")
print(daily_sessions)

# Save analysis results
participation_rate.to_csv('participation_rate.csv')
repeat_orders_df = pd.DataFrame([repeat_orders], columns=['repeat_orders'])  # Convert to DataFrame
repeat_orders_df.to_csv('repeat_orders.csv', index=False) # Save to CSV

daily_sessions.to_csv('daily_sessions.csv')

print("Analysis of Relationships Complete!")

# Step 4: Identify Popular Dishes
# Aggregating and ranking orders by dish name
popular_dishes = merged_data.groupby('dish_name_x')['order_id'].count().sort_values(ascending=False)
print("\nPopular Dishes:")
print(popular_dishes)

# Investigate variations by demographics (e.g., age group)
merged_data['age_group'] = pd.cut(merged_data['age'], bins=[0, 18, 35, 50, 65, 100], labels=['<18', '18-35', '35-50', '50-65', '65+'])
dish_by_age = merged_data.groupby(['age_group', 'dish_name_x'])['order_id'].count().unstack().fillna(0)
print("\nDishes by Age Group:")
print(dish_by_age)

# Save analysis results
popular_dishes.to_csv('popular_dishes.csv')
dish_by_age.to_csv('dish_by_age_group.csv')

print("Popular Dishes Analysis Complete!")

# Step 5: Demographic Influences
# Segment users by demographics and analyze behavior
# 1. Age group influence on total orders
age_group_orders = merged_data.groupby('age_group')['order_id'].nunique()
print("\nTotal Orders by Age Group:")
print(age_group_orders)

# 2. Location influence on participation
location_participation = merged_data.groupby('location')['session_id'].nunique()
print("\nSessions by Location:")
print(location_participation)



# Save demographic analysis results
age_group_orders.to_csv('age_group_orders.csv')
location_participation.to_csv('location_participation.csv')


print("Demographic Influences Analysis Complete!")

# Step 6: Visualizations
# 1. Bar chart: Total Orders by Age Group
plt.figure(figsize=(10, 6))
age_group_orders.plot(kind='bar', color='skyblue')
plt.title('Total Orders by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Total Orders')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('total_orders_by_age_group.png')
plt.show()

# 2. Heatmap: Dishes by Age Group
plt.figure(figsize=(12, 8))
sns.heatmap(dish_by_age, cmap='YlGnBu', annot=False)
plt.title('Dishes by Age Group')
plt.xlabel('Dish Name')
plt.ylabel('Age Group')
plt.tight_layout()
plt.savefig('dishes_by_age_group_heatmap.png')
plt.show()

# 4. Bar chart: Sessions by Location
plt.figure(figsize=(12, 6))
location_participation.sort_values(ascending=False).plot(kind='bar', color='green')
plt.title('Sessions by Location')
plt.xlabel('Location')
plt.ylabel('Number of Sessions')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('sessions_by_location.png')
plt.show()

print("Visualizations Generated and Saved!")