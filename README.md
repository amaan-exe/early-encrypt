# early-encrypt
🔐 encrypt.py Encrypts a text file using XOR encryption. It preserves special characters (like \n, \t) and saves the encrypted output as encr.amn.  🔓 decrypt.py Decrypts the encr.amn file using the same XOR key. Restores the original text and saves it as decp.txt.


# 🔐 XOR File Encryptor & Decryptor

This project provides two simple Python scripts to encrypt and decrypt text files using XOR encryption, while preserving special characters like newlines and tabs.

---

## 📁 Files Included

- **encrypt.py** — Encrypts a text file and outputs `encr.amn`.
- **decrypt.py** — Decrypts `encr.amn` back to plain text as `decp.txt`.

---

## ⚙️ How to Use

### 1. Encryption
```bash
python encrypt.py
Enter the path of the text file to encrypt.

Provide an integer key for XOR encryption.

Output saved as encr.amn.

2. Decryption
python decrypt.py
Enter the path of the .amn file.

Provide the same integer key used for encryption.

Output saved as decp.txt.

📝 Notes
Encoding used: latin1 to avoid decode issues.

Escape characters (\n, \t, etc.) are kept unchanged.

Keep the key safe — it's required for decryption!
