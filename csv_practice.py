# Reflection 1:
# Python can read, change, and organize large amounts of data automatically.
# Excel is easier for manually editing data and making charts, but Python is better for repeating tasks.

# Reflection 2:
# A business could use an append-mode log to record each sale made during the day.
# Append mode is useful because it adds new records without deleting the previous records.

import csv
from datetime import datetime

# EXERCISE 1: Setup
# The sales file is stored inside the data folder.
file_path = "data/sales.csv"


# EXERCISE 2: Read and print raw rows
print("\nEXERCISE 2: Raw CSV Rows")

with open(file_path, "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# EXERCISE 3: Skip the header
print("\nEXERCISE 3: Skip the Header")

with open(file_path, "r", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)


# EXERCISE 4: Compute totals
print("\nEXERCISE 4: Compute Totals")

total_revenue = 0

with open(file_path, "r", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")


# EXERCISE 5: Filter and write
print("\nEXERCISE 5: Filter and Write")

original_count = 0
written_count = 0

with open(file_path, "r", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)

    with open("data/cleaned.csv", "w", newline="") as output_file:
        writer = csv.writer(output_file)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, round(total, 2)])
                written_count += 1

print("Original rows:", original_count)
print("Rows written:", written_count)


# EXERCISE 6: csv.DictReader
print("\nEXERCISE 6: DictReader")

dict_total_revenue = 0

with open(file_path, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total_revenue += total

        print(f"{product}: ${total:.2f}")

print(f"DictReader total revenue: ${dict_total_revenue:.2f}")

# csv.reader uses column positions, so it is useful for simple CSV files.
# DictReader uses column names, so it is easier to understand when there are many columns.


# EXERCISE 7: Sales summary by product
print("\nEXERCISE 7: Sales Summary")

sales_summary = {}

with open(file_path, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")


# EXERCISE 8: Append Mode Log
print("\nEXERCISE 8: Run Log")

current_time = datetime.now()

with open("data/run_log.txt", "a") as log_file:
    log_file.write(
        f"{current_time} - Total Revenue: ${total_revenue:.2f}\n"
    )

print("Run log updated successfully.")