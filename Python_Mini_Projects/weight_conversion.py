from colorama import Fore, Style, init
init(autoreset=True)


def single_weight_conversion():

    # Taking user weights to convert
    def user_units():
        while True:
            try:
                user_unit = float(input(Fore.LIGHTGREEN_EX + "Enter your weights to convert: " + Style.RESET_ALL))
                return user_unit
            except ValueError as e:
                print(Fore.RED + "Please enter your weights only in numbers nor strings" + Style.RESET_ALL)

    # Condition for choice 1
    def gram_to_kg():
        user_unit = user_units()
        result = user_unit * 0.001
        print(Fore.GREEN + f"Your weight in Kilograms is {result:.2f} kg" + Style.RESET_ALL)

    # Condition for choice 2
    def kg_to_grams():
        user_unit = user_units()
        result = user_unit * 1000
        print(Fore.GREEN + f"Your weight in grams is {result:.2f} g" + Style.RESET_ALL)

    # Condition for choice 3
    def pounds_to_kg():
        user_unit = user_units()
        result = user_unit * 0.453592
        print(Fore.GREEN + f"Your weight in Kilograms is {result:.2f} kg" + Style.RESET_ALL)

    # Condition for choice 4
    def kg_to_pounds():
        user_unit = user_units()
        result = user_unit * 2.20462
        print(Fore.GREEN + f"Your weight in Pounds is {result:.2f} lb" + Style.RESET_ALL)

    # Condition for choice 5
    def ounces_to_grams():
        user_unit = user_units()
        result = user_unit * 28.3495
        print(Fore.GREEN + f"Your weight in grams is {result:.2f} g" + Style.RESET_ALL)

    # Condition for choice 6
    def grams_to_ounces():
        user_unit = user_units()
        result = user_unit * 0.035274
        print(Fore.GREEN + f"Your weight in Ounces is {result:.2f} oz" + Style.RESET_ALL)

    # Condition for choice 7
    def pounds_to_ounces():
        user_unit = user_units()
        result = user_unit * 16
        print(Fore.GREEN + f"Your weight in Ounces is {result:.2f} oz" + Style.RESET_ALL)

    # Condition for choice 8
    def ounces_to_pounds():
        user_unit = user_units()
        result = user_unit * 0.0625
        print(Fore.GREEN + f"Your weight in Pounds is {result:.2f} lb" + Style.RESET_ALL)


    def main():
        print(Fore.LIGHTGREEN_EX + "---------------Welcome to weight converter---------------\n---------------Let's view your weights in other units---------------" + Style.RESET_ALL)
        # giving options to users
        print(Fore.CYAN +
            "1. Grams(g) to Kilograms(kg)\n2. KiloGrams(kg) to grams(g)\n3. Pounds(lb) to Kilograms(kg)\n4. Kilograms(kg) to Pounds(lb)" + Style.RESET_ALL)
        print(Fore.CYAN +
            "5. Ounces(oz) to Grams(g)\n6. Grams(g) to Ounces(oz)\n7. Pounds(lb) to Ounces(oz)\n8. Ounces(oz) to Pounds(lb)\n9. Exit" + Style.RESET_ALL)

        while True:

            # Taking user inputs
            usin = input(Fore.BLUE + "Enter your choice baby(1-9): " + Style.RESET_ALL)

            # Condition for grams to kg
            if usin == "1":
                gram_to_kg()
            # Condition for kg to grams
            elif usin == "2":
                kg_to_grams()
            # Condition for pounds to kg
            elif usin == "3":
                pounds_to_kg()
            # Condition for kg to pounds
            elif usin == "4":
                kg_to_pounds()
            # Condition for ounces to grams
            elif usin == "5":
                ounces_to_grams()
            # Condition for grams to ounces
            elif usin == "6":
                grams_to_ounces()
            # Condition for pounds to ounces
            elif usin == "7":
                pounds_to_ounces()
            # Condition for ounces to pounds
            elif usin == "8":
                ounces_to_pounds()
            # Condition for if user wants to exit
            elif usin == "9":
                print(Fore.MAGENTA + "Thanks! For using our service\nWe hope it helped you" + Style.RESET_ALL)
                break
            # Condition for irrelevant user choice
            else:
                print(Fore.RED + "Please enter a valid choice" + Style.RESET_ALL)
                continue

            if input(Fore.BLUE + "Do you wanna convert more weights?(yes/no): " + Style.RESET_ALL).strip().lower() != "yes":
                print(Fore.MAGENTA + "Thanks for using our service! We hope you liked it" + Style.RESET_ALL)
                break

    main()



