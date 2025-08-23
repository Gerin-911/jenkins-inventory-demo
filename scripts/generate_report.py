import csv
import os

inventory_file = "inventory.txt"   # hoặc đường dẫn thực tế
report_file = "reports/daily_report.csv"

# Tạo thư mục nếu chưa tồn tại
os.makedirs(os.path.dirname(report_file), exist_ok=True)

with open(inventory_file, "r", encoding="utf-8") as f:
    inventory = [line.strip().split(",") for line in f]

# Xuất báo cáo dạng CSV
with open(report_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Sản phẩm", "Số lượng còn lại"])
    writer.writerows(inventory)

print(f"Báo cáo đã tạo: {report_file}")
