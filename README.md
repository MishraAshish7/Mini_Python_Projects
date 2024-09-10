# Mini_Python_Projects

## Project 1: FinTrack Pro
FinTrack Pro is a powerful and user-friendly personal finance management tool designed to help you effortlessly track, analyze, and visualize your financial transactions. Whether you're managing your daily expenses or monitoring your income, FinTrack Pro makes it easy to keep your finances in check.

Key Features:

Seamless Data Entry: Add transactions with ease, including date, amount, category, and description. Ensure accurate records with built-in validation.
Comprehensive Summaries: View detailed summaries of your income and expenses over any date range to gain insights into your financial trends.
Interactive Visualizations: Choose from a variety of charts and graphs, including pie charts, line plots, and bar graphs, to visualize your spending patterns and financial health.
Flexible Date Handling: Specify any date range to analyze transactions and see summaries tailored to your financial timeline.
Whether you're tracking monthly budgets or analyzing long-term spending, FinTrack Pro offers a clear and intuitive way to manage your finances and make informed decisions about your money.


## Project 2: Ultimate Temperature Converter
Introduction:
Welcome to the Ultimate Temperature Converter, the comprehensive tool designed to make temperature conversions simple and efficient. Whether you're a student, a professional, or just someone in need of quick temperature conversions, this tool is here to help. With a user-friendly interface and vibrant color coding, our converter ensures a seamless experience from start to finish.

Key Features:
Multi-Scale Conversion: Convert temperatures between Celsius, Fahrenheit, and Kelvin with ease. Our tool supports six different conversion types, catering to a wide range of needs.

Color-Coded Prompts: Enjoy a visually engaging experience with color-enhanced prompts and results. The use of vibrant colors not only makes the interface more appealing but also helps in distinguishing different types of information quickly.

Error Handling: Built-in validation ensures that only valid numerical inputs are accepted. If an invalid entry is detected, you receive clear, color-coded feedback to correct your input.

User-Friendly Interface: The intuitive menu guides you through the conversion process step-by-step. Choose your desired conversion type, input the temperature, and get instant results in a format that's easy to understand.

Interactive Feedback: After each conversion, you have the option to perform another conversion or exit the application. The tool ensures that you can efficiently complete multiple conversions in one session.

Exit Confirmation: When you're done, a thoughtful exit message thanks you for using the service, adding a personal touch to your experience.

Whether you’re dealing with scientific data, cooking recipes, or everyday temperature readings, the Ultimate Temperature Converter is your reliable companion for accurate and hassle-free temperature conversions. Thank you for choosing our tool—experience precision and simplicity with every conversion!


 
## Project 3: Universal Weight Converter

Description:
The Universal Weight Converter is a versatile and user-friendly Python application designed to convert between various units of weight. This project offers both single and batch conversion modes, enabling users to seamlessly convert weights between grams, kilograms, pounds, and ounces.

Key Features:
   -- Single Weight Conversion: Allows users to convert individual weights between grams, kilograms, pounds, and ounces with ease.
   -- Batch Weight Conversion: Supports the conversion of multiple weights at once, facilitating bulk operations for users.
   -- User-Friendly Interface: Interactive command-line interface with clear prompts and colorful outputs for a pleasant user experience.
   -- Error Handling: Robust input validation ensures that users receive accurate results by preventing invalid inputs.


Supported Conversions:
1. Grams (g) to Kilograms (kg) and vice versa
2. Pounds (lb) to Kilograms (kg) and vice versa
3. Ounces (oz) to Grams (g) and vice versa
4. Pounds (lb) to Ounces (oz) and vice versa



## Project 4: Password Encryption and Decryption System

### Overview:
This repository contains a Python-based system for encrypting and decrypting passwords. The system uses custom salts and a character mapping approach to ensure secure encryption. It also includes functionality for decrypting the encrypted passwords by removing the added salts.

### Features:
- **Password Encryption**: Encrypts passwords using a custom character set and key mapping.
- **Password Decryption**: Decrypts encrypted passwords by removing salts and reversing the encryption process.
- **Custom Salts**: Adds extra obfuscation to encrypted passwords using a customizable salt list.

### Function Documentation:

#### `salts()`
**Purpose**: Generates a list of salt values used to obfuscate encrypted passwords.
**Returns**: 
- A list of strings, each representing a salt value.

#### `characters()`
**Purpose**: Provides a list of all possible characters that can be used in passwords.
**Returns**: 
- A list of characters including digits, letters, and punctuation.

#### `chars_keys()`
**Purpose**: Provides a list of keys corresponding to the characters defined in `characters()`.
**Returns**: 
- A list of keys.

#### `encrypter()`
**Purpose**: Encrypts a user-provided password using a defined character set and adds salt to the encrypted password.
Process:
1. Prompts user to enter a password to encrypt.
2. Encrypts the password using character mapping.
3. Adds salt to the encrypted password.

#### `decrypter()`
**Purpose**: Decrypts a user-provided hashed value by removing salt and reversing the encryption process.
Process:
1. Prompts user to enter a hashed password.
2. Removes salt from the hashed password.
3. Decrypts the resulting string.

## Example

**Encryption Example**:

Enter password to encrypt: abc456
Encrypted password: eV0!$z
Password after adding salt: 2jsa2aNVa7hBeV0NVaD1Bka8!$za2a2qB1.AlauA7cHOFI


**Decryption Example**:

step 1: Enter hashed value to Decrypt: 2jsa2aNVa7hBeV0NVaD1Bka8!$za2a2qB1.AlauA7cHOFI
step 1: Password after removing salt: eV0!$z
step 1: Decrypted password: abc456
