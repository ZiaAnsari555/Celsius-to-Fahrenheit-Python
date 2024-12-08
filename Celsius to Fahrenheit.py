def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_celsius = float(input("Enter temperature in Celsius: "))
print(f"{temp_celsius}°C is {celsius_to_fahrenheit(temp_celsius)}°F")
