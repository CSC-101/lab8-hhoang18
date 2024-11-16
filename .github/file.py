def main():
    filename = 'input'
    try:
        with open(filename,'r') as file:
            for line in file:
                two_parts = line.split()
                if len(two_parts) != 2:
                    print("Error: this line is missing a value.")
                    continue
                try: #converting to float
                    num1 = float(two_parts[0])
                    num2 = float(two_parts[1])
                    print("Sum:", num1+num2)
                except ValueError:
                    print("Error: this line has a value that could not be converted.")
    except FileNotFoundError:
        print("Error: the file cannot be found.")
        exit()
#the function's purpose is to open a file and read each line
#the function checks if there are two float values and converts them, then prints their sum
#the input is a file
#the output is the sum of the two float values for each line or an error message (if a line is missing a value,
#the file cannot be opened, or one of the values cannot be converted)
if __name__ == "__main__":
    main()