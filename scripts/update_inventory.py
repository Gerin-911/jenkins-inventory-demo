import os

# Đường dẫn file (nằm cùng workspace)
inventory_file = "inventory.txt"
orders_file = "orders.txt"

# Khởi tạo dictionary rỗng
inventory = {}

# Đọc file inventory.txt
if os.path.exists(inventory_file):
    with open(inventory_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                product, qty = line.split(",")
                inventory[product] = int(qty)
            except ValueError:
                print(f"Bỏ qua dòng không hợp lệ trong inventory: {line}")
else:
    print(f"File {inventory_file} không tồn tại!")

# Đọc file orders.txt và trừ kho
if os.path.exists(orders_file):
    with open(orders_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                product, qty = line.split(",")
                qty = int(qty)
                if product in inventory:
                    inventory[product] -= qty
                else:
                    print(f"Sản phẩm {product} không có trong kho, bỏ qua")
                print(f"Trừ {qty} sản phẩm {product} trong kho")
            except ValueError:
                print(f"Bỏ qua dòng không hợp lệ trong orders: {line}")
else:
    print(f"File {orders_file} không tồn tại!")

# In inventory hiện tại
print("\nKho hiện tại:")
for product, qty in inventory.items():
    print(f"{product}: {qty} còn lại")
