def string_to_binary(text: str) -> None:
    bin_text = ''.join([bin(ord(i))[2:] for i in text])
    return bin_text

def binary_to_string(text1: str) -> None:
    str_text = "".join([chr(int(text1[i:i+7], 2)) for i in range(0, len(text1), 7)])
    return str_text

if __name__=='__main__':
    string_to_binary()
    binary_to_string()