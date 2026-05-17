import sys
from collections import Counter

def main():
    # בדיקה ששם קובץ הקלט הועבר בשורת הפקודה
    if len(sys.argv) < 2:
        print("Usage: python character_frequencies.py <input_file_path>")
        return
    
    input_path = sys.argv[1]
    output_path = "frequencies.txt"
    
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
        return

    # ספירה
    char_counts = Counter(text)
    
    # כתיבת התוצאות לקובץ
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("char,count\n")
        
        for char, count in char_counts.items():
            # טיפול בתווים שאינם printable 
            char_to_print = char if char.isprintable() else repr(char)[1:-1]
            
            f.write(f"{char_to_print},{count}\n")
            
    print(f"Success! Frequencies saved to {output_path}")

if __name__ == "__main__":
    main()