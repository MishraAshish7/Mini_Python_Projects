# colorama is used to add different colors to our texts to enhance the user-experiences
from colorama import Fore, Style, init


init(autoreset=True)
def Temperature_Coverter():

    # Creating prompt to take numbers which is going to be converted
    def number():
        while True:
            try:
                num = float(input(Fore.LIGHTGREEN_EX + "Enter temperature to convert: " + Style.RESET_ALL))
                return num
            except ValueError as e:
                print(Fore.RED + "Please enter a valid number only" + Style.RESET_ALL)

    # Case 1: Celsius to Fahrenheit Conversion
    def celsius_To_Fahrenheit():
        num = number()
        result = (num * 9 / 5) + 32
        print(Fore.GREEN + f"Your result is {result:.2f}°F" + Style.RESET_ALL)

    # Case 2: Celsius to Kelvin Conversion
    def Celsius_to_Kelvin():
        num = number()
        result = num + 273.15
        print(Fore.GREEN + f"Your result is {result:.2f} K" + Style.RESET_ALL)

    # Case 3: Fahrenheit to celsius Conversion
    def Fahrenheit_to_celsius():
        num = number()
        result = (num - 32) * 5 / 9
        print(Fore.GREEN + f"Your result is {result:.2f}°C" + Style.RESET_ALL)

    # Case 4: Fahrenheit to Kelvin Conversion
    def Fahrenheit_to_Kelvin():
        num = number()
        result = (num + 459.67) * 5 / 9
        print(Fore.GREEN + f"Your result is {result:.2f} K" + Style.RESET_ALL)

    # Case 5: Kelvin to Celsius Conversion
    def Kelvin_to_Celsius():
        num = number()
        result = num - 273.15
        print(Fore.GREEN + f"Your result is {result:.2f}°C" + Style.RESET_ALL)

    # Case 6: Kelvin to Fahrenheit Conversion
    def Kelvin_to_Fahrenheit():
        num = number()
        result = (num * 9 / 5) - 459.67
        print(Fore.GREEN + f"Your result is {result:.2f}°F" + Style.RESET_ALL)

    # Main functions that prints outputs as per conditions
    def main():
        while True:

            # Printing options for users
            print(Fore.LIGHTGREEN_EX + "-----------------Welcome to Ultimate Temperature Converter-----------------" + Style.RESET_ALL)
            print(Fore.CYAN + "1. Celsius to Fahrenheit\n2. Celsius to Kelvin\n3. Fahrenheit to Celsius\n4. Fahrenheit to Kelvin" + Style.RESET_ALL)
            print(Fore.CYAN + "5. Kelvin to Celsius\n6. Kelvin to Fahrenheit\n7. Exit" + Style.RESET_ALL)

            # Taking user inputs
            user_choice = input(Fore.BLUE + "Please Enter your choice (1-7): " + Style.RESET_ALL).strip()

            if user_choice == "1":
                celsius_To_Fahrenheit()
            elif user_choice == "2":
                Celsius_to_Kelvin()
            elif user_choice == "3":
                Fahrenheit_to_celsius()
            elif user_choice == "4":
                Fahrenheit_to_Kelvin()
            elif user_choice == "5":
                Kelvin_to_Celsius()
            elif user_choice == "6":
                Kelvin_to_Fahrenheit()
            elif user_choice == "7":
                print(Fore.MAGENTA + "Thanks for using our service! We hope you liked it." + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "Please enter an valid choice (1-7)" + Style.RESET_ALL)
                continue

            # Asking user if he wants to do one more conversion
            if input(Fore.BLUE + "Do you wanna do one more conversion?(yes/no): " + Style.RESET_ALL).strip().lower() != "yes":
                print(Fore.MAGENTA + "Thanks for using our service! We hope you liked our service" + Style.RESET_ALL)
                break
    main()
Temperature_Coverter()
