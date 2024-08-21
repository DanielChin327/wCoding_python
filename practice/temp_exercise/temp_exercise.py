
def input_temp():
    while True:
        temp = input("Insert a temperature: ")
        try:
            temp = int(temp)
            return temp
        except ValueError:
            print(f"Invalid input. You wrote ${temp}")

def check_type():
    while True:
        type = input("Is this Celsius or Farenheit? (type c or f): ")
        if type == 'c' or type == 'f':
            return type
        else:
            print(f"invalid input. You put {type}. Choose c or f")

def convert_temp(temp, type):
    if type == 'c':
        return f"The degree in f is : {round((temp * 9/5) + 32, 2)}"
    elif type == 'f':
        return f"The degree in c is : {round((temp - 32) * (5/9, 2))}"
    else:
        return "invalid input"

def start():
    while True:
        temp = input_temp()
        type = check_type()
        converted = convert_temp(temp, type)
        print(f"{converted}\n")
        again = input("Press any key to check another temp. Otherwise type 'quit' to stop.\n")
        again = again.lower()
        if again == 'quit':
            print("Have a Nice Day!")
            break

start()
