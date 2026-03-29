import fitz

doc = fitz.open('mina.pdf')
print(f'Total Pages: {len(doc)}')

full_text = ""
for i in range(len(doc)):
    page = doc[i]
    text = page.get_text()
    full_text += f"\n\n--- Page {i+1} ---\n{text}"

# Save full text
with open('mina_content.txt', 'w', encoding='utf-8') as f:
    f.write(full_text)

print("\n" + "="*50)
print("FIRST 10000 CHARACTERS:")
print("="*50)
print(full_text[:10000])
