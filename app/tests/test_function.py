import pytest
from app.main import process_file  
from docx import Document

@pytest.fixture
def txt_file(tmp_path):
    file = tmp_path / "test_file.txt"
    file.write_text("This is a sample text file.")
    return file

@pytest.fixture
def docx_file(tmp_path):
    file = tmp_path / "test_file.docx"
    doc = Document()
    doc.add_paragraph("This is a sample docx file.")
    doc.save(file)
    return file

def test_process_txt_file(txt_file):
    content = process_file(str(txt_file))
    assert content == "This is a sample text file."

def test_process_docx_file(docx_file):
    content = process_file(str(docx_file))
    assert content == "This is a sample docx file."

def test_process_unsupported_file_format(tmp_path):
    file = tmp_path / "test_file.pdf"
    file.write_text("PDF content")
    with pytest.raises(ValueError, match="Не поддерживаемый формат"):
        process_file(str(file))
