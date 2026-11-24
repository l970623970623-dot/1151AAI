
usage = int(input())

# Calculate tiered electricity fee based on consumption brackets
if usage <= 120:
    bill = usage * 2.10
elif usage <= 500:
    bill = 120 * 2.10 + (usage - 120) * 3.02
else:
    bill = 120 * 2.10 + (500 - 120) * 3.02 + (usage - 500) * 4.39

# Round to 1 decimal place (adding 1e-9 avoids floating-point precision issues)
bill_rounded = round(bill + 1e-9, 1)

# Output formatted string with 'NT$' prefix and 1 decimal place
print(f"NT${bill_rounded:.1f}")
