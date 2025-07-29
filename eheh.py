import os

escape_chars = ['\t', '\n', '\r', '\b', '\f', '\v']

# Step 1: Ask for path of encrypted file
file_path = input("Enter the path of the encrypted .amn file: ").strip()

# Check if file exists
if not os.path.isfile(file_path):
    print("File not found. Please check the path and try again.")
    exit()

# Step 2: Read encrypted data using 'latin1' to avoid decode errors
with open(file_path, 'r', encoding='latin1') as file:
    encrypted_text = file.read()

# Step 3: Ask for the same XOR key used in encryption
while True:
    try:
        key = int(input("Enter the same integer key used for XOR encryption: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Step 4: Reconstruct the original text
result = []
i = 0
while i < len(encrypted_text):
    ch = encrypted_text[i]

    if ch in escape_chars:
        result.append(ch)
        i += 1
    else:
        digits = []
        while i < len(encrypted_text) and encrypted_text[i] not in escape_chars and encrypted_text[i] != ' ':
            digits.append(encrypted_text[i])
            i += 1

        if digits:
            xor_val = int(''.join(digits))
            original_ascii = xor_val ^ key
            result.append(chr(original_ascii))

        if i < len(encrypted_text) and encrypted_text[i] == ' ':
            i += 1

# Step 5: Save decrypted output to 'decp.txt'
output_file = "decp.txt"
with open(output_file, 'w', encoding='latin1') as f:
    f.write(''.join(result))

print(f"Decryption complete! Decrypted text saved to {output_file}")
