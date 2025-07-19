import os
import fitz  # pymupdf

def read_all_pdfs_from_folder(folder_path):
    all_texts = []
    filenames = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            path = os.path.join(folder_path, filename)
            text = read_pdf_text(path)
            all_texts.append(text)
            filenames.append(filename)
    return all_texts, filenames

def read_pdf_text(pdf_path):
    doc = fitz.open(pdf_path)
    texts = []
    for page in doc:
        texts.append(page.get_text())
    return "\n".join(texts)

def split_text(text, max_len=1000):
    paragraphs = text.split('\n')
    chunks = []
    chunk = ""
    for para in paragraphs:
        if len(chunk) + len(para) < max_len:
            chunk += para + "\n"
        else:
            chunks.append(chunk)
            chunk = para + "\n"
    if chunk:
        chunks.append(chunk)
    return chunks
