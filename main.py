#Instruction for overall program
print("Please input the following price per item:")

#Input burger price
burgerPrice = int(input("Enter burger selling prices: "))

#Input soda price
sodaPrice = int(input("Enter soda selling price: "))

#Input combo meal price
comboMeal = int(input("Enter combo meal selling price: "))

#Calculation for fixed profit
fixedProfit = (burgerPrice + sodaPrice) - comboMeal

#print output
print(f"Fixed profit: {fixedProfit}")

