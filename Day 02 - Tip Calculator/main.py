def tipcalculate(bill, tip):
  tip = (bill * tip) / 100
  return tip
def totalCalculate(bill, tip):
  tipcal = tipcalculate(bill, tip)
  return tipcal + bill
  
def main():
  bill = int(input("Enter total bill"))
  tip  = int(input("Enter tip in percentage %"))
  
  print("Total Bill: ", totalCalculate(bill, tip))
  
main()