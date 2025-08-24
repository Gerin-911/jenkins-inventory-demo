import os

inventory_file = "inventory.txt"
letter_file = "letter.txt"

def generate_supplier_letter(item_name, current_qty, target_qty=100):
    return f"""
Subject: Request for Stable Supply of {item_name}

Dear Supplier,

I hope this message finds you well.

Our current stock for **{item_name}** is only {current_qty} units.
We kindly request your support to ensure that our inventory is
always maintained at a minimum of {target_qty} units.

Please arrange for regular supply to keep our stock stable.

Thank you very much for your cooperation.

Best regards,
Inventory Management Team
"""

letters = []

# Đọc file inventory.txt (giả sử mỗi dòng có dạng: item_name,quantity)
if os.path.exists(inventory_file):
    with open(inventory_file, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2:
                item_name, qty_str = parts
                try:
                    qty = int(qty_str)
                    if qty < 100:
                        letters.append(generate_supplier_letter(item_name, qty))
                except ValueError:
                    continue

# Ghi tất cả thư vào file letter.txt
if letters:
    with open(letter_file, "w", encoding="utf-8") as f:
        for letter in letters:
            f.write(letter)
            f.write("\n" + "="*50 + "\n\n")  # phân cách giữa các thư
    print(f"Letters have been generated and saved in {letter_file}")
else:
    print("All items are stable (>= 100). No letters needed.")
