# Split The Bill
# Use a list to calculate the amount of the bill, then divide it 4 ways

bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]

if len(bill) == 0 or bill == 0:
  print("The bill list is empty, no average to calculate.")
else:
    total_bill = 0
    for item in bill:
        total_bill += item

    my_share = total_bill / 4
    print(f"£{my_share:.2f}")