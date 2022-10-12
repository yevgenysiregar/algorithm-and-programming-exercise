#input amount of bill
billAmount = float(input("Enter the amount of bill(USD): "))

#input amount of people
totalPerson = int(input("Enter the amount of people: "))

#input amount of tips
totalTips = float(input("Enter the amount of tips(%): "))

#formula for bill per person and tips per person
totalBillPerPerson = ((((billAmount * totalTips) / 100) + billAmount) / totalPerson)
tipsPerPerson = totalTips /5 * totalPerson

#print output
print(f"Total bill per person(USD): {totalBillPerPerson}")
print(f"Tips per person(%): {tipsPerPerson}")