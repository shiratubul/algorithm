import sys

def read_frequencies(filepath):
    """קריאת קובץ התדירויות בפורמט char,count"""
    frequencies = {}
    with open(filepath, "r", encoding="utf-8") as f:
        header = f.readline()  # דילוג על הכותרת
        for line in f:
            line = line.rstrip("\n")
            last_comma = line.rfind(",")
            if last_comma == -1:
                continue
            char_repr = line[:last_comma]
            actual_char = char_repr.encode("raw_unicode_escape").decode("unicode_escape")
            count = int(line[last_comma + 1:])
            frequencies[actual_char] = count
    return frequencies

def read_codes(filepath):
    """קריאת קובץ הקודים בפורמט char:code"""
    codes = {}
    with open(filepath, "r", encoding="utf-8") as f:
        header = f.readline()  # דילוג על הכותרת char:code
        for line in f:
            line = line.rstrip("\n")
            last_colon = line.rfind(":")
            if last_colon == -1:
                continue
            char_repr = line[:last_colon]
            actual_char = char_repr.encode("raw_unicode_escape").decode("unicode_escape")
            code_str = line[last_colon + 1:]
            codes[actual_char] = code_str
    return codes

def main():
    # בדיקה שהועברו שני קבצים בשורת הפקודה
    if len(sys.argv) < 3:
        print("Usage: python calculate_encoding_cost.py <frequencies_file> <codes_file>")
        return

    freq_file_path = sys.argv[1]
    codes_file_path = sys.argv[2]

    try:
        # טעינת הנתונים מהקבצים
        frequencies = read_frequencies(freq_file_path)
        codes = read_codes(codes_file_path)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    total_bits = 0
    
    # חישוב העלות הכוללת בביטים
    for char, count in frequencies.items():
        if char in codes:
            code_length = len(codes[char])  # אורך הקוד בביטים (למשל "0101" זה 4 ביטים)
            total_bits += count * code_length
        else:
            print(f"Warning: Character '{repr(char)}' found in frequencies but missing in codes file.")

    print(f"Total encoding length: {total_bits} bits")

if __name__ == "__main__":
    main()