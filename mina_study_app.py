import streamlit as st
import sys
sys.path.append('app_data')

# Import all units content
from unit1_content import slides as unit1_slides
from unit2_content import slides as unit2_slides
from unit3_content import slides as unit3_slides
from unit4_content import slides as unit4_slides

# Import question banks from multiple files
try:
    from questions import questions as questions_list
except:
    questions_list = []

try:
    from unit2_questions import questions as unit2_questions_list
except:
    unit2_questions_list = []

try:
    from more_questions import additional_questions as more_q_list
except:
    more_q_list = []

try:
    from all_questions import (
        # Unit 1
        unit1_lesson1_mcq, unit1_lesson1_tf, unit1_lesson1_flashcards,
        unit1_lesson2_mcq, unit1_lesson2_tf, unit1_lesson2_flashcards,
        unit1_lesson3_mcq, unit1_lesson3_tf, unit1_lesson3_flashcards,
        # Unit 2
        unit2_lesson1_mcq, unit2_lesson1_tf, unit2_lesson1_flashcards,
        unit2_lesson2_mcq, unit2_lesson2_tf, unit2_lesson2_flashcards,
        # Unit 3
        unit3_lesson1_mcq, unit3_lesson1_tf, unit3_lesson1_flashcards,
        unit3_lesson2_mcq, unit3_lesson2_tf, unit3_lesson2_flashcards,
        # Unit 4
        unit4_lesson1_mcq, unit4_lesson1_tf, unit4_lesson1_flashcards,
        unit4_lesson2_mcq, unit4_lesson2_tf, unit4_lesson2_flashcards,
    )
    has_all_questions = True
except Exception as e:
    has_all_questions = False
    # Unit 1
    unit1_lesson1_mcq = unit1_lesson1_tf = unit1_lesson1_flashcards = []
    unit1_lesson2_mcq = unit1_lesson2_tf = unit1_lesson2_flashcards = []
    unit1_lesson3_mcq = unit1_lesson3_tf = unit1_lesson3_flashcards = []
    # Unit 2
    unit2_lesson1_mcq = unit2_lesson1_tf = unit2_lesson1_flashcards = []
    unit2_lesson2_mcq = unit2_lesson2_tf = unit2_lesson2_flashcards = []
    # Unit 3
    unit3_lesson1_mcq = unit3_lesson1_tf = unit3_lesson1_flashcards = []
    unit3_lesson2_mcq = unit3_lesson2_tf = unit3_lesson2_flashcards = []
    # Unit 4
    unit4_lesson1_mcq = unit4_lesson1_tf = unit4_lesson1_flashcards = []
    unit4_lesson2_mcq = unit4_lesson2_tf = unit4_lesson2_flashcards = []

# Import flashcards
try:
    from flashcards import flashcards_db
except:
    flashcards_db = {}

# Import JSON flashcards
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
                # Convert format if needed
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
                # Convert format if needed
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

# Helper function to get flashcards from all sources
def get_flashcards_from_db(unit_num, lesson_num):
    cards = []
    
    # Get from flashcards_db (Python module)
    unit_key = f"unit{unit_num}"
    if unit_key in flashcards_db:
        unit_data = flashcards_db[unit_key]
        if isinstance(unit_data, dict) and "lessons" in unit_data:
            lesson_data = unit_data["lessons"].get(lesson_num, {})
            if isinstance(lesson_data, dict) and "cards" in lesson_data:
                cards.extend(lesson_data["cards"])
    
    # Get from JSON files
    if unit_key in json_flashcards:
        if lesson_num in json_flashcards[unit_key]:
            cards.extend(json_flashcards[unit_key][lesson_num])
        elif str(lesson_num) in json_flashcards[unit_key]:
            cards.extend(json_flashcards[unit_key][str(lesson_num)])
    
    return cards

# Build questions dictionary
all_questions_data = {
    "unit1": {
        "name": "الطاقة الحرارية وتغيرات المادة",
        "lessons": {
            1: {
                "name": "التغيرات الحرارية المصاحبة للتغيرات الفيزيائية",
                "mcq": unit1_lesson1_mcq if has_all_questions else [q for q in questions_list if q.get('lesson') == 1] + [q for q in more_q_list if q.get('lesson') == 1],
                "truefalse": unit1_lesson1_tf if has_all_questions else [],
                "flashcards": unit1_lesson1_flashcards if has_all_questions else get_flashcards_from_db(1, 1)
            },
            2: {
                "name": "التغيرات الحرارية المصاحبة للتغيرات الكيميائية",
                "mcq": unit1_lesson2_mcq if has_all_questions else [q for q in questions_list if q.get('lesson') == 2] + [q for q in more_q_list if q.get('lesson') == 2],
                "truefalse": unit1_lesson2_tf if has_all_questions else [],
                "flashcards": unit1_lesson2_flashcards if has_all_questions else get_flashcards_from_db(1, 2)
            },
            3: {
                "name": "الاحتراق والأكسدة والاختزال",
                "mcq": unit1_lesson3_mcq if has_all_questions else [q for q in questions_list if q.get('lesson') == 3],
                "truefalse": unit1_lesson3_tf if has_all_questions else [],
                "flashcards": unit1_lesson3_flashcards if has_all_questions else get_flashcards_from_db(1, 3)
            },
        }
    },
    "unit2": {
        "name": "القوى والحركة",
        "lessons": {
            1: {
                "name": "قوانين نيوتن للحركة",
                "mcq": unit2_lesson1_mcq if has_all_questions else [q for q in unit2_questions_list if q.get('lesson') == 4],
                "truefalse": unit2_lesson1_tf if has_all_questions else [],
                "flashcards": unit2_lesson1_flashcards if has_all_questions else get_flashcards_from_db(2, 1)
            },
            2: {
                "name": "الروافع",
                "mcq": unit2_lesson2_mcq if has_all_questions else [],
                "truefalse": unit2_lesson2_tf if has_all_questions else [],
                "flashcards": unit2_lesson2_flashcards if has_all_questions else get_flashcards_from_db(2, 2)
            },
        }
    },
    "unit3": {
        "name": "التكاثر فى الكائنات الحية",
        "lessons": {
            1: {
                "name": "الانقسام الخلوى",
                "mcq": unit3_lesson1_mcq if has_all_questions else [],
                "truefalse": unit3_lesson1_tf if has_all_questions else [],
                "flashcards": unit3_lesson1_flashcards if has_all_questions else get_flashcards_from_db(3, 1)
            },
            2: {
                "name": "التكاثر الزهرى",
                "mcq": unit3_lesson2_mcq if has_all_questions else [],
                "truefalse": unit3_lesson2_tf if has_all_questions else [],
                "flashcards": unit3_lesson2_flashcards if has_all_questions else get_flashcards_from_db(3, 2)
            },
        }
    },
    "unit4": {
        "name": "التغيرات الفيزيائية فى الغلاف الجوى",
        "lessons": {
            1: {
                "name": "أثر الحرارة والضغط فى تشكل المناخ",
                "mcq": unit4_lesson1_mcq if has_all_questions else [],
                "truefalse": unit4_lesson1_tf if has_all_questions else [],
                "flashcards": unit4_lesson1_flashcards if has_all_questions else get_flashcards_from_db(4, 1)
            },
            2: {
                "name": "الرياح والتنبؤات الجوية",
                "mcq": unit4_lesson2_mcq if has_all_questions else [],
                "truefalse": unit4_lesson2_tf if has_all_questions else [],
                "flashcards": unit4_lesson2_flashcards if has_all_questions else get_flashcards_from_db(4, 2)
            },
        }
    },
}

