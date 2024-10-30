import pytest
from app.main import process_file, count_words
from docx import Document

@pytest.fixture
def txt_file(tmp_path):
    file = tmp_path / "test_file.txt"
    file.write_text("This is a sample text file with seven words.")
    return file

@pytest.fixture
def docx_file(tmp_path):
    file = tmp_path / "test_file.docx"
    doc = Document()
    doc.add_paragraph("This is a sample docx file with eight words total.")
    doc.save(file)
    return file

def test_process_and_count_words_txt(txt_file):
    content = process_file(str(txt_file))
    word_count = count_words(content)
    assert word_count == 9

def test_process_and_count_words_docx(docx_file):
    content = process_file(str(docx_file))
    word_count = count_words(content)
    assert word_count == 10
