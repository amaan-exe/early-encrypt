import os

escape_chars = ['\t', '\n', '\r', '\b', '\f', '\v']

# Step 1: Ask user for file to encrypt
file_path = input("Enter the path of the file to encrypt: ").strip()

# Check if file exists
if not os.path.isfile(file_path):
    print("File not found. Please check the path and try again.")
    exit()

# Step 2: Read the file content using 'latin1' encoding to avoid decode errors
with open(file_path, 'r', encoding='latin1') as file:
    text = file.read()

# Step 3: Ask for XOR key
while True:
    try:
        key = int(input("Enter an integer key for XOR encryption: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Step 4: Convert chars except escape chars to ASCII codes with space delimiter
result = []
for ch in text:
    if ch in escape_chars:
        result.append(ch)
    else:
        result.append(str(ord(ch)))
        result.append(' ')

converted_text = ''.join(result).strip()

# Step 5: XOR each ASCII code with key, keep escape chars, add space delimiter
result_xor = []
i = 0
while i < len(converted_text):
    ch = converted_text[i]
    if ch in escape_chars:
        result_xor.append(ch)
        i += 1
    else:
        digits = []
        while i < len(converted_text) and converted_text[i] not in escape_chars and converted_text[i] != ' ':
            digits.append(converted_text[i])
            i += 1

        if digits:
            ascii_code = int(''.join(digits))
            xor_val = ascii_code ^ key
            result_xor.append(str(xor_val))
            result_xor.append(' ')

        if i < len(converted_text) and converted_text[i] == ' ':
            i += 1

final_text = ''.join(result_xor).strip()

# Step 6: Write encrypted output to 'encr.amn' in current directory
output_file = "encr.amn"
with open(output_file, 'w', encoding='latin1') as f:
    f.write(final_text)

print(f"Encryption complete! Encrypted data saved to {output_file}")
