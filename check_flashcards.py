import sys
sys.path.append('app_data')
import json

# Test loading all flashcards
def load_all_flashcards():
    all_cards = {
        1: {1: [], 2: [], 3: []},
        2: {1: [], 2: []},
        3: {1: [], 2: []},
        4: {1: [], 2: []}
    }
    
    # Load from flashcards.py
    try:
        from flashcards import flashcards_db
        for unit_num in range(1, 5):
            unit_key = f"unit{unit_num}"
            if unit_key in flashcards_db:
                unit_data = flashcards_db[unit_key]
                if isinstance(unit_data, dict) and "lessons" in unit_data:
                    for lesson_num, lesson_data in unit_data["lessons"].items():
                        if isinstance(lesson_data, dict) and "cards" in lesson_data:
                            all_cards[unit_num][lesson_num] = lesson_data["cards"]
        print("Loaded from flashcards.py")
    except Exception as e:
        print(f"Error loading flashcards.py: {e}")
    
    # Load from JSON files
    try:
        with open('app_data/flashcards_arabic.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for ch in data.get('chapters', []):
            ch_id = ch.get('chapter_id')
            for lesson in ch.get('lessons', []):
                l_id = lesson.get('lesson_id')
                cards = lesson.get('flashcards', [])
                if ch_id in all_cards and l_id in all_cards[ch_id]:
                    for card in cards:
                        if isinstance(card, dict):
                            all_cards[ch_id][l_id].append({
                                'q': card.get('question', ''),
                                'a': card.get('correct_answer', card.get('explanation', ''))
                            })
        print("Loaded from flashcards_arabic.json")
    except Exception as e:
        print(f"Error loading flashcards_arabic.json: {e}")
    
    try:
        with open('app_data/flashcards_complete.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for ch in data.get('chapters', []):
            ch_id = ch.get('chapter_id', 4)
            for lesson in ch.get('lessons', []):
                l_id = lesson.get('lesson_id')
                cards = lesson.get('flashcards', [])
                if ch_id in all_cards and l_id in all_cards[ch_id]:
                    for card in cards:
                        if isinstance(card, dict):
                            all_cards[ch_id][l_id].append({
                                'q': card.get('term', ''),
                                'a': card.get('definition', '')
                            })
        print("Loaded from flashcards_complete.json")
    except Exception as e:
        print(f"Error loading flashcards_complete.json: {e}")
    
    return all_cards

cards = load_all_flashcards()

print("\n=== All Flashcards ===")
for unit_num in range(1, 5):
    print(f"Unit {unit_num}:")
    for lesson_num in sorted(cards[unit_num].keys()):
        count = len(cards[unit_num][lesson_num])
        print(f"  Lesson {lesson_num}: {count} cards")
