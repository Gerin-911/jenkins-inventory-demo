import os

# File nằm cùng cấp với workspace
inventory_file = "inventory.txt"
report_file = "report.txt"  # cùng cấp với inventory.txt và orders.txt

# Đọc dữ liệu inventory
inventory = {}
with open(inventory_file, "r", encoding="utf-8") as f:
    for line in f:
        product, qty = line.strip().split(",")
        inventory[product] = int(qty)

# Ghi báo cáo, ghi đè mỗi lần chạy
with open(report_file, "w", encoding="utf-8") as f:
    f.write("Sản phẩm | Số lượng còn lại\n")
    f.write("-" * 30 + "\n")
    for product, qty in inventory.items():
        f.write(f"{product} | {qty}\n")

print(f"Báo cáo đã tạo/ghi đè: {os.path.abspath(report_file)}")