# Page config
st.set_page_config(
    page_title="مينا - تطبيق المذاكرة الذكي",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS with RTL fixes
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@400;600;700&display=swap');
    
    * {
        font-family: 'Noto Naskh Arabic', 'Segoe UI', sans-serif;
    }
    
    /* RTL Support */
    html, body, .stApp {
        direction: rtl;
        text-align: right;
    }
    
    /* Main container RTL */
    .main .block-container {
        direction: rtl;
        text-align: right;
        padding: 2rem 1rem;
    }
    
    /* All text elements RTL */
    h1, h2, h3, h4, h5, h6, p, div, span, li, label {
        text-align: right;
    }
    
    /* Headers */
    h1 {
        color: #1e3a5f;
        text-align: center;
        border-bottom: 3px solid #667eea;
        padding-bottom: 15px;
        margin-bottom: 25px;
        font-size: 2.2rem;
    }
    
    h2 {
        color: #1e3a5f;
        font-size: 1.8rem;
        margin-top: 20px;
    }
    
    h3 {
        color: #2d4a6f;
        font-size: 1.4rem;
    }
    
    /* Content boxes */
    .content-box {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        border-right: 5px solid #667eea;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        direction: rtl;
        text-align: right;
    }
    
    .content-box ul {
        padding-right: 25px;
        padding-left: 0;
        list-style-position: outside;
    }
    
    .content-box li {
        margin: 10px 0;
        line-height: 1.8;
    }
    
    /* Question cards */
    .question-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        border-right: 5px solid #11998e;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Flash card styles */
    .flashcard {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 20px;
        padding: 40px;
        margin: 20px 0;
        border: 3px solid #667eea;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        min-height: 300px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .flashcard:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(0,0,0,0.2);
    }
    
    .flashcard-front {
        font-size: 1.5rem;
        font-weight: bold;
        color: #1e3a5f;
        text-align: center;
    }
    
    .flashcard-back {
        font-size: 1.3rem;
        color: #28a745;
        text-align: center;
        border-top: 2px dashed #667eea;
        padding-top: 20px;
        margin-top: 20px;
    }
    
    /* Formula box */
    .formula-box {
        background: #1e3a5f;
        color: #00d4ff;
        padding: 18px;
        border-radius: 12px;
        text-align: center;
        margin: 15px 0;
        font-family: 'Courier New', monospace;
        font-size: 1.1rem;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    
    /* Stats cards */
    .stat-card {
        background: linear-gradient(145deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
        transition: transform 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
    }
    
    .stat-card h2 {
        color: white;
        font-size: 2.5rem;
        margin: 10px 0;
    }
    
    .stat-card h3 {
        color: white;
        font-size: 1.8rem;
        margin: 5px 0;
    }
    
    .stat-card p {
        color: rgba(255,255,255,0.9);
        font-size: 1.1rem;
        text-align: center;
    }
    
    /* Answer feedback */
    .correct-answer {
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
        color: white;
        padding: 18px;
        border-radius: 12px;
        margin: 15px 0;
        font-weight: bold;
        font-size: 1.1rem;
        box-shadow: 0 4px 15px rgba(40, 167, 69, 0.3);
    }
    
    .wrong-answer {
        background: linear-gradient(135deg, #dc3545 0%, #e74c3c 100%);
        color: white;
        padding: 18px;
        border-radius: 12px;
        margin: 15px 0;
        font-weight: bold;
        font-size: 1.1rem;
        box-shadow: 0 4px 15px rgba(220, 53, 69, 0.3);
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        padding: 18px;
        border-radius: 12px;
        margin: 12px 0;
        border-right: 5px solid #2196f3;
    }
    
    .warning-box {
        background: linear-gradient(135deg, #fff3cd 0%, #ffe082 100%);
        padding: 18px;
        border-radius: 12px;
        margin: 12px 0;
        border-right: 5px solid #ffc107;
    }
    
    .success-box {
        background: linear-gradient(135deg, #d4edda 0%, #a5d6a7 100%);
        padding: 18px;
        border-radius: 12px;
        margin: 12px 0;
        border-right: 5px solid #28a745;
    }
    
    /* Highlight */
    .highlight {
        background: linear-gradient(120deg, #a8edea 0%, #fed6e3 100%);
        padding: 3px 10px;
        border-radius: 6px;
        font-weight: bold;
    }
    
    /* Lesson borders */
    .lesson-1 { border-right-color: #667eea !important; }
    .lesson-2 { border-right-color: #11998e !important; }
    .lesson-3 { border-right-color: #f093fb !important; }
    
    /* Progress */
    .progress-text {
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        color: #1e3a5f;
        margin: 15px 0;
    }
    
    /* Tables */
    table {
        width: 100%;
        border-collapse: collapse;
        direction: rtl;
        margin: 15px 0;
    }
    
    th {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        text-align: right;
        font-weight: 600;
    }
    
    td {
        padding: 12px 15px;
        border: 1px solid #dee2e6;
        text-align: right;
    }
    
    tr:nth-child(even) {
        background: #f8f9fa;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Unit badge */
    .unit-badge {
        display: inline-block;
        padding: 8px 20px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 1rem;
        margin-bottom: 15px;
    }
    
    .unit-1 { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
    .unit-2 { background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%); color: white; }
    .unit-3 { background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); color: white; }
    .unit-4 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; }
    
    /* Lesson tags */
    .lesson-tag {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 8px;
    }
    
    .lesson-tag-1 { background: #667eea; color: white; }
    .lesson-tag-2 { background: #11998e; color: white; }
    .lesson-tag-3 { background: #f093fb; color: white; }
</style>
""", unsafe_allow_html=True)

# Initialize session state
for key in ['current_slide', 'current_question', 'quiz_started', 'show_answer', 'correct_count', 'wrong_count', 'selected_unit', 'question_results', 'current_lesson', 'flashcard_index', 'flashcard_show_answer', 'quiz_mode']:
    if key not in st.session_state:
        if key == 'question_results':
            st.session_state[key] = {}
        elif key in ['correct_count', 'wrong_count', 'current_slide', 'current_question', 'selected_unit', 'current_lesson', 'flashcard_index']:
            st.session_state[key] = 0
        elif key == 'quiz_mode':
            st.session_state[key] = 'mcq'  # 'mcq' or 'truefalse'
        else:
            st.session_state[key] = False

# Store slide positions for each unit
for i in range(1, 5):
    if f'current_slide_u{i}' not in st.session_state:
        st.session_state[f'current_slide_u{i}'] = 0

# All units data
units_data = {
    1: {"name": "الوحدة الأولى: الطاقة الحرارية وتغيرات المادة", "slides": unit1_slides, "color": "#667eea", "lessons": 3},
    2: {"name": "الوحدة الثانية: القوى والحركة", "slides": unit2_slides, "color": "#ff6b6b", "lessons": 2},
    3: {"name": "الوحدة الثالثة: التكاثر فى الكائنات الحية", "slides": unit3_slides, "color": "#11998e", "lessons": 2},
    4: {"name": "الوحدة الرابعة: التغيرات الفيزيائية فى الغلاف الجوى", "slides": unit4_slides, "color": "#f093fb", "lessons": 2},
}

# Lesson names
lesson_names = {
    (1, 1): "الدرس الأول: التغيرات الحرارية المصاحبة للتغيرات الفيزيائية",
    (1, 2): "الدرس الثانى: التغيرات الحرارية المصاحبة للتغيرات الكيميائية",
    (1, 3): "الدرس الثالث: الاحتراق والأكسدة والاختزال",
    (2, 1): "الدرس الأول: قوانين نيوتن للحركة",
    (2, 2): "الدرس الثانى: الروافع",
    (3, 1): "الدرس الأول: الانقسام الخلوى",
    (3, 2): "الدرس الثانى: التكاثر الزهرى",
    (4, 1): "الدرس الأول: أثر الحرارة والضغط فى تشكل المناخ",
    (4, 2): "الدرس الثانى: الرياح والتنبؤات الجوية",
}

# Unit key mapping
unit_map = {1: "unit1", 2: "unit2", 3: "unit3", 4: "unit4"}

# Flatten all questions - handle the nested structure
all_questions = []
for unit_num in range(1, 5):
    unit_key = unit_map[unit_num]
    if unit_key in all_questions_data:
        unit_data = all_questions_data[unit_key]
        if isinstance(unit_data, dict) and "lessons" in unit_data:
            for lesson_num, lesson_data in unit_data["lessons"].items():
                if isinstance(lesson_data, dict):
                    # Add MCQ questions
                    if "mcq" in lesson_data:
                        for q in lesson_data["mcq"]:
                            if isinstance(q, dict):
                                q_copy = q.copy()
                                q_copy['unit'] = unit_num
                                q_copy['lesson'] = lesson_num
                                q_copy['type'] = 'mcq'
                                # Convert keys: 'question' -> 'q', 'answer' -> 'correct'
                                if 'question' in q_copy:
                                    q_copy['q'] = q_copy.pop('question')
                                if 'answer' in q_copy:
                                    ans = q_copy.pop('answer')
                                    if isinstance(ans, int):
                                        q_copy['correct'] = ans
                                    elif 'options' in q_copy and ans in q_copy['options']:
                                        q_copy['correct'] = q_copy['options'].index(ans)
                                    else:
                                        q_copy['correct'] = 0
                                all_questions.append(q_copy)
                    # Add True/False questions converted to MCQ
                    if "truefalse" in lesson_data:
                        for q in lesson_data["truefalse"]:
                            if isinstance(q, dict):
                                q_copy = q.copy()
                                q_copy['unit'] = unit_num
                                q_copy['lesson'] = lesson_num
                                q_copy['type'] = 'truefalse'
                                q_copy['options'] = ["صح", "خطأ"]
                                # Convert keys
                                if 'question' in q_copy:
                                    q_copy['q'] = q_copy.pop('question')
                                # Determine correct answer
                                if 'answer' in q_copy:
                                    ans = q_copy.pop('answer')
                                    if isinstance(ans, int):
                                        q_copy['correct'] = ans
                                    elif ans in [0, 'صح', True, 'True', 'true']:
                                        q_copy['correct'] = 0
                                    else:
                                        q_copy['correct'] = 1
                                elif 'correct' in q_copy:
                                    if q_copy['correct'] in [0, 'صح', True, 'True', 'true']:
                                        q_copy['correct'] = 0
                                    else:
                                        q_copy['correct'] = 1
                                else:
                                    q_copy['correct'] = 0
                                all_questions.append(q_copy)

# Get flashcards
def get_flashcards(unit_num=None, lesson_num=None):
    flashcards = []
    for u_num in range(1, 5):
        if unit_num and u_num != unit_num:
            continue
        unit_key = unit_map[u_num]
        if unit_key in all_questions_data:
            unit_data = all_questions_data[unit_key]
            if isinstance(unit_data, dict) and "lessons" in unit_data:
                for l_num, lesson_data in unit_data["lessons"].items():
                    if lesson_num and l_num != lesson_num:
                        continue
                    if isinstance(lesson_data, dict) and "flashcards" in lesson_data:
                        for card in lesson_data["flashcards"]:
                            if isinstance(card, dict):
                                card_copy = card.copy()
                                card_copy['unit'] = u_num
                                card_copy['lesson'] = l_num
                                flashcards.append(card_copy)
    return flashcards

# Sidebar
st.sidebar.markdown("<h1 style='text-align: right;'>📚 قائمة التنقل</h1>", unsafe_allow_html=True)
page = st.sidebar.radio("", 
    ["🏠 الرئيسية", "📘 الوحدة الأولى", "📗 الوحدة الثانية", "📙 الوحدة الثالثة", "📕 الوحدة الرابعة", "❓ اختبار MCQ", "📋 امتحان شامل", "🎴 بطاقات التعلم", "📊 إحصائيات"], 
    label_visibility="collapsed"
)

def render_unit_page(unit_num):
    """Render a unit page with lessons"""
    unit = units_data[unit_num]
    st.markdown(f"<div class='unit-badge unit-{unit_num}'>{unit['name']}</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    current_slide_key = f'current_slide_u{unit_num}'
    current_slide = st.session_state[current_slide_key]
    total_slides = len(unit['slides'])
    
    # Filter slides by lesson if selected
    lesson_filter = st.selectbox(
        "اختر الدرس:",
        ["جميع الدروس"] + [lesson_names[(unit_num, i)] for i in range(1, unit['lessons'] + 1)]
    )
    
    filtered_slides = unit['slides']
    if lesson_filter != "جميع الدروس":
        lesson_num = int(lesson_filter.split("الدرس ")[1].split(":")[0])
        filtered_slides = [s for s in unit['slides'] if s.get('lesson', 1) == lesson_num]
    
    if not filtered_slides:
        st.warning("لا توجد شرائح لهذا الدرس")
        return
    
    # Progress
    st.markdown(f"<p class='progress-text'>الشريحة {current_slide + 1} من {total_slides}</p>", unsafe_allow_html=True)
    st.progress((current_slide + 1) / total_slides)
    
    # Navigation buttons
    nav_cols = st.columns(10)
    for i in range(min(10, total_slides)):
        btn_type = "primary" if i == current_slide else "secondary"
        if nav_cols[i].button(f"{i+1}", key=f"u{unit_num}_{i}", type=btn_type):
            st.session_state[current_slide_key] = i
            st.rerun()
    
    # Second row if needed
    if total_slides > 10:
        nav_cols2 = st.columns(10)
        for i in range(10, min(20, total_slides)):
            btn_type = "primary" if i == current_slide else "secondary"
            if nav_cols2[i-10].button(f"{i+1}", key=f"u{unit_num}_{i}", type=btn_type):
                st.session_state[current_slide_key] = i
                st.rerun()
    
    st.markdown("---")
    
    # Content
    current = unit['slides'][current_slide]
    lesson_num = current.get('lesson', 1)
    lesson_class = f"lesson-{lesson_num}"
    
    st.markdown(f"""
    <div style='text-align: center; margin-bottom: 15px;'>
        <span class='lesson-tag lesson-tag-{lesson_num}'>الدرس {lesson_num}</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"<h2 style='text-align: center; color: {unit['color']};'>{current['title']}</h2>", unsafe_allow_html=True)
    st.markdown(f"<div class='content-box {lesson_class}'>{current['content']}</div>", unsafe_allow_html=True)
    
    # Nav buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if current_slide < total_slides - 1:
            if st.button("⬅️ التالي", use_container_width=True):
                st.session_state[current_slide_key] += 1
                st.rerun()
    with col3:
        if current_slide > 0:
            if st.button("السابق ➡️", use_container_width=True):
                st.session_state[current_slide_key] -= 1
                st.rerun()

# Main pages
if page == "🏠 الرئيسية":
    st.title("📚 مرحباً بك في تطبيق مينا للمذاكرة")
    st.markdown("<h3 style='text-align: center; color: #667eea;'>علوم - الصف الثانى الإعدادى - الترم الثانى</h3>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Stats cards
    total_mcq = len(all_questions)
    total_flashcards = len(get_flashcards())
    total_slides = sum(len(u["slides"]) for u in units_data.values())
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class='stat-card'>
            <div style='font-size: 2.5rem;'>📖</div>
            <h3>4 وحدات</h3>
            <p>محتوى تعليمى شامل</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class='stat-card'>
            <div style='font-size: 2.5rem;'>📑</div>
            <h3>{total_slides} شريحة</h3>
            <p>شرح تفصيلى للدروس</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class='stat-card'>
            <div style='font-size: 2.5rem;'>❓</div>
            <h3>{total_mcq} سؤال</h3>
            <p>اختبارات تفاعلية</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class='stat-card'>
            <div style='font-size: 2.5rem;'>🎴</div>
            <h3>{total_flashcards} بطاقة</h3>
            <p>بطاقات تعليمية</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Units overview
    st.markdown("<h3 style='text-align: right;'>📋 الوحدات الدراسية:</h3>", unsafe_allow_html=True)
    
    for unit_num, unit in units_data.items():
        lesson_count = unit["lessons"]
        slide_count = len(unit["slides"])
        mcq_count = len([q for q in all_questions if q.get('unit') == unit_num])
        
        st.markdown(f"""
        <div class='info-box' style='border-right-color: {unit["color"]};'>
            <b style='color: {unit["color"]}; font-size: 1.2rem;'>📚 {unit['name']}</b><br>
            <span style='margin-right: 25px;'>• {lesson_count} دروس</span><br>
            <span style='margin-right: 25px;'>• {slide_count} شريحة تعليمية</span><br>
            <span style='margin-right: 25px;'>• {mcq_count} سؤال</span>
        </div>
        """, unsafe_allow_html=True)

elif page == "📘 الوحدة الأولى":
    render_unit_page(1)

elif page == "📗 الوحدة الثانية":
    render_unit_page(2)

elif page == "📙 الوحدة الثالثة":
    render_unit_page(3)

elif page == "📕 الوحدة الرابعة":
    render_unit_page(4)

elif page == "❓ اختبار MCQ":
    st.title("❓ اختبار الأسئلة متعددة الخيارات")
    st.markdown("---")
    
    if not st.session_state.quiz_started:
        st.markdown("<h3 style='text-align: right;'>⚙️ إعدادات الاختبار</h3>", unsafe_allow_html=True)
        
        # Count questions per unit/lesson
        question_counts = {}
        for unit_num in range(1, 5):
            question_counts[unit_num] = {}
            for lesson_num in range(1, units_data[unit_num]["lessons"] + 1):
                count = len([q for q in all_questions if q.get('unit') == unit_num and q.get('lesson') == lesson_num])
                question_counts[unit_num][lesson_num] = count
        
        # Filter options
        filter_options = ["الكل (جميع الوحدات)"]
        for unit_num in range(1, 5):
            filter_options.append(f"📚 {units_data[unit_num]['name']}")
            for lesson_num in range(1, units_data[unit_num]["lessons"] + 1):
                count = question_counts[unit_num].get(lesson_num, 0)
                filter_options.append(f"   📖 {lesson_names[(unit_num, lesson_num)]} ({count} سؤال)")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            lesson_filter = st.selectbox("اختر المحتوى:", filter_options)
        with col2:
            num_q_choice = st.selectbox("عدد الأسئلة:", [10, 20, 30, 50, 100, "الكل"])
        with col3:
            quiz_types = ["كل الأسئلة", "اختيار من متعدد فقط", "صح أو خطأ فقط"]
            quiz_type_filter = st.selectbox("نوع الأسئلة:", quiz_types)
        
        # Calculate available questions based on filter
        filtered = all_questions.copy()
        
        # Filter by unit/lesson
        if lesson_filter.startswith("📚"):
            unit_num = None
            for u in range(1, 5):
                if units_data[u]["name"] in lesson_filter:
                    unit_num = u
                    break
            if unit_num:
                filtered = [q for q in filtered if q.get('unit') == unit_num]
        elif lesson_filter.startswith("   📖"):
            unit_num = None
            lesson_num = None
            for u in range(1, 5):
                for l in range(1, units_data[u]["lessons"] + 1):
                    if lesson_names[(u, l)] in lesson_filter:
                        unit_num = u
                        lesson_num = l
                        break
                if unit_num:
                    break
            if unit_num and lesson_num:
                filtered = [q for q in filtered if q.get('unit') == unit_num and q.get('lesson') == lesson_num]
        
        # Filter by question type
        if quiz_type_filter == "اختيار من متعدد فقط":
            filtered = [q for q in filtered if q.get('type') == 'mcq']
        elif quiz_type_filter == "صح أو خطأ فقط":
            filtered = [q for q in filtered if q.get('type') == 'truefalse']
        
        available_count = len(filtered)
        
        if num_q_choice == "الكل":
            num_q = available_count
        else:
            num_q = min(num_q_choice, available_count)
        
        st.markdown(f"""
        <div class='info-box' style='text-align: right;'>
        ℹ️ <b>عدد الأسئلة المتاحة:</b> {available_count} سؤال<br>
        ℹ️ <b>سيتم عرض:</b> {num_q} سؤال
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 بدء الاختبار", use_container_width=True):
            st.session_state.selected_questions = filtered[:num_q]
            st.session_state.quiz_started = True
            st.session_state.current_question = 0
            st.session_state.correct_count = 0
            st.session_state.wrong_count = 0
            st.session_state.show_answer = False
            st.session_state.question_results = {}
            st.rerun()
    else:
        current_q = st.session_state.selected_questions[st.session_state.current_question]
        q_num = st.session_state.current_question + 1
        total_q = len(st.session_state.selected_questions)
        q_id = f"q_{st.session_state.current_question}"
        
        unit_num = current_q.get('unit', 1)
        lesson_num = current_q.get('lesson', 1)
        q_type = current_q.get('type', 'mcq')
        
        # Unit and lesson badge
        unit_color = units_data[unit_num]["color"]
        unit_name = units_data[unit_num]["name"].split(":")[0]
        
        # Question type badge
        type_badge = "📝 اختيار من متعدد" if q_type == 'mcq' else "✓✗ صح أو خطأ"
        
        # Show question result indicator
        question_status = ""
        if q_id in st.session_state.question_results:
            if st.session_state.question_results[q_id]:
                question_status = "<span style='background: #28a745; color: white; padding: 5px 15px; border-radius: 15px; margin-right: 10px;'>✓ صحيح</span>"
            else:
                question_status = "<span style='background: #dc3545; color: white; padding: 5px 15px; border-radius: 15px; margin-right: 10px;'>✗ خطأ</span>"
        
        st.markdown(f"""
        <div style='text-align: center; margin-bottom: 15px;'>
            <span style='background: {unit_color}; color: white; padding: 8px 20px; border-radius: 20px; font-weight: bold;'>
                {unit_name}
            </span>
            <span class='lesson-tag lesson-tag-{lesson_num}' style='margin-right: 10px;'>{lesson_names[(unit_num, lesson_num)]}</span>
            <span style='background: #6c757d; color: white; padding: 5px 15px; border-radius: 15px; margin-right: 10px; font-size: 0.85rem;'>{type_badge}</span>
            {question_status}
        </div>
        """, unsafe_allow_html=True)
        
        st.progress(q_num / total_q)
        st.markdown(f"<p class='progress-text'>السؤال {q_num} من {total_q}</p>", unsafe_allow_html=True)
        
        lesson_class = f"lesson-{((lesson_num - 1) % 3) + 1}"
        question_text = current_q.get('q', current_q.get('question', 'سؤال'))
        st.markdown(f"<div class='question-card {lesson_class}'><h3 style='font-size: 1.3rem;'>❓ {question_text}</h3></div>", unsafe_allow_html=True)
        
        if not st.session_state.show_answer:
            for i, opt in enumerate(current_q['options']):
                if st.button(f"{i+1}. {opt}", key=f"opt_{i}", use_container_width=True):
                    st.session_state.user_answer = i
                    st.session_state.show_answer = True
                    is_correct = (i == current_q['correct'])
                    st.session_state.question_results[q_id] = is_correct
                    if is_correct:
                        st.session_state.correct_count += 1
                    else:
                        st.session_state.wrong_count += 1
                    st.rerun()
        else:
            user_ans = st.session_state.user_answer
            correct_ans = current_q['correct']
            
            if user_ans == correct_ans:
                st.markdown(f"""
                <div class='correct-answer' style='text-align: right;'>
                    ✅ <b>إجابة صحيحة!</b><br>
                    الإجابة الصحيحة: {current_q['options'][correct_ans]}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class='wrong-answer' style='text-align: right;'>
                    ❌ <b>إجابة خاطئة!</b><br>
                    إجابتك: {current_q['options'][user_ans]}<br>
                    الإجابة الصحيحة: {current_q['options'][correct_ans]}
                </div>
                """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col1:
                if q_num < total_q:
                    if st.button("⬅️ السؤال التالي", use_container_width=True):
                        st.session_state.current_question += 1
                        st.session_state.show_answer = False
                        st.rerun()
                else:
                    if st.button("🏁 إنهاء الاختبار", use_container_width=True):
                        st.session_state.quiz_started = False
                        st.rerun()
            with col3:
                if q_num > 1:
                    if st.button("السابق ➡️", use_container_width=True):
                        st.session_state.current_question -= 1
                        st.session_state.show_answer = False
                        st.rerun()
        
        st.markdown("---")
        
        # Question status summary
        st.markdown("<h4 style='text-align: right;'>📋 حالة الأسئلة:</h4>", unsafe_allow_html=True)
        status_cols = st.columns(min(10, total_q))
        for i in range(min(10, total_q)):
            check_id = f"q_{i}"
            if check_id in st.session_state.question_results:
                if st.session_state.question_results[check_id]:
                    status_cols[i].markdown(f"<div style='text-align: center; background: #28a745; color: white; padding: 5px; border-radius: 5px; font-size: 0.8rem;'>{i+1}✓</div>", unsafe_allow_html=True)
                else:
                    status_cols[i].markdown(f"<div style='text-align: center; background: #dc3545; color: white; padding: 5px; border-radius: 5px; font-size: 0.8rem;'>{i+1}✗</div>", unsafe_allow_html=True)
            else:
                is_current = (i == st.session_state.current_question)
                bg_color = "#ffc107" if is_current else "#e9ecef"
                text_color = "#000" if is_current else "#666"
                status_cols[i].markdown(f"<div style='text-align: center; background: {bg_color}; color: {text_color}; padding: 5px; border-radius: 5px; font-size: 0.8rem;'>{i+1}</div>", unsafe_allow_html=True)
        
        st.markdown("---")
        c1, c2, c3 = st.columns(3)
        c1.metric("✅ الإجابات الصحيحة", st.session_state.correct_count)
        c2.metric("❌ الإجابات الخاطئة", st.session_state.wrong_count)
        total = st.session_state.correct_count + st.session_state.wrong_count
        pct = (st.session_state.correct_count / total * 100) if total > 0 else 0
        c3.metric("📊 النسبة المئوية", f"{pct:.0f}%")

elif page == "📋 امتحان شامل":
    st.title("📋 امتحان شامل على جميع الوحدات")
    st.markdown("---")
    
    if not st.session_state.quiz_started:
        st.markdown("<h3 style='text-align: right;'>⚙️ إعدادات الامتحان الشامل</h3>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='info-box' style='text-align: right;'>
        📋 <b>الامتحان الشامل</b> يجمع أسئلة من جميع الوحدات الأربع<br>
        📝 مناسب للمراجعة النهائية قبل الامتحان
        </div>
        """, unsafe_allow_html=True)
        
        # Total available questions
        total_available = len(all_questions)
        
        col1, col2 = st.columns(2)
        with col1:
            num_q_choice = st.selectbox(
                "عدد الأسئلة:",
                [20, 50, 100, "الكل (جميع الأسئلة)"]
            )
        with col2:
            quiz_type = st.selectbox(
                "نوع الأسئلة:",
                ["كل الأسئلة", "اختيار من متعدد فقط", "صح أو خطأ فقط", "خليط متنوع"]
            )
        
        # Filter by type
        filtered = all_questions.copy()
        if quiz_type == "اختيار من متعدد فقط":
            filtered = [q for q in filtered if q.get('type') == 'mcq']
        elif quiz_type == "صح أو خطأ فقط":
            filtered = [q for q in filtered if q.get('type') == 'truefalse']
        elif quiz_type == "خليط متنوع":
            # Ensure mix of both types
            mcq = [q for q in filtered if q.get('type') == 'mcq']
            tf = [q for q in filtered if q.get('type') == 'truefalse']
            # Alternate between types
            filtered = []
            for i in range(max(len(mcq), len(tf))):
                if i < len(mcq):
                    filtered.append(mcq[i])
                if i < len(tf):
                    filtered.append(tf[i])
        
        available_count = len(filtered)
        
        if num_q_choice == "الكل (جميع الأسئلة)":
            num_q = available_count
        else:
            num_q = min(num_q_choice, available_count)
        
        # Show breakdown by unit
        st.markdown("<h4 style='text-align: right;'>📊 توزيع الأسئلة المتاحة:</h4>", unsafe_allow_html=True)
        
        breakdown_cols = st.columns(4)
        for i, unit_num in enumerate(range(1, 5)):
            unit_q_count = len([q for q in filtered if q.get('unit') == unit_num])
            with breakdown_cols[i]:
                st.markdown(f"""
                <div style='background: {units_data[unit_num]['color']}; color: white; padding: 15px; border-radius: 10px; text-align: center;'>
                    <div style='font-size: 1.5rem; font-weight: bold;'>{unit_q_count}</div>
                    <div style='font-size: 0.9rem;'>الوحدة {unit_num}</div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class='info-box' style='text-align: right; margin-top: 20px;'>
        ℹ️ <b>إجمالي الأسئلة المتاحة:</b> {available_count} سؤال<br>
        ℹ️ <b>سيتم عرض:</b> {num_q} سؤال
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 بدء الامتحان الشامل", use_container_width=True):
            # Get questions from all units, distributed proportionally
            st.session_state.selected_questions = filtered[:num_q]
            st.session_state.quiz_started = True
            st.session_state.current_question = 0
            st.session_state.correct_count = 0
            st.session_state.wrong_count = 0
            st.session_state.show_answer = False
            st.session_state.question_results = {}
            st.session_state.comp_exam_mode = True
            st.rerun()
    else:
        # This uses the same quiz interface as MCQ page
        current_q = st.session_state.selected_questions[st.session_state.current_question]
        q_num = st.session_state.current_question + 1
        total_q = len(st.session_state.selected_questions)
        q_id = f"q_{st.session_state.current_question}"
        
        unit_num = current_q.get('unit', 1)
        lesson_num = current_q.get('lesson', 1)
        q_type = current_q.get('type', 'mcq')
        
        # Unit badge
        unit_color = units_data[unit_num]["color"]
        unit_name = units_data[unit_num]["name"].split(":")[0]
        
        # Question type badge
        type_badge = "📝 اختيار من متعدد" if q_type == 'mcq' else "✓✗ صح أو خطأ"
        
        # Show question result indicator
        question_status = ""
        if q_id in st.session_state.question_results:
            if st.session_state.question_results[q_id]:
                question_status = "<span style='background: #28a745; color: white; padding: 5px 15px; border-radius: 15px; margin-right: 10px;'>✓ صحيح</span>"
            else:
                question_status = "<span style='background: #dc3545; color: white; padding: 5px 15px; border-radius: 15px; margin-right: 10px;'>✗ خطأ</span>"
        
        st.markdown(f"""
        <div style='text-align: center; margin-bottom: 15px;'>
            <span style='background: #6c5ce7; color: white; padding: 8px 20px; border-radius: 20px; font-weight: bold;'>
                📋 امتحان شامل
            </span>
            <span style='background: {unit_color}; color: white; padding: 5px 15px; border-radius: 15px; margin-right: 10px; font-size: 0.9rem;'>
                {unit_name}
            </span>
            <span style='background: #6c757d; color: white; padding: 5px 15px; border-radius: 15px; margin-right: 10px; font-size: 0.85rem;'>{type_badge}</span>
            {question_status}
        </div>
        """, unsafe_allow_html=True)
        
        st.progress(q_num / total_q)
        st.markdown(f"<p class='progress-text'>السؤال {q_num} من {total_q}</p>", unsafe_allow_html=True)
        
        lesson_class = f"lesson-{((lesson_num - 1) % 3) + 1}"
        question_text = current_q.get('q', current_q.get('question', 'سؤال'))
        st.markdown(f"<div class='question-card {lesson_class}'><h3 style='font-size: 1.3rem;'>❓ {question_text}</h3></div>", unsafe_allow_html=True)
        
        if not st.session_state.show_answer:
            for i, opt in enumerate(current_q['options']):
                if st.button(f"{i+1}. {opt}", key=f"opt_{i}", use_container_width=True):
                    st.session_state.user_answer = i
                    st.session_state.show_answer = True
                    is_correct = (i == current_q['correct'])
                    st.session_state.question_results[q_id] = is_correct
                    if is_correct:
                        st.session_state.correct_count += 1
                    else:
                        st.session_state.wrong_count += 1
                    st.rerun()
        else:
            user_ans = st.session_state.user_answer
            correct_ans = current_q['correct']
            
            if user_ans == correct_ans:
                st.markdown(f"""
                <div class='correct-answer' style='text-align: right;'>
                    ✅ <b>إجابة صحيحة!</b><br>
                    الإجابة الصحيحة: {current_q['options'][correct_ans]}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class='wrong-answer' style='text-align: right;'>
                    ❌ <b>إجابة خاطئة!</b><br>
                    إجابتك: {current_q['options'][user_ans]}<br>
                    الإجابة الصحيحة: {current_q['options'][correct_ans]}
                </div>
                """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col1:
                if q_num < total_q:
                    if st.button("⬅️ السؤال التالي", use_container_width=True):
                        st.session_state.current_question += 1
                        st.session_state.show_answer = False
                        st.rerun()
                else:
                    if st.button("🏁 إنهاء الامتحان", use_container_width=True):
                        st.session_state.quiz_started = False
                        st.session_state.comp_exam_mode = False
                        st.rerun()
            with col3:
                if q_num > 1:
                    if st.button("السابق ➡️", use_container_width=True):
                        st.session_state.current_question -= 1
                        st.session_state.show_answer = False
                        st.rerun()
        
        st.markdown("---")
        
        # Question status summary
        st.markdown("<h4 style='text-align: right;'>📋 حالة الأسئلة:</h4>", unsafe_allow_html=True)
        status_cols = st.columns(min(10, total_q))
        for i in range(min(10, total_q)):
            check_id = f"q_{i}"
            if check_id in st.session_state.question_results:
                if st.session_state.question_results[check_id]:
                    status_cols[i].markdown(f"<div style='text-align: center; background: #28a745; color: white; padding: 5px; border-radius: 5px; font-size: 0.8rem;'>{i+1}✓</div>", unsafe_allow_html=True)
                else:
                    status_cols[i].markdown(f"<div style='text-align: center; background: #dc3545; color: white; padding: 5px; border-radius: 5px; font-size: 0.8rem;'>{i+1}✗</div>", unsafe_allow_html=True)
            else:
                is_current = (i == st.session_state.current_question)
                bg_color = "#ffc107" if is_current else "#e9ecef"
                text_color = "#000" if is_current else "#666"
                status_cols[i].markdown(f"<div style='text-align: center; background: {bg_color}; color: {text_color}; padding: 5px; border-radius: 5px; font-size: 0.8rem;'>{i+1}</div>", unsafe_allow_html=True)
        
        # Score summary
        st.markdown("---")
        c1, c2, c3 = st.columns(3)
        c1.metric("✅ الإجابات الصحيحة", st.session_state.correct_count)
        c2.metric("❌ الإجابات الخاطئة", st.session_state.wrong_count)
        total = st.session_state.correct_count + st.session_state.wrong_count
        pct = (st.session_state.correct_count / total * 100) if total > 0 else 0
        c3.metric("📊 النسبة المئوية", f"{pct:.0f}%")
        
        # Unit breakdown in exam
        if total > 0:
            st.markdown("---")
            st.markdown("<h4 style='text-align: right;'>📊 الأداء حسب الوحدة:</h4>", unsafe_allow_html=True)
            unit_perf_cols = st.columns(4)
            for i, unit_num in enumerate(range(1, 5)):
                unit_correct = sum(1 for j, q in enumerate(st.session_state.selected_questions[:total]) 
                                  if q.get('unit') == unit_num and st.session_state.question_results.get(f"q_{j}", False))
                unit_total = sum(1 for q in st.session_state.selected_questions[:total] if q.get('unit') == unit_num)
                if unit_total > 0:
                    unit_pct = (unit_correct / unit_total * 100)
                    with unit_perf_cols[i]:
                        st.markdown(f"""
                        <div style='background: {units_data[unit_num]['color']}; color: white; padding: 15px; border-radius: 10px; text-align: center;'>
                            <div style='font-size: 1.2rem; font-weight: bold;'>{unit_pct:.0f}%</div>
                            <div style='font-size: 0.8rem;'>الوحدة {unit_num}</div>
                            <div style='font-size: 0.7rem;'>{unit_correct}/{unit_total}</div>
                        </div>
                        """, unsafe_allow_html=True)

elif page == "🎴 بطاقات التعلم":
    st.title("🎴 بطاقات التعلم (Flash Cards)")
    st.markdown("---")
    
    # Filter options
    col1, col2 = st.columns(2)
    with col1:
        unit_filter = st.selectbox(
            "اختر الوحدة:",
            ["الكل"] + [f"الوحدة {i}" for i in range(1, 5)]
        )
    with col2:
        if unit_filter != "الكل":
            unit_num = int(unit_filter.split("الوحدة ")[1])
            lesson_options = ["الكل"] + [f"الدرس {i}" for i in range(1, units_data[unit_num]["lessons"] + 1)]
        else:
            lesson_options = ["الكل"]
        lesson_filter = st.selectbox("اختر الدرس:", lesson_options)
    
    # Get filtered flashcards
    unit_num = None
    lesson_num = None
    if unit_filter != "الكل":
        unit_num = int(unit_filter.split("الوحدة ")[1])
    if lesson_filter != "الكل":
        lesson_num = int(lesson_filter.split("الدرس ")[1])
    
    flashcards = get_flashcards(unit_num, lesson_num)
    
    if not flashcards:
        st.info("📝 لا توجد بطاقات تعليمية متاحة لهذا الاختيار")
    else:
        st.markdown(f"<p class='progress-text'>البطاقة {st.session_state.flashcard_index + 1} من {len(flashcards)}</p>", unsafe_allow_html=True)
        st.progress((st.session_state.flashcard_index + 1) / len(flashcards))
        
        current_card = flashcards[st.session_state.flashcard_index]
        
        # Flash card display - use 'question'/'answer' keys from data
        if st.session_state.flashcard_show_answer:
            card_content = current_card.get('answer', current_card.get('a', ''))
            card_label = "📝 الإجابة:"
        else:
            card_content = current_card.get('question', current_card.get('q', ''))
            card_label = "❓ السؤال:"
        
        st.markdown(f"""
        <div class='flashcard'>
            <div style='color: #6c757d; font-size: 1rem; margin-bottom: 10px;'>{card_label}</div>
            <div class='flashcard-front'>{card_content}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Control buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("⬅️ البطاقة التالية", use_container_width=True):
                st.session_state.flashcard_index = (st.session_state.flashcard_index + 1) % len(flashcards)
                st.session_state.flashcard_show_answer = False
                st.rerun()
        with col2:
            if st.button("🔄 اقلب البطاقة", use_container_width=True):
                st.session_state.flashcard_show_answer = not st.session_state.flashcard_show_answer
                st.rerun()
        with col3:
            if st.button("السابقة ➡️", use_container_width=True):
                st.session_state.flashcard_index = (st.session_state.flashcard_index - 1) % len(flashcards)
                st.session_state.flashcard_show_answer = False
                st.rerun()
        
        st.markdown("---")
        
        # Jump to specific card
        jump_cols = st.columns(10)
        for i in range(min(10, len(flashcards))):
            if jump_cols[i].button(f"{i+1}", key=f"fc_{i}"):
                st.session_state.flashcard_index = i
                st.session_state.flashcard_show_answer = False
                st.rerun()

elif page == "📊 إحصائيات":
    st.title("📊 إحصائيات التعلم")
    st.markdown("---")
    
    # Count by unit
    unit_counts = {}
    for unit_num in range(1, 5):
        unit_counts[unit_num] = len([q for q in all_questions if q.get('unit') == unit_num])
    
    # Stats cards
    col1, col2, col3, col4 = st.columns(4)
    for i, (unit_num, count) in enumerate(unit_counts.items()):
        with [col1, col2, col3, col4][i]:
            st.markdown(f"""
            <div style='background: {units_data[unit_num]["color"]}; color: white; padding: 20px; border-radius: 15px; text-align: center;'>
                <div style='font-size: 2rem;'>📚</div>
                <div style='font-size: 1.8rem; font-weight: bold;'>{count}</div>
                <div>الوحدة {unit_num}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Lesson breakdown
    st.markdown("<h3 style='text-align: right;'>📊 توزيع الأسئلة حسب الدرس</h3>", unsafe_allow_html=True)
    
    for unit_num in range(1, 5):
        st.markdown(f"<h4 style='color: {units_data[unit_num]['color']};'>📚 {units_data[unit_num]['name']}</h4>", unsafe_allow_html=True)
        lesson_cols = st.columns(units_data[unit_num]["lessons"])
        for lesson_num in range(1, units_data[unit_num]["lessons"] + 1):
            mcq_count = len([q for q in all_questions if q.get('unit') == unit_num and q.get('lesson') == lesson_num and q.get('type') == 'mcq'])
            tf_count = len([q for q in all_questions if q.get('unit') == unit_num and q.get('lesson') == lesson_num and q.get('type') == 'truefalse'])
            with lesson_cols[lesson_num - 1]:
                st.markdown(f"""
                <div style='background: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center; border-right: 4px solid {units_data[unit_num]["color"]};'>
                    <div style='font-size: 1.2rem; font-weight: bold; color: {units_data[unit_num]["color"]};'>الدرس {lesson_num}</div>
                    <div style='font-size: 0.9rem; color: #28a745;'>📝 {mcq_count} اختيار</div>
                    <div style='font-size: 0.9rem; color: #17a2b8;'>✓✗ {tf_count} صح/خطأ</div>
                </div>
                """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Flashcards stats
    st.markdown("<h3 style='text-align: right;'>🎴 إحصائيات البطاقات التعليمية</h3>", unsafe_allow_html=True)
    total_flashcards = len(get_flashcards())
    st.metric("إجمالي البطاقات التعليمية", total_flashcards)
    
    st.markdown("---")
    st.markdown("<h3 style='text-align: right;'>📈 تقدمك في الاختبارات</h3>", unsafe_allow_html=True)
    
    total_answered = st.session_state.correct_count + st.session_state.wrong_count
    if total_answered > 0:
        c1, c2 = st.columns(2)
        c1.metric("✅ الإجابات الصحيحة", st.session_state.correct_count)
        c2.metric("❌ الإجابات الخاطئة", st.session_state.wrong_count)
        
        pct = (st.session_state.correct_count / total_answered * 100)
        
        if pct >= 80:
            st.success(f"🎉 ممتاز! نسبة نجاحك {pct:.0f}%")
        elif pct >= 60:
            st.warning(f"👍 جيد! نسبة نجاحك {pct:.0f}%")
        else:
            st.error(f"📚 تحتاج لمزيد من المذاكرة. نسبة نجاحك {pct:.0f}%")
    else:
        st.info("📝 لم تقم بأي اختبارات بعد. ابدأ من صفحة 'اختبار MCQ'")
    
    st.markdown("---")
    if st.button("🔄 إعادة تعيين الإحصائيات", use_container_width=True):
        st.session_state.correct_count = 0
        st.session_state.wrong_count = 0
        st.session_state.question_results = {}
        st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown(f"""
<div style='text-align: right;'>
📝 <b>تطبيق مينا للمذاكرة</b><br><br>
علوم - صف ثانى إعدادى - ترم ثان<br><br>
✅ <b>المحتوى:</b><br>
• 4 وحدات<br>
• {sum(len(u['slides']) for u in units_data.values())} شريحة<br>
• {len(all_questions)} سؤال اختبار<br>
• {len(get_flashcards())} بطاقة تعليمية
</div>
""", unsafe_allow_html=True)
