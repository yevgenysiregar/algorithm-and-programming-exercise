from Temperature import Temperature

def main():
    output = Temperature(float(input("Enter temperature: ")))
    print(output.output())

if __name__ == "__main__":
    main()