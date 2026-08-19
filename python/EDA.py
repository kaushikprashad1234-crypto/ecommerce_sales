# ============================================================
# E-Commerce Sales Analytics - Exploratory Data Analysis (EDA)
# ============================================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("E:\\power bi\\ecommerce_sales\\data\\ecommerce_sales_analytics_5000.csv")

# -----------------------------
# 2. Display Dataset
# -----------------------------
print("First 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

# -----------------------------
# 3. Dataset Information
# -----------------------------
print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# -----------------------------
# 4. Missing Values
# -----------------------------
print("\nMissing Values")
print(df.isnull().sum())

# -----------------------------
# 5. Duplicate Records
# -----------------------------
print("\nDuplicate Records:", df.duplicated().sum())

# -----------------------------
# 6. Statistical Summary
# -----------------------------
print("\nStatistical Summary")
print(df.describe())

# -----------------------------
# 7. Revenue Analysis
# -----------------------------
print("\nTotal Revenue :", round(df['revenue'].sum(),2))
print("Average Revenue :", round(df['revenue'].mean(),2))
print("Maximum Revenue :", df['revenue'].max())
print("Minimum Revenue :", df['revenue'].min())

# -----------------------------
# 8. Quantity Analysis
# -----------------------------
print("\nTotal Quantity Sold :", df['quantity'].sum())
print("Average Quantity :", round(df['quantity'].mean(),2))

# -----------------------------
# 9. Product Category Analysis
# -----------------------------
category_sales = df.groupby('product_category')['revenue'].sum().sort_values(ascending=False)

print("\nRevenue by Category")
print(category_sales)

# -----------------------------
# 10. Region Analysis
# -----------------------------
region_sales = df.groupby('region')['revenue'].sum().sort_values(ascending=False)

print("\nRevenue by Region")
print(region_sales)

# -----------------------------
# 11. Payment Method Analysis
# -----------------------------
payment = df['payment_method'].value_counts()

print("\nPayment Methods")
print(payment)

# -----------------------------
# 12. Customer Rating
# -----------------------------
print("\nAverage Customer Rating")
print(round(df['customer_rating'].mean(),2))

# -----------------------------
# 13. Delivery Analysis
# -----------------------------
print("\nAverage Delivery Days")
print(round(df['delivery_days'].mean(),2))

# -----------------------------
# 14. Correlation Matrix
# -----------------------------
print("\nCorrelation Matrix")
print(df.corr(numeric_only=True))

# -----------------------------
# 15. Revenue Distribution
# -----------------------------
plt.figure(figsize=(8,5))
plt.hist(df['revenue'], bins=30)
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# 16. Revenue by Category
# -----------------------------
plt.figure(figsize=(8,5))
category_sales.plot(kind='bar')
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# 17. Revenue by Region
# -----------------------------
plt.figure(figsize=(8,5))
region_sales.plot(kind='bar')
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.show()

# -----------------------------
# 18. Payment Method Distribution
# -----------------------------
plt.figure(figsize=(6,6))
payment.plot(kind='pie', autopct='%1.1f%%')
plt.title("Payment Method Distribution")
plt.ylabel("")
plt.show()

# -----------------------------
# 19. Customer Rating Distribution
# -----------------------------
plt.figure(figsize=(8,5))
plt.hist(df['customer_rating'], bins=10)
plt.title("Customer Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# -----------------------------
# 20. Delivery Days Distribution
# -----------------------------
plt.figure(figsize=(8,5))
plt.hist(df['delivery_days'], bins=10)
plt.title("Delivery Days Distribution")
plt.xlabel("Days")
plt.ylabel("Count")
plt.show()

# -----------------------------
# 21. Discount vs Revenue
# -----------------------------
plt.figure(figsize=(8,5))
plt.scatter(df['discount'], df['revenue'])
plt.title("Discount vs Revenue")
plt.xlabel("Discount")
plt.ylabel("Revenue")
plt.show()

# -----------------------------
# 22. Monthly Revenue Trend
# -----------------------------
df['order_date'] = pd.to_datetime(df['order_date'])

monthly_sales = df.groupby(df['order_date'].dt.to_period('M'))['revenue'].sum()

plt.figure(figsize=(12,5))
monthly_sales.plot()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()

# -----------------------------
# 23. Top 10 Customers
# -----------------------------
top_customers = df.groupby('customer_id')['revenue'].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Customers")
print(top_customers)

# -----------------------------
# 24. Top Categories by Quantity
# -----------------------------
quantity = df.groupby('product_category')['quantity'].sum()

print("\nQuantity Sold by Category")
print(quantity)

# -----------------------------
# 25. Business KPIs
# -----------------------------
print("\n========== BUSINESS KPIs ==========")

print("Total Orders :", len(df))
print("Total Revenue :", round(df['revenue'].sum(),2))
print("Average Order Value :", round(df['revenue'].mean(),2))
print("Total Quantity :", df['quantity'].sum())
print("Average Rating :", round(df['customer_rating'].mean(),2))
print("Average Delivery :", round(df['delivery_days'].mean(),2))

print("\nEDA Completed Successfully!")