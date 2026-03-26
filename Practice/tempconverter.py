temperature = float(input("Enter a temperature in Celsius: "))
enter_unit = input("Enter the unit you want to convert to (F for Fahrenheit, K for Kelvin): ")
if enter_unit == "F":
    converted_temp = (temperature * 9/5) + 32
    print(f"{temperature} degrees Celsius is equal to {converted_temp} degrees Fahrenheit.")
elif enter_unit == "K":
    converted_temp = temperature + 273.15
    print(f"{temperature} degrees Celsius is equal to {converted_temp} Kelvin.")
else:
    print("Invalid unit entered. Please enter 'F' for Fahrenheit or 'K' for Kelvin.")