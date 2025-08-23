import csv

inventory_file = "data/inventory.txt"
orders_file = "data/orders.txt"

# Đọc dữ liệu kho
inventory = {}
with open(inventory_file, "r", encoding="utf-8") as f:
    for line in f:
        product, qty = line.strip().split(",")
        inventory[product] = int(qty)

# Đọc đơn hàng và trừ kho
with open(orders_file, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(",")
        if len(parts) == 3:
            _, product, qty = parts
            qty = int(qty)
            if product in inventory:
                inventory[product] -= qty

# Ghi lại kho mới
with open(inventory_file, "w", encoding="utf-8") as f:
    for product, qty in inventory.items():
        f.write(f"{product},{qty}\n")

print("✅ Đã cập nhật kho:", inventory)

