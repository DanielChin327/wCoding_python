
def input_temp():
    while True:
        temp = input("Insert a temperature: ")
        temp = int(temp)
        print(type(temp))
        if type(temp) ==  int:
            return temp
        else:
            print(f"invalid input. You put {temp}. Type a number")

def check_type():
    while True:
        type = input("Is this Celsius or Farenheit? (c / f): ")
        type = type.lower()
        if type == 'c' or type == 'f':
            return type
        else:
            print(f"invalid input. You put {type}. Choose c or f")

def convert_temp(temp, type):
    if type == 'c':
        return f"The degree in f is : {((temp * 9/5) + 32)}"
    elif type == 'f':
        return f"The degree in c is : {((temp - 32) * (5/9))}"
    else:
        return "invalid input"

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
