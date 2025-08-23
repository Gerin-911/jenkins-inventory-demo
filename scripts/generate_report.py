import csv

inventory_file = "data/inventory.txt"
report_file = "reports/daily_report.csv"

with open(inventory_file, "r", encoding="utf-8") as f:
    inventory = [line.strip().split(",") for line in f]

# Xuất báo cáo dạng CSV
with open(report_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Sản phẩm", "Số lượng còn lại"])
    writer.writerows(inventory)

print(f"📊 Báo cáo đã tạo: {report_file}")

