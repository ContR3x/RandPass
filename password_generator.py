import random
import string

# Project Title: Random Password Generator Tool

def generate_char_password(length=8, use_uppercase=True, use_digits=True, use_symbols=True):
    if length < 8 or length > 60:
        raise ValueError("Password length must be between 8 and 60 characters.")
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    symbols = '@!&*' if use_symbols else ''
    
    all_characters = lowercase_letters + uppercase_letters + digits + symbols
    
    if not all_characters:
        raise ValueError("You must include at least one character set.")
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def generate_word_password(num_words=3, separator='_', use_uppercase=True, use_digits=True):
    if num_words < 3 or num_words > 10:
        raise ValueError("Number of words must be between 3 and 10.")
    
    # Generate random words using uppercase letters
    words = [''.join(random.choices(string.ascii_uppercase, k=random.randint(3, 5))) for _ in range(num_words)]

    # Mix words with numbers
    for i in range(len(words)):
        if use_digits:
            if random.choice([True, False]):  # Randomly decide whether to add a digit
                digit = random.choice(string.digits)
                position = random.randint(0, len(words[i]))  # Select random position for the digit
                words[i] = words[i][:position] + digit + words[i][position:]

    password = separator.join(words)
    return password

def main():
    while True:
        print("\nSelect the type of password to generate:")
        print("1. Characters")
        print("2. Words")
        print("3. Exit")
        
        choice = input("Enter option (1, 2 or 3): ")
        
        if choice not in ['1', '2', '3']:
            print("Invalid option. Please choose a valid option.")
            continue
        
        if choice == '3':
            print("Exiting the tool...")
            break
        
        if choice == '1':
            while True:
                try:
                    length = int(input("Enter password length (8-60): "))
                    if length < 8 or length > 60:
                        raise ValueError
                    break
                except ValueError:
                    print("Please enter a valid number between 8 and 60.")
                    
            while True:
                use_uppercase_input = input("Include uppercase letters? (Y/N): ").lower()
                if use_uppercase_input in ['y', 'n']:
                    use_uppercase = use_uppercase_input == 'y'
                    break
                print("Please enter 'Y' for yes or 'N' for no.")
                
            while True:
                use_digits_input = input("Include digits? (Y/N): ").lower()
                if use_digits_input in ['y', 'n']:
                    use_digits = use_digits_input == 'y'
                    break
                print("Please enter 'Y' for yes or 'N' for no.")
                
            while True:
                use_symbols_input = input("Include symbols (@!&*)? (Y/N): ").lower()
                if use_symbols_input in ['y', 'n']:
                    use_symbols = use_symbols_input == 'y'
                    break
                print("Please enter 'Y' for yes or 'N' for no.")
                
            password = generate_char_password(length, use_uppercase, use_digits, use_symbols)
        
        elif choice == '2':
            while True:
                try:
                    num_words = int(input("Enter number of words (3-10): "))
                    if num_words < 3 or num_words > 10:
                        raise ValueError
                    break
                except ValueError:
                    print("Please enter a valid number between 3 and 10.")

            while True:
                separator_choice = input("Select the separator: 1. Underscore (_), 2. Hyphen (-), 3. Comma (,), 4. Period (.): ")
                if separator_choice in ['1', '2', '3', '4']:
                    separators = {'1': '_', '2': '-', '3': ',', '4': '.'}
                    separator = separators[separator_choice]
                    break
                print("Invalid option. Please choose a valid option.")
            
            use_uppercase = False
            while True:
                use_uppercase_input = input("Include uppercase in words? (Y/N): ").lower()
                if use_uppercase_input in ['y', 'n']:
                    use_uppercase = use_uppercase_input == 'y'
                    break
                print("Please enter 'Y' for yes or 'N' for no.")
                
            use_digits = False
            while True:
                use_digits_input = input("Include digits? (Y/N): ").lower()
                if use_digits_input in ['y', 'n']:
                    use_digits = use_digits_input == 'y'
                    break
                print("Please enter 'Y' for yes or 'N' for no.")
                
            password = generate_word_password(num_words, separator, use_uppercase, use_digits)
        
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
