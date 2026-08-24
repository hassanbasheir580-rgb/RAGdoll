from app.ingestion.pdf_loader import load_pdf


text = load_pdf("tests/documents/sample.pdf")

print(text)