def caesar_cipher(text, shift, direction):
    result = ""   
    # Adjust the shift for decryption
    if direction == "decrypt":
        shift = -shift
    # Traverse the text
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Perform the shift
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # Append non-alphabetical characters as is
            result += char            
    return result
def main():
    while True:
        direction = input("Do you want to encrypt, decrypt the message or exit? (enter 'encrypt', 'decrypt' or 'exit'): ").strip().lower()
        
        if direction == 'exit':
            print("Goodbye!")
            break
        if direction not in ['encrypt', 'decrypt']:
            print("Invalid input. Please enter 'encrypt', 'decrypt', or 'exit'.")
            continue
        message = input("Enter your message: ")
        while True:
            try:
                shift = int(input("Enter the shift value: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer for the shift value.") 
        result = caesar_cipher(message, shift, direction)
        print(f"The result is: {result}")
if __name__ == "__main__":
    main()
