import fitz
import os

# Find the second PDF
pdfs = [f for f in os.listdir('.') if f.endswith('.pdf')]
pdf2 = None
for p in pdfs:
    if 'mina' not in p.lower():
        pdf2 = p
        break

if pdf2:
    doc = fitz.open(pdf2)
    
    # Check first few pages for text vs images
    with open('pdf_analysis.txt', 'w', encoding='utf-8') as f:
        f.write(f'PDF Analysis\n')
        f.write(f'Pages: {len(doc)}\n\n')
        
        for i in range(min(5, len(doc))):
            page = doc[i]
            text = page.get_text().strip()
            images = page.get_images()
            
            f.write(f'Page {i+1}:\n')
            f.write(f'  Text length: {len(text)}\n')
            f.write(f'  Images: {len(images)}\n')
            if text:
                f.write(f'  Sample: {text[:200]}\n')
            f.write('\n')
