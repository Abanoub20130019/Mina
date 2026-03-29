import os
import fitz
import sys

# Find all PDF files
pdfs = [f for f in os.listdir('.') if f.endswith('.pdf')]

# Use the second PDF (not mina.pdf)
pdf2 = None
for p in pdfs:
    if 'mina' not in p.lower():
        pdf2 = p
        break

if pdf2:
    doc = fitz.open(pdf2)
    
    full_text = ''
    for i in range(len(doc)):
        page = doc[i]
        text = page.get_text()
        if text.strip():
            full_text += f'\n\n=== Page {i+1} ===\n{text}'
    
    with open('unit2_content.txt', 'w', encoding='utf-8') as f:
        f.write(full_text)
    
    # Write status to file instead of printing
    with open('extract_status.txt', 'w', encoding='utf-8') as f:
        f.write(f'PDF: {len(doc)} pages\n')
        f.write(f'Text length: {len(full_text)} chars\n')
        f.write('\nFirst 2000 chars:\n')
        f.write(full_text[:2000])
