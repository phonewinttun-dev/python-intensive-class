temp_celsius_input = float(input("Enter temperature in Celsius: "))
temp_fahrenheit = (temp_celsius_input * 9/5) + 32
print(f"Temperature in Fahrenheit: {temp_fahrenheit} °F")

temp_fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
temp_celsius = (temp_fahrenheit_input - 32) * 5/9
print(f"Temperature in Celsius: {temp_celsius} °C")
