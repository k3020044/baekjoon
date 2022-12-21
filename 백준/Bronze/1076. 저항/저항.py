resistor = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

first = input()
second = input()
third = input()

value = str(resistor.index(first)) + str(resistor.index(second))

print(int(value) * (10**resistor.index(third)))