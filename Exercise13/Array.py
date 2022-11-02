class Array:

    def __init__(self, number):
        self.__number = number

arr = ["zero", "one", "two", "three", "four"]

print(arr[0])
arr.append("five")
arr.pop()
arr.extend(["five", "six", "seven"])
arr.insert(8, "eight")
arr.index("zero")
print(len(arr))