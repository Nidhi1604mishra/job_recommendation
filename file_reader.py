import fitz        # PyMuPDF
import docx

def read_pdf(file):
    doc = fitz.open(file.name)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def read_docx(file):
    doc = docx.Document(file.name)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def extract_text_from_file(file):
    filename = file.name
    if file is None:
        return "Please upload a file"
    
    if filename.endswith(".pdf"):
        return read_pdf(file)
    elif filename.endswith(".docx"):
        return read_docx(file)
    else:
        return "Unsupported file type. PLease upload a PDF or DOCX file"
