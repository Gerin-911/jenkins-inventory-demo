import os

inventory_file = "inventory.txt"
orders_file = "orders.txt"

# Đọc inventory hiện tại
inventory = {}
if os.path.exists(inventory_file):
    with open(inventory_file, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2:
                product, qty = parts
                inventory[product] = int(qty)

# Đọc đơn hàng và trừ kho
if os.path.exists(orders_file):
    with open(orders_file, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2:
                product, qty = parts
                qty = int(qty)
                if product in inventory:
                    inventory[product] -= qty
                else:
                    inventory[product] = -qty
                print(f"Trừ {qty} sản phẩm {product} trong kho")
            else:
                print(f"Bỏ qua dòng không hợp lệ: {line}")

# Ghi inventory trở lại file
with open(inventory_file, "w", encoding="utf-8") as f:
    for product, qty in inventory.items():
        f.write(f"{product},{qty}\n")
