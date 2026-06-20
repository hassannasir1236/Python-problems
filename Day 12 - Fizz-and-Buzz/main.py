getInput = int(input("Enter a number: "))

if getInput % 3 == 0 and getInput % 5 == 0:
    print("FizzBuzz")
elif getInput % 3 == 0:
    print("Fizz")
elif getInput % 5 == 0:
    print("Buzz")
else:
    print(getInput)