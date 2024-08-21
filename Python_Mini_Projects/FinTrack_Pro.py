from datetime import date
import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns

def FinTrack_Pro():
    def new_transact():

        val_mail = "@gmail.com"
        file_name = "latest_proj.csv"

        # Opening the file in append mode
        with open(file_name, mode="a", newline="") as file:
            writer = csv.writer(file)

            while True:
                # Getting user input to saved in database/ csv file
                date_ = input("Enter the date (dd/mm/yyyy) or press enter for today: ")
                if date_ == "":
                    date_ = date.today()

                f_name = input("Enter your first name: ").title()
                l_name = input("Enter your last name: ").title()

                while True:
                    email = input("Enter your email: ")
                    if not email.endswith(val_mail):
                        print("Enter valid mail (e.g. exam@gmail.com)")
                    else:
                        break

                while True:
                    try:
                        amt = float(input("Enter the Amount: "))
                        break
                    except ValueError as e:
                        print("Warning! Amount can't be a word or alphabet")

                while True:
                    cate = input("Enter the Category (I for Income, E for Expense): ")
                    if cate == "":
                        print("Category can't be null value")
                    elif cate == "i":
                        cate = "Income"
                        break
                    elif cate == "e":
                        cate = "Expense"
                        break
                    else:
                        cate = "Others"
                        break

                desc = input("Enter description (optional): ")

                # Preparing data as a list
                data = [date_, f_name, l_name, email, amt, cate, desc]

                # Writing data to csv file
                writer.writerow(data)

                # Asking user if he wants to more data
                if input("Wanna add some more entry? ").lower() != "yes":
                    break
        print("Data added successfully man!")



    def view_tranSuminRange():

        # importing data
        data = pd.read_csv("latest_proj.csv")
        df = pd.DataFrame(data)

        # converting data date to date format
        df["Date"] = pd.to_datetime(df["Date"], format="mixed")

        # asking user the range of data he wants
        # Entering start date
        while True:
            try:
                start_date_str = input("Enter the start date (dd-mm-yyyy): ").strip()
                end_date_str = input("Enter the end date (dd-mm-yyyy): ").strip()

                # Convert user input to datetime
                start_date = pd.to_datetime(start_date_str, format="%d-%m-%Y")
                end_date = pd.to_datetime(end_date_str, format="%d-%m-%Y")

                if start_date > end_date:
                    print("Start date cannot be after end date. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid date format. Please use dd-mm-yyyy.")


        # Preparing data to return
        user_data = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

        # Summary Part
        # Preparing data for income
        for_income = df[df["Category"] == "Income"]
        income = sum(for_income["Amount"])

        # Preparing data for expense
        for_expense = df[df["Category"] == "Expense"]
        expense = sum(for_expense["Amount"])

        # Net savings
        saving = income - expense

        # Returning data
        print(user_data)

        print("\nSummary:")
        print(f"Total Income: ${income}")
        print(f"Total Expenses: ${expense}")
        print(f"Net Savings: ${saving}")


        # Data preparation for pie chart/ bar graph
        pie_data = df.groupby('Category')["Amount"].sum()


        # Asking user if he wants a graph
        ask_graph = input("Would you like to see a plot/graph?").lower()
        if ask_graph == "yes":

            #Asking user what type og graph he wants
            while True:
                try:
                    ask_type = int(input("Which type of graph do you want to see? "))
                    print("1. Pie chart\n2. Line plot\n3. Bar graph")
                    break
                except ValueError as e:
                    print("Enter only in numbers")

            # Case 1: Pie chart
            if ask_type == 1:
                plt.pie(pie_data, autopct="%1.1f%%", startangle= 140, wedgeprops={'edgecolor': 'black'}, labels=pie_data.index)
                plt.title("Percentage of Expenses or Incomes", fontsize= 16, fontweight= "bold", color= "black")
                plt.axis("equal")
                plt.tight_layout()
                plt.show()

            #Case 2: Line Plot
            elif ask_type == 2:
                sns.lineplot(x= for_income["Date"], y= for_income["Amount"], marker="o", label= "Income")
                sns.lineplot(x= for_expense["Date"], y=for_expense["Amount"], marker="o", label= "Expense")
                plt.title("Income and Expense Over Time")
                plt.xlabel("Date")
                plt.ylabel("Amount")
                plt.legend()
                plt.xticks(rotation= 35)
                plt.grid(True)
                plt.show()

            # Case 1: Bar graph
            elif ask_type == 3:
                plt.bar(pie_data.index, pie_data.values)
                plt.xlabel("Category", fontsize= 14, fontweight= "bold", color= "black")
                plt.ylabel("Amount", fontsize=14, fontweight="bold", color="black")
                plt.title("Amount spend by category", fontsize=16, fontweight="bold", color="black")
                plt.xticks(rotation= 35)
                plt.grid(True, linestyle= "--", alpha= 0.7)
                plt.tight_layout()
                plt.show()

            else:
                print("Thanks for using our service!")


    def main_body():
        while True:
            # Providing options to users
            print("-----------------FinTrack Pro-----------------")
            print("Welcome to FinTrack Pro my friend:")
            print("1. Add a new transaction")
            print("2. View transactions and summary within a date range")
            print("3. Know about FinTrack Pro")
            print("4. Exit")

            # user choice
            us_choice = input("Enter your choice: ")

            # Executing commands on each conditions
            if us_choice == "1":
                new_transact()
            elif us_choice == "2":
                view_tranSuminRange()
            elif us_choice == "3":
                print("----------------- FinTrack Pro -----------------")
                print("""
                Welcome to **FinTrack Pro**, the ultimate personal finance management tool designed to simplify tracking, analyzing, and visualizing your financial transactions.
                    **Key Features:**
                    - **Seamless Data Entry:** Easily add transactions with details such as date, amount, category, and description. Enjoy accurate record-keeping with built-in validation.
                    - **Comprehensive Summaries:** Gain valuable insights with detailed summaries of your income and expenses over any date range. Understand your financial trends at a glance.
                    - **Interactive Visualizations:** Visualize your spending patterns and financial health with a variety of charts and graphs, including pie charts, line plots, and bar graphs.
                    - **Flexible Date Handling:** Analyze transactions and view summaries based on any date range that suits your needs.

                Whether you're budgeting monthly or analyzing long-term spending, FinTrack Pro provides a clear, intuitive interface to help you manage your finances and make informed decisions.
                Discover how easy it is to take control of your finances with FinTrack Pro!
                """)

            elif us_choice == "4":
                break
            else:
                print("Invalid choice. Please select a valid option.")

    main_body()

FinTrack_Pro()
