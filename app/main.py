from docx import Document

def process_file(file_path):
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        content = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    else:
        raise ValueError("Не поддерживаемый формат")
    return content

def count_words(text):
    return len(text.split())