# Weight conversion in group
def group_of_weight_convert():
    #Taking bunch of weights
    def group_of_weights_from_user():
        while True:
            try:
                user_inputs = input(Fore.LIGHTBLUE_EX + "Enter group of weights(e.g. 10,20,25): " + Style.RESET_ALL)
                # Stripping the extra comma's
                strip_comma = user_inputs.strip(",")
                # Splitting values by comma(,)
                list_of_weight = strip_comma.split(",")
                # Converting list values to float from list by appending values one by one
                float_weights = []
                for i in list_of_weight:
                    float_weights.append(float(i))
                print("Your entered weights are:", float_weights)
                return float_weights
            except ValueError as e:
                print(Fore.RED + "Don't try to make us fool man! Weight can't be an alphabets" + Style.RESET_ALL)

    # Condition for choice 1
    def gms_to_kg():
        weights = group_of_weights_from_user()
        for i in weights:
            print(i,"gms =", i * 0.001,"kg")

    # Condition for choice 2
    def kg_to_gms():
        weights = group_of_weights_from_user()
        for i in weights:
            print(i,"kg =", i * 1000,"gms")

    # Condition for choice 3
    def lb_to_kg():
        weights = group_of_weights_from_user()
        for i in weights:
            print(i,"lbs =", i * 0.453592,"kg")

    # Condition for choice 4
    def kg_to_lb():
        weights = group_of_weights_from_user()
        for i in weights:
            print( i,"kg =", i * 2.20462,"lbs")

    # Condition for choice 5
    def oz_to_gms():
        weights = group_of_weights_from_user()
        for i in weights:
            print( i,"oz =", i * 28.3495,"gms")

    # Condition for choice 6
    def gms_to_oz():
        weights = group_of_weights_from_user()
        for i in weights:
            print( i,"gms =", i * 0.035274,"oz")

    # Condition for choice 7
    def lb_to_oz():
        weights = group_of_weights_from_user()
        for i in weights:
            print( i,"lbs =", i * 16,"oz")

    # Condition for choice 8
    def oz_to_lb():
        weights = group_of_weights_from_user()
        for i in weights:
            print( i,"oz =", i * 0.0625,"lbs" )

    def main():

        # giving options to users
        print(Fore.CYAN +
            "1. Grams(g) to Kilograms(kg)\n2. KiloGrams(kg) to grams(g)\n3. Pounds(lb) to Kilograms(kg)\n4. Kilograms(kg) to Pounds(lb)" + Style.RESET_ALL)
        print(Fore.CYAN +
            "5. Ounces(oz) to Grams(g)\n6. Grams(g) to Ounces(oz)\n7. Pounds(lb) to Ounces(oz)\n8. Ounces(oz) to Pounds(lb)\n9. Exit" + Style.RESET_ALL)

        while True:

            # Taking user inputs
            usin = input(Fore.BLUE + "Enter your choice baby(1-9): " + Style.RESET_ALL)

            # Condition for grams to kg
            if usin == "1":
                gms_to_kg()
            # Condition for kg to grams
            elif usin == "2":
                kg_to_gms()
            # Condition for pounds to kg
            elif usin == "3":
                lb_to_kg()
            # Condition for kg to pounds
            elif usin == "4":
                kg_to_lb()
            # Condition for ounces to grams
            elif usin == "5":
                oz_to_gms()
            # Condition for grams to ounces
            elif usin == "6":
                gms_to_oz()
            # Condition for pounds to ounces
            elif usin == "7":
                lb_to_oz()
            # Condition for ounces to pounds
            elif usin == "8":
                oz_to_lb()
            # Condition for if user wants to exit
            elif usin == "9":
                print(Fore.MAGENTA + "Thanks! For using our service\nWe hope it helped you" + Style.RESET_ALL)
                break
            # Condition for irrelevant user choice
            else:
                print(Fore.RED + "Please enter a valid choice" + Style.RESET_ALL)
                continue

            if input(Fore.BLUE + "Do you wanna convert more weights?(yes/no): " + Style.RESET_ALL).strip().lower() != "yes":
                print(Fore.MAGENTA + "Thanks for using our service! We hope you liked it" + Style.RESET_ALL)
                break

    main()


def main_application():
    print("1. Single Weight Converter\n2. Group Weight Converter\n3. Exit")
    while True:
        usin = input("Enter your choice(1-3)(3-Exit): ")

        if usin == "1":
            single_weight_conversion()
        elif usin == "2":
            group_of_weight_convert()
        elif usin == "3":
            print("Thanks for using our service! We hope you liked it!")
            break
        else:
            print("Please enter a valid choice(1-3)")
            continue
main_application()

