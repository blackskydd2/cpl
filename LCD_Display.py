def print_lc_display(s, n):
    digits = [
        [" - ", "| |", "   ", "| |", " - "],
        ["   ", "  |", "   ", "  |", "   "],
        [" - ", "  |", " - ", "|  ", " - "],
        [" - ", "  |", " - ", "  |", " - "],
        ["   ", "| |", " - ", "  |", "   "],
        [" - ", "|  ", " - ", "  |", " - "],
        [" - ", "|  ", " - ", "| |", " - "],
        [" - ", "  |", "   ", "  |", "   "],
        [" - ", "| |", " - ", "| |", " - "],
        [" - ", "| |", " - ", "  |", " - "]
    ]
    
    num_str = str(n)
    for row in range(2 * s + 3):
        line = ""
        for digit in num_str:
            digit_int = int(digit)
            if row % (s + 1) == 0:
                line += digits[digit_int][0] + " "
            elif 0 < row < (s + 1):
                line += digits[digit_int][1][0] + (s * " ") + digits[digit_int][1][1] + " "
            elif row == (s + 1):
                line += digits[digit_int][2] + " "
            elif (s + 2) < row < (2 * s + 2):
                line += digits[digit_int][3][0] + (s * " ") + digits[digit_int][3][1] + " "
            elif row == (2 * s + 2):
                line += digits[digit_int][4] + " "
        print(line)
    print()

def main():
    while True:
        s, n = map(int, input().split())
        if s == 0 and n == 0:
            break
        print_lc_display(s, n)

if __name__ == "__main__":
    main()
