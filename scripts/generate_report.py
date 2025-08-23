import csv
import os

inventory_file = "inventory.txt"
report_file = "report.txt"  # nằm cùng cấp với inventory.txt

# Đọc inventory
inventory = []
if os.path.exists(inventory_file):
    with open(inventory_file, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2:
                inventory.append(parts)

# Ghi báo cáo
with open(report_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Remaining Quantity"])  # đổi tiêu đề sang ASCII
    writer.writerows(inventory)

print(f"Report has been created: {report_file}")  # đổi thông báo sang ASCII
