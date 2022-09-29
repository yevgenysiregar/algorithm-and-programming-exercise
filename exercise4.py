#input time in seconds
timeInSeconds = int(input("Enter the number of time in seconds: "))

#formula for hour, minute and second
hour = timeInSeconds // 3600
minute = (timeInSeconds % 3600) // 60
second = timeInSeconds - ((hour * 3600) + (minute * 60))

#print output
print(f"Results: {hour}:{minute}:{second}")