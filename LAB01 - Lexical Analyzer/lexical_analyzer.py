import string


def get_reserved_words():
    file = open("reserved_words.txt")
    reserved_words = set()
    for line in file:
        reserved_words.add(line.strip())
    file.close()
    return reserved_words


def display_set(s):
    res = ""
    for word in s:
        res += word + ", "
    return res[:-2]


class LexicalAnalyzer:
    def __init__(self, word_stream):
        self.reserved_words = get_reserved_words()
        print(f"\nReserved Words: {self.reserved_words}\n")
        self.keywords = set()
        self.identifiers = set()
        self.math_operators = set()
        self.logical_operators = set()
        self.numerical_values = set()
        self.others = set()

    def scan(self):
        for i in range(len(word_stream)):
            if word_stream[i] in self.reserved_words:
                self.keywords.add(word_stream[i])
                word_stream[i] = None
                continue
            if word_stream[i] in ["+", "-", "*", "/", "="]:
                self.math_operators.add(word_stream[i])
                word_stream[i] = None
                continue
            if word_stream[i] in [">", "<", "<=", ">=", "=="]:
                self.logical_operators.add(word_stream[i])
                word_stream[i] = None
                continue
            if "." in word_stream[i]:
                try:
                    float_object = float(word_stream[i])
                    self.numerical_values.add(word_stream[i])
                except:
                    self.others.add(word_stream[i])
                word_stream[i] = None
                continue
            if word_stream[i][0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                try:
                    int_object = int(word_stream[i])
                    self.numerical_values.add(word_stream[i])
                except:
                    print(f"WHAT!: {word_stream[i]}")
                    self.others.add(word_stream[i])
                word_stream[i] = None
                continue
        for i in range(len(word_stream)):
            if word_stream[i] != None:
                if word_stream[i][0] in list(string.ascii_lowercase):
                    self.identifiers.add(word_stream[i])
                else:
                    self.others.add(word_stream[i])
                word_stream[i] = None

    def show_result(self):
        print(f"Keywords: {display_set(self.keywords)}")
        print(f"Identifiers: {display_set(self.identifiers)}")
        print(f"Math Operators: {display_set(self.math_operators)}")
        print(f"Logical Operators: {display_set(self.logical_operators)}")
        print(f"Numerical Values: {display_set(self.numerical_values)}")
        print(f"Others: {display_set(self.others)}")


def read(filename):
    file = open("input.txt", "r")
    word_stream = []
    for line in file:
        word_stream.extend(line.strip().split(" "))
    file.close()
    return word_stream


word_stream = read("input.txt")
print(f"Word Stream: {word_stream}\n")
analyzer = LexicalAnalyzer(word_stream)
analyzer.scan()
analyzer.show_result()
