import pytest
from app.main import process_file, extract_images_from_docx
from docx import Document
from PIL import Image
import io

@pytest.fixture
def docx_file_with_image(tmp_path):
    file = tmp_path / "test_file_with_image.docx"
    doc = Document()
    doc.add_paragraph("This is a sample docx file with text and one image.")

    image = Image.new('RGB', (100, 100), color = 'red')
    image_stream = io.BytesIO()
    image.save(image_stream, format="jpeg")
    image_stream.seek(0)
    doc.part.related_parts["image1.jpeg"] = io.BytesIO(image_stream.read())
    
    doc.save(file)
    return file

def test_process_and_extract_images(docx_file_with_image, tmp_path):
    text_content = process_file(str(docx_file_with_image))
    assert "This is a sample docx file with text and one image." in text_content

    output_folder = tmp_path / "images"
    output_folder.mkdir()
    image_count = extract_images_from_docx(str(docx_file_with_image))
    assert image_count == 1
    assert (output_folder / "image_1.jpeg").exists()
