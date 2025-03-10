def binary_to_gray(binary: str) -> str:
    """Convert binary string to Gray code."""
    binary = int(binary, 2)
    gray = binary ^ (binary >> 1)
    return format(gray, 'b').zfill(len(bin(binary)[2:]))

def gray_to_binary(gray: str) -> str:
    """Convert Gray code string to binary."""
    gray = int(gray, 2)
    binary, shift = gray, gray >> 1
    while shift:
        binary ^= shift
        shift >>= 1
    return format(binary, 'b').zfill(len(bin(gray)[2:]))

# Example Usage
if __name__ == "__main__":
    binary_num = "1011"
    gray_code = binary_to_gray(binary_num)
    binary_converted_back = gray_to_binary(gray_code)

    print(f"Binary: {binary_num}")
    print(f"Gray Code: {gray_code}")
    print(f"Converted Back to Binary: {binary_converted_back}")
