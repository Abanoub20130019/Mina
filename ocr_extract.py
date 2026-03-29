import fitz
import os
from PIL import Image
import pytesseract
import io

# Find the second PDF
pdfs = [f for f in os.listdir('.') if f.endswith('.pdf')]
pdf2 = None
for p in pdfs:
    if 'mina' not in p.lower():
        pdf2 = p
        break

if pdf2:
    doc = fitz.open(pdf2)
    full_text = ''
    
    # Process first few pages as a test
    for i in range(min(5, len(doc))):
        page = doc[i]
        
        # Get page as image
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x zoom for better OCR
        img_data = pix.tobytes("png")
        img = Image.open(io.BytesIO(img_data))
        
        # OCR with Arabic language
        text = pytesseract.image_to_string(img, lang='ara+eng')
        full_text += f'\n\n=== Page {i+1} ===\n{text}'
    
    with open('unit2_ocr.txt', 'w', encoding='utf-8') as f:
        f.write(full_text)
    
    with open('ocr_status.txt', 'w', encoding='utf-8') as f:
        f.write(f'OCR completed for first 5 pages\n')
        f.write(f'Text length: {len(full_text)} chars\n')
        f.write('\nContent:\n')
        f.write(full_text[:3000])
