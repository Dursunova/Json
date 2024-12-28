import json
import math

with open('laptops.json', 'r') as file:
    laptops = json.load(file)


touch_screen_count = sum(1 for laptop in laptops if laptop.get("Touch Screen", False))


total_laptops = len(laptops)


touch_screen_percentage = (touch_screen_count / total_laptops) * 100 if total_laptops > 0 else 0

matching_laptops = [
    laptop for laptop in laptops
    if ("512GB SSD" in laptop.get("Product Name", "") or "512GB" in laptop.get("Product Name", "")) and 
    ("16GB" in laptop.get("Product Name", "")) and 
    ("1TB" in laptop.get("Product Name", ""))
]


min_specs_laptop = min(laptops, key=lambda x: (int(x.get("Battery Life (up to hours)", 0)), x.get("Size", "0")))

unique_brands = {laptop["Brand"] for laptop in laptops}


brand_counts = {}
for laptop in laptops:
    brand = laptop["Brand"]
    brand_counts[brand] = brand_counts.get(brand, 0) + 1
most_common_brand = max(brand_counts, key=brand_counts.get)


most_common_brand_count = brand_counts[most_common_brand]


large_screen_laptops_count = sum(1 for laptop in laptops if float(laptop["Size"].replace("inch", "").strip()) > 17)


iball_battery_lives = [int(laptop["Battery Life (up to hours)"]) for laptop in laptops if laptop["Brand"] == "iBall"]
average_iball_battery_life = sum(iball_battery_lives) / len(iball_battery_lives) if iball_battery_lives else 0


unique_windows_versions = {laptop["Operating system"] for laptop in laptops}


print(f"Touch screen olan notbukların faizi: {math.ceil(touch_screen_percentage)}%")
print("\nSSD = 512GB, RAM = 16GB, Sərt disk = 1TB olan notbuklar:")
for laptop in matching_laptops:
    print(f"- {laptop['Product Name']} | Link: {laptop.get('link', 'N/A')}")

print(f"\nƏn az texniki xüsusiyyətlərə malik notbuk: {min_specs_laptop['Product Name']}")

print(f"\nFaylda {len(unique_brands)} müxtəlif notbuk markası təmsil olunur.")
print(f"\nDaha çox yayılmış marka: {most_common_brand} | Görünmə sayı: {most_common_brand_count}")

print(f"\nEkranın diametri 17 düymdən çox olan {large_screen_laptops_count} notbuk var.")

print(f"\n'iBall' notbukları üçün orta batareya ömrü: {average_iball_battery_life:.2f} saat.")

print(f"\nFaylda Windows-un {len(unique_windows_versions)} müxtəlif versiyası təqdim olunub.")