class Temperature:

    def __init__(self, userInput = 0):
        self.__celsius = userInput

    def setToCelsius(self, userInput):
        self.__celsius = userInput

    def setToFahrenheit(self, userInput):
        self.__celsius = (userInput * 9 / 5) + 32

    def setToKelvin(self, userInput):
        self.__celsius = userInput + 273.15

    def getToCelsius(self):
        return self.__celsius

    def getToFahrenheit(self):
        return (self.__celsius * 9 / 5) + 32

    def getToKelvin(self):
        return self.__celsius + 273.15

    def output(self):
        return "Celsius: " + str(self.getToCelsius()) + f"\N{DEGREE SIGN}C" + "\nFahrenheit: " + str(self.getToFahrenheit()) + f"\N{DEGREE SIGN}F" + "\nKelvin: " + str(self.getToKelvin()) + f"\N{DEGREE SIGN}K"





