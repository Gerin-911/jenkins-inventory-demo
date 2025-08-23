import csv
import sys
sys.stdout.reconfigure(encoding='utf-8')

inventory_file = "inventory.txt"
orders_file = "orders.txt"

# Đọc dữ liệu kho
with open("orders.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue  # bỏ qua dòng trống
        parts = line.split(",")
        if len(parts) != 2:
            print(f"⚠️ Bỏ qua dòng không hợp lệ: {line}")
            continue
        product, qty = parts
        print(f"Trừ {qty} sản phẩm {product} trong kho")

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

