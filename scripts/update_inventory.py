import os

inventory_file = "inventory.txt"
orders_file = "orders.txt"
report_file = "report.txt"

# Load inventory
inventory = {}
if os.path.exists(inventory_file):
    with open(inventory_file, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2:
                product, qty = parts
                inventory[product] = int(qty)

# Process orders
if os.path.exists(orders_file):
    with open(orders_file, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2:
                product, qty = parts
                qty = int(qty)
                if product in inventory:
                    inventory[product] -= qty
                    if inventory[product] < 0:
                        inventory[product] = 0
                    print(f"Deducted {qty} of {product} from inventory")
                else:
                    print(f"Skipped unknown product in orders: {product}")

# Save updated inventory
with open(inventory_file, "w", encoding="utf-8") as f:
    for product, qty in inventory.items():
        f.write(f"{product},{qty}\n")

# Generate report
with open(report_file, "w", encoding="utf-8") as f:
    f.write("Product,Remaining Quantity\n")
    for product, qty in inventory.items():
        f.write(f"{product},{qty}\n")

print(f"Report saved to {report_file}")
