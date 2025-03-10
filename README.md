# Binary-Gray-Code-Converter

A simple Python script to **convert Binary to Gray Code** and vice versa. Gray Code is widely used in digital systems to minimize errors in **sensors, encoders,** and **error correction**.

## 🚀 Features
- Convert Binary to Gray Code.
- Convert Gray Code back to Binary.
- Clean and efficient implementation.

## 🔧 Usage
```python
from binary_to_gray import binary_to_gray, gray_to_binary

binary = "1011"
gray = binary_to_gray(binary)
binary_back = gray_to_binary(gray)

print(f"Binary: {binary}, Gray Code: {gray}, Back to Binary: {binary_back}")
