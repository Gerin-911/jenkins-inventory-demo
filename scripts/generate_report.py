import os
import csv

inventory_file = "inventory.txt"  # đường dẫn mới
report_dir = "reports"
os.makedirs(report_dir, exist_ok=True)  # tạo thư mục nếu chưa có
report_file = os.path.join(report_dir, "daily_report.csv")

with open(inventory_file, "r", encoding="utf-8") as f:
    inventory = [line.strip().split(",") for line in f]

# Tạo báo cáo CSV
with open(report_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Sản phẩm", "Số lượng còn lại"])
    writer.writerows(inventory)

print(f"📊 Báo cáo đã tạo: {report_file}")
