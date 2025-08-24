import os

inventory_file = "inventory.txt"
letter_file = "letter.txt"
target_qty = 100

# Doc inventory
items_to_order = []

if os.path.exists(inventory_file):
    with open(inventory_file, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2:
                item_name, qty_str = parts
                try:
                    qty = int(qty_str)
                    if qty < target_qty:
                        need = target_qty - qty
                        items_to_order.append((item_name, need))
                except ValueError:
                    continue

# Tao noi dung thu duy nhat
if items_to_order:
    letter_content = "Chao nha cung cap,\n\n"
    letter_content += f"Ben toi can bo sung cac san pham sau de duy tri ton kho {target_qty}:\n\n"

    for item, need in items_to_order:
        letter_content += f"- {item}: {need} cai\n"

    letter_content += "\nMong quy cong ty ho tro.\n\nTran trong,\nInventory Team"

    with open(letter_file, "w", encoding="utf-8") as f:
        f.write(letter_content)

    print(f"Letter has been generated and saved in {letter_file}")
else:
    print("Tat ca san pham deu >= 100. Khong can tao thu.")
