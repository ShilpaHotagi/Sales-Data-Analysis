import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('../data/sales.csv')

# Data Cleaning
df.dropna(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Sales by Category
category_sales = df.groupby('Category')['Sales'].sum()
print(category_sales)

category_sales.plot(kind='bar', title="Sales by Category")
plt.show()

# Monthly Trend
df['Month'] = df['Order Date'].dt.month
monthly_sales = df.groupby('Month')['Sales'].sum()

monthly_sales.plot(title="Monthly Sales Trend")
plt.show()