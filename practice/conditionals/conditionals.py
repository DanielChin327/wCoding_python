print("Fizz Buzz")
number = input("Insert a number: ")

number = int(number)

def fizz_buzz(num):
    counter = 0
    while counter <= num:
        if counter % 3 == 0 and counter % 5 == 0:
            print("fizzbuzz")
            counter += 1
        elif counter % 3 == 0:
            print('fizz')
            counter += 1
        elif counter % 5 == 0:
            print('buzz')
            counter += 1
        else:
            print(counter)
            counter +=1

print(fizz_buzz(number))
