import json

# Check flashcards_arabic.json
print("=== flashcards_arabic.json ===")
with open('app_data/flashcards_arabic.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chapters = data.get('chapters', [])
total = 0
for i, ch in enumerate(chapters):
    print(f"Chapter {i+1} (ID: {ch.get('chapter_id')}):")
    lessons = ch.get('lessons', [])
    for lesson in lessons:
        lid = lesson.get('lesson_id')
        fcount = len(lesson.get('flashcards', []))
        total += fcount
        print(f"  Lesson {lid}: {fcount} flashcards")

print(f"Total: {total} flashcards")

# Check flashcards_complete.json
print("\n=== flashcards_complete.json ===")
with open('app_data/flashcards_complete.json', 'r', encoding='utf-8') as f:
    data2 = json.load(f)

chapters2 = data2.get('chapters', [])
total2 = 0
for i, ch in enumerate(chapters2):
    print(f"Chapter {i+1}:")
    lessons = ch.get('lessons', [])
    if lessons:
        for lesson in lessons:
            lid = lesson.get('lesson_id')
            fcount = len(lesson.get('flashcards', []))
            total2 += fcount
            print(f"  Lesson {lid}: {fcount} flashcards")
    else:
        print("  No lessons found")

print(f"Total: {total2} flashcards")
