import sys
import heapq

def read_frequencies(filepath):
    frequencies = {}
    with open(filepath, "r", encoding="utf-8") as f:
        header = f.readline()  # דילוג על כותרת char,count
        for line in f:
            line = line.rstrip("\n")
            last_comma = line.rfind(",")
            if last_comma == -1:
                continue
            char_repr = line[:last_comma]
            
            # המרה חזרה של escape sequences לתווים אמיתיים
            actual_char = (
                char_repr.encode("raw_unicode_escape")
                .decode("unicode_escape")
            )
            count = int(line[last_comma + 1:])
            frequencies[actual_char] = count
    return frequencies

# מחלקה המייצגת צומת בעץ הופמן
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # הגדרת אופרטור "קטן מ-" עבור הערימה (heapq משתמשת בו כדי להשוות תדירויות)
    def __lt__(self, other):
        return self.freq < other.freq

# פונקציה רקורסיבית למעבר על העץ והפקת הקודים לכל תו
def generate_codes(node, current_code, codes_dict):
    if node is None:
        return
    
    # אם הגענו לעלה (תו)
    if node.char is not None:
        codes_dict[node.char] = current_code
        return
    
    # מעבר שמאלה מוסיף '0', מעבר ימינה מוסיף '1'
    generate_codes(node.left, current_code + "0", codes_dict)
    generate_codes(node.right, current_code + "1", codes_dict)

def main():
    if len(sys.argv) < 2:
        print("Usage: python huffman_code.py <frequencies_file_path>")
        return

    freq_file_path = sys.argv[1]
    output_path = "huffman.txt"

    # 1. קריאת השכיחויות מהקובץ
    try:
        frequencies = read_frequencies(freq_file_path)
    except FileNotFoundError:
        print(f"Error: The file '{freq_file_path}' was not found.")
        return

    if not frequencies:
        print("The frequencies file is empty.")
        return

    # 2. בניית ערימת המינימום (Min-Heap)
    heap = []
    for char, freq in frequencies.items():
        node = HuffmanNode(char, freq)
        heapq.heappush(heap, node)

    # 3. בניית עץ הופמן על ידי איחוד צמתים בעלי תדירות נמוכה
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        # יצירת צומת אב חדש שסכום תדירויותיו הוא סכום שני הבנים
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

    # השורש שנשאר בערימה הוא שורש עץ הופמן המלא
    root = heap[0]

    # 4. הפקת הקודים מתוך העץ
    huffman_codes = {}
    # מקרה קצה: אם יש רק תו אחד ייחודי בטקסט
    if root.char is not None:
        huffman_codes[root.char] = "0"
    else:
        generate_codes(root, "", huffman_codes)

    # 5. כתיבת הקודים לקובץ huffman.txt בפורמט char:code
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("char:code\n")  # שורת כותרת בפורמט הנדרש
        for char, code in huffman_codes.items():
            # המרת תווים מיוחדים חזרה לפורמט הניתן להדפסה (למשל \n)
            char_to_print = char if char.isprintable() else repr(char)[1:-1]
            f.write(f"{char_to_print}:{code}\n")

    print(f"Success! Huffman codes saved to {output_path}")

if __name__ == "__main__":
    main()