def string_to_binary(text: str) -> None:
    list = []

    for i in text:
        decimal = ord(i)
        binary = bin(decimal)[2:]
        list.append(binary)

    bin_text = "".join(list)
    return bin_text


if __name__ == "__main__":
    string_to_binary()
