matrixInput = eval(input("Enter a matrix: "))

matrixResult = [[matrixInput[j][i] for j in range(len(matrixInput))] for i in range(len(matrixInput[0]))]

print(matrixResult)