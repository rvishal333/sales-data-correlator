import pandas as pd
import random

# Generate an expanded dataset with 100 samples
data = {
    "sale_id": list(range(1, 501)),
    "branch": [random.choice(["A", "B", "C"]) for _ in range(500)],
    "city": [random.choice(["New York", "Chicago", "Los Angeles"]) for _ in range(500)],
    "customer_type": [random.choice(["Member", "Normal"]) for _ in range(500)],
    "gender": [random.choice(["Male", "Female"]) for _ in range(500)],
    "product_name": [f"Product {chr(65 + i % 26)}" for i in range(500)],
    "product_category": [random.choice(["Category A", "Category B", "Category C"]) for _ in range(500)],
    "unit_price": [round(random.uniform(5.0, 100.0), 2) for _ in range(500)],
    "quantity": [random.randint(1, 10) for _ in range(500)],
}

# Calculate tax (7%) and total price
data["tax"] = [round(price * qty * 0.07, 2) for price, qty in zip(data["unit_price"], data["quantity"])]
data["total_price"] = [
    round(price * qty + tax, 2) for price, qty, tax in zip(data["unit_price"], data["quantity"], data["tax"])
]

# Assign reward points for members
data["reward_points"] = [
    random.randint(5, 50) if cust_type == "Member" else 0 for cust_type in data["customer_type"]
]

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
csv_file_path = "expanded_sales.csv"
df.to_csv(csv_file_path, index=False)

print(f"Expanded dataset saved to {csv_file_path}")
