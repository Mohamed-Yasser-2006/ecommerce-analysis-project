import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("ecommerce_data.csv")

# Feature Engineering
df["Sales"] = df["Quantity"] * df["Price"]
 
# Analysis
total_sales = df["Sales"].sum()
average_order_value = total_sales / len(df)

product_sales = df.groupby("Product")["Sales"].sum()
product_quantity = df.groupby("Product")["Quantity"].sum()
category_sales  = df.groupby("Category")["Sales"].sum()
city_sales = df.groupby("City")["Sales"].sum()

print("\n===== PRODUCT QUANTITY =====")
print(product_quantity.sort_values(ascending=False))

print("\n===== CATEGORY SALES =====")
print(category_sales.sort_values(ascending=False))

print("\n===== CITY SALES =====")
print(city_sales.sort_values(ascending=False))

top_5_products = product_sales.sort_values(ascending=False).head(5)

# Report
print("\n===== E-COMMERCE REPORT =====")

print(f"Total Sales: {total_sales:.2f}")
print(f"Average Order Value: {average_order_value:.2f}")

print("Best Selling Product:", product_quantity.idxmax())
print("Worst Selling Product:", product_quantity.idxmin())

print("Best Category:", category_sales.idxmax())
print("Worst Category:", category_sales.idxmin())

print("Best City:", city_sales.idxmax())
print("Worst City:", city_sales.idxmin())

print("\n===== TOP 5 PRODUCTS BY SALES =====")
print(top_5_products)

# Visualization
plt.figure(figsize=(8, 5))

product_sales.sort_values(ascending=False).plot(kind="bar")

plt.title("Sales By Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.savefig("product_sales.png")
plt.show()

plt.figure(figsize=(8, 5))

city_sales.sort_values(ascending=False).plot(kind="bar")

plt.title("Sales By City")
plt.xlabel("City")
plt.ylabel("Sales")

plt.savefig("city_sales.png")
plt.show()