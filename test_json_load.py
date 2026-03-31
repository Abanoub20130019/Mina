import sys
sys.path.append('app_data')
import json

def load_json_flashcards():
    """Load flashcards from JSON files"""
    json_flashcards = {
        "unit1": {},
        "unit2": {},
        "unit3": {},
        "unit4": {}
    }
    
    # Load flashcards_arabic.json
    try:
        with open('app_data/flashcards_arabic.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for ch in data.get('chapters', []):
            ch_id = ch.get('chapter_id')
            unit_key = f"unit{ch_id}"
            if unit_key not in json_flashcards:
                json_flashcards[unit_key] = {}
            
            for lesson in ch.get('lessons', []):
                l_id = lesson.get('lesson_id')
                cards = lesson.get('flashcards', [])
                if l_id not in json_flashcards[unit_key]:
                    json_flashcards[unit_key][l_id] = []
                for card in cards:
                    if isinstance(card, dict):
                        json_flashcards[unit_key][l_id].append({
                            'q': card.get('question', card.get('q', '')),
                            'a': card.get('answer', card.get('a', ''))
                        })
    except Exception as e:
        print(f"Error loading flashcards_arabic.json: {e}")
    
    # Load flashcards_complete.json
    try:
        with open('app_data/flashcards_complete.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for ch in data.get('chapters', []):
            ch_id = ch.get('chapter_id', 1)
            unit_key = f"unit{ch_id}"
            if unit_key not in json_flashcards:
                json_flashcards[unit_key] = {}
            
            for lesson in ch.get('lessons', []):
                l_id = lesson.get('lesson_id')
                cards = lesson.get('flashcards', [])
                if l_id not in json_flashcards[unit_key]:
                    json_flashcards[unit_key][l_id] = []
                for card in cards:
                    if isinstance(card, dict):
                        json_flashcards[unit_key][l_id].append({
                            'q': card.get('question', card.get('q', '')),
                            'a': card.get('answer', card.get('a', ''))
                        })
    except Exception as e:
        print(f"Error loading flashcards_complete.json: {e}")
    
    return json_flashcards

json_flashcards = load_json_flashcards()

print('JSON flashcards loaded:')
total = 0
for unit_key in json_flashcards:
    unit_data = json_flashcards[unit_key]
    if unit_data:
        print(f'  {unit_key}:')
        for lesson_key in unit_data:
            count = len(unit_data[lesson_key])
            total += count
            print(f'    Lesson {lesson_key}: {count} cards')

print(f'Total JSON cards: {total}')
