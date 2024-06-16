def read_file_lines(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print(f"Tệp {file_path} không tồn tại.")
        return None
    except IOError:
        print(f"Không thể đọc tệp {file_path}. Kiểm tra quyền truy cập.")
        return None

file_path = "D:/ayaiau/gitcode/AIO-Exercise/tuan 2/P1_data.txt"
lines = read_file_lines(file_path)

if lines is not None:
    print("Các dòng trong tệp:")
    for line in lines:
        print(line.strip()) 

lines = 'I love AI'
words = lines.split()
print(words)
def preprocess_text(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace('.', '').replace(',', '')
    words = sentence.split()
    return words

def count_word(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    counter = {}
    for line in lines:
        words = preprocess_text(line)
        for word in words:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
    return counter

file_path = 'D:/ayaiau/gitcode/AIO-Exercise/P1_data.txt'  
result = count_word(file_path)

assert result['who'] == 3
print(result['man'])
print(result)