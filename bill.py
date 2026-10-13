def total_calc(bill_amount, tip_percentage):
   total = bill_amount + (bill_amount * tip_percentage / 100)
   total = round(total, 2)
   print(f"Total amount to be paid: ${total}")

total_calc(100, 15)