import streamlit as st
import sys
sys.path.append('app_data')
from questions import questions as unit1_questions
from unit2_questions import questions as unit2_questions
from unit2_slides import slides as unit2_slides

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
    .lesson-4 { border-right-color: #ff6b6b !important; }
    
    /* Progress */
    .progress-text {
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        color: #1e3a5f;
        margin: 15px 0;
    }
    
    /* Slide navigation container */
    .slide-nav {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        justify-content: center;
        margin: 20px 0;
        padding: 15px;
        background: #f8f9fa;
        border-radius: 15px;
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
    
    /* Number buttons for slides */
    .slide-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        width: 45px !important;
        height: 45px !important;
        font-weight: bold !important;
        font-size: 1rem !important;
    }
    
    .slide-btn:hover {
        transform: scale(1.1) !important;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4) !important;
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
    
    /* Sidebar */
    .css-1lcbmhc {
        direction: rtl;
    }
    
    /* Fix for columns RTL */
    .row-widget.stHorizontalBlock {
        direction: rtl;
    }
    
    /* Main content area */
    .main {
        direction: rtl;
    }
    
    /* Question result indicators */
    .question-correct {
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%) !important;
        color: white !important;
    }
    
    .question-wrong {
        background: linear-gradient(135deg, #dc3545 0%, #e74c3c 100%) !important;
        color: white !important;
    }
    
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
    .lesson-tag-4 { background: #ff6b6b; color: white; }
</style>
""", unsafe_allow_html=True)

# Initialize session state
for key in ['current_slide', 'current_question', 'quiz_started', 'show_answer', 'correct_count', 'wrong_count', 'selected_unit', 'question_results']:
    if key not in st.session_state:
        if key == 'question_results':
            st.session_state[key] = {}
        elif key in ['correct_count', 'wrong_count', 'current_slide', 'current_question', 'selected_unit']:
            st.session_state[key] = 0
        else:
            st.session_state[key] = False

if 'current_slide_u2' not in st.session_state:
    st.session_state.current_slide_u2 = 0

# Combine all questions with proper lesson info
all_questions = []
for q in unit1_questions:
    q_copy = q.copy()
    q_copy['unit'] = 1
    # Ensure lesson is set (default to 1 if not present)
    if 'lesson' not in q_copy:
        q_copy['lesson'] = 1
    all_questions.append(q_copy)
for q in unit2_questions:
    q_copy = q.copy()
    q_copy['unit'] = 2
    q_copy['lesson'] = 4  # Unit 2 lessons start at 4
    all_questions.append(q_copy)

# Lesson names
lesson_names = {
    1: "الدرس الأول: التغيرات الفيزيائية",
    2: "الدرس الثاني: التغيرات الكيميائية", 
    3: "الدرس الثالث: التطبيقات العملية",
    4: "الوحدة الثانية: الكهروكيمياء"
}

# Unit 1 slides
unit1_slides = [
    {"title": "📘 الوحدة الأولى: التغيرات الحرارية", "content": """
    <div class='content-box'>
    <h3>🎯 أهداف الوحدة:</h3>
    <ul>
    <li>التعرف على المواد المتهدرجة والمواد غير المتهدرجة (الهيدرات)</li>
    <li>تمييز بين حرارة الذوبان الطارحة والماصة</li>
    <li>الأحمال الحرارية عند تبخر الماء</li>
    <li>تحديد علاقة الذوبان بالتغير الحراري</li>
    <li>تطبيقات حياتية على التغيرات الحرارية</li>
    </ul>
    </div>"""},
    {"title": "🔥 حرارة الذوبان", "content": """
    <div class='content-box'>
    <h3>📌 تعريف حرارة الذوبان:</h3>
    <p>هي كمية الحرارة المتبادلة عند <span class='highlight'>ذوبان مادة</span> في <span class='highlight'>مذيب</span></p>
    <div class='formula-box'>ΔT = T₂ - T₁<br>T₁ = الحرارة الابتدائية | T₂ = الحرارة النهائية</div>
    <h3>أنواع الذوبان:</h3>
    <ul>
    <li><b>طارح للحرارة:</b> يرتفعت درجة الحرارة (ΔT موجب)</li>
    <li><b>ماص للحرارة:</b> تنخفض درجة الحرارة (ΔT سالب)</li>
    </ul>
    </div>"""},
    {"title": "⚗️ أمثلة على الذوبان", "content": """
    <div class='content-box'>
    <h3>🔥 مواد طارحة للحرارة:</h3>
    <ul><li>NaOH - هيدروكسيد الصوديوم</li><li>CaCl₂ - كلوريد الكالسيوم</li><li>CuSO₄ - كبريتات النحاس</li></ul>
    <h3>❄️ مواد ماصة للحرارة:</h3>
    <ul><li>NH₄NO₃ - نترات الأمونيوم</li><li>K₂SO₄ - كبريتات البوتاسيوم</li><li>NaHCO₃ - بيكربونات الصوديوم</li></ul>
    </div>"""},
    {"title": "🧪 دورة التبريد", "content": """
    <div class='content-box'>
    <h3>🔄 دورة التبريد في الثلاجات:</h3>
    <h4>عملية طارحة للحرارة:</h4>
    <ul><li>الضغط: يرتفع ضغط الغاز → ارتفاع الحرارة</li><li>التكثف: يتحول الغاز لسائل ويطلق حرارة</li></ul>
    <h4>عملية ماصة للحرارة:</h4>
    <ul><li>التمدد: يصبح السائل غازاً</li><li>التبخر: يمتص الغاز الحرارة من الثلاجة</li></ul>
    <div class='formula-box'>دورة: ضغط ← تكثف ← تمدد ← تبخر</div>
    </div>"""},
    {"title": "🩹 كمادات الضغط", "content": """
    <div class='content-box'>
    <h3>❄️ كمادات باردة:</h3>
    <ul><li><b>المادة:</b> NH₄NO₃</li><li><b>الاستخدام:</b> تبريد الكدمات</li></ul>
    <h3>🔥 كمادات ساخنة:</h3>
    <ul><li><b>المادة:</b> CaCl₂</li><li><b>الاستخدام:</b> تسكين آلام العضلات</li></ul>
    </div>"""},
    {"title": "📗 الدرس الثاني: التغيرات الكيميائية", "content": """
    <div class='content-box'>
    <h3>🎯 أهداف الدرس:</h3>
    <ul>
    <li>قانون بقاء الطاقة</li>
    <li>كسر ونكون الروابط</li>
    <li>التفاعلات الطارحة والماصة</li>
    <li>تطبيقات عملية</li>
    </ul>
    </div>"""},
    {"title": "⚖️ قانون بقاء الطاقة", "content": """
    <div class='content-box'>
    <p style='font-size: 18px; background: #e8e8e8; padding: 15px; text-align: center;'><b>"الطاقة لا تفنى ولا تستحدث من العدم، إنما تتحول من صورة إلى أخرى"</b></p>
    <div class='info-box'><b>تفاعل طارح:</b> تحول طاقة كيميائية → حرارية</div>
    <div class='info-box'><b>تفاعل ماص:</b> امتصاص طاقة حرارية من الوسط</div>
    </div>"""},
    {"title": "🔗 كسر ونكون الروابط", "content": """
    <div class='content-box'>
    <h3>✂️ كسر الروابط:</h3>
    <ul><li>يتطلب <span class='highlight'>طاقة</span> (ماص)</li></ul>
    <h3>🔗 نكون الروابط:</h3>
    <ul><li>ينتج <span class='highlight'>طاقة</span> (طارح)</li></ul>
    <div class='formula-box'>ΔH = طاقة كسر - طاقة تكوين</div>
    </div>"""},
    {"title": "📊 مقارنة التفاعلات", "content": """
    <div class='content-box'>
    <table style='width: 100%;'><tr style='background: #667eea; color: white;'><th style='padding: 10px;'>طارح</th><th style='padding: 10px;'>ماص</th></tr>
    <tr><td style='padding: 10px; border: 1px solid #ddd;'>يطلق حرارة</td><td style='padding: 10px; border: 1px solid #ddd;'>يمتص حرارة</td></tr>
    <tr style='background: #f5f5f5;'><td style='padding: 10px; border: 1px solid #ddd;'>ΔH سالب</td><td style='padding: 10px; border: 1px solid #ddd;'>ΔH موجب</td></tr>
    </table>
    </div>"""},
    {"title": "🔥 تفاعلات طارحة", "content": """
    <div class='content-box'>
    <p><b>1️⃣ Mg + HCl:</b></p><div class='formula-box'>Mg + 2HCl → MgCl₂ + H₂ + طاقة</div>
    <p><b>2️⃣ تفاعل الثرميت:</b></p><div class='formula-box'>2Al + Fe₂O₃ → Al₂O₃ + 2Fe + طاقة</div>
    </div>"""},
    {"title": "❄️ تفاعلات ماصة", "content": """
    <div class='content-box'>
    <p><b>BaCl₂ + NH₄Cl:</b></p><div class='formula-box'>يمتص حرارة</div>
    <p><b>تحلل CaCO₃:</b></p><div class='formula-box'>CaCO₃ → CaO + CO₂</div>
    </div>"""},
    {"title": "🏗️ تطبيقات", "content": """
    <div class='content-box'>
    <h3>🔥 تسخين فوري:</h3><ul><li>CaO + H₂O → Ca(OH)₂ + حرارة</li></ul>
    <h3>🔥 تفاعل الثرميت:</h3><ul><li>2500°C - لحام السكك</li></ul>
    <h3>❄️ تبريد كيميائي:</h3><ul><li>BaCl₂ + NH₄Cl</li></ul>
    </div>"""},
    {"title": "🎯 ملخص الوحدة الأولى", "content": """
    <div class='content-box'>
    <div class='info-box'><b>الذوبان:</b> تغير فيزيائي</div>
    <div class='info-box'><b>التفاعل:</b> تغير كيميائي</div>
    <div class='info-box'><b>كسر روابط =</b> امتصاص طاقة</div>
    <div class='info-box'><b>تكوين روابط =</b> تحرير طاقة</div>
    </div>"""},
]

# Sidebar
st.sidebar.markdown("<h1 style='text-align: right;'>📚 قائمة التنقل</h1>", unsafe_allow_html=True)
page = st.sidebar.radio("", ["🏠 الرئيسية", "📖 الوحدة الأولى", "📖 الوحدة الثانية", "❓ اختبار MCQ", "📊 إحصائيات"], label_visibility="collapsed")

if page == "🏠 الرئيسية":
    st.title("📚 مرحباً بك في تطبيق مينا للمذاكرة")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class='stat-card'>
            <div style='font-size: 3rem;'>📖</div>
            <h3>25 شريحة</h3>
            <p>وحدتان تعليميتان</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class='stat-card'>
            <div style='font-size: 3rem;'>❓</div>
            <h3>{len(all_questions)} سؤال</h3>
            <p>أسئلة متعددة الخيارات</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='stat-card'>
            <div style='font-size: 3rem;'>🎯</div>
            <h3>100% مجاني</h3>
            <p>تعلم بلا حدود</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Count questions by lesson
    lesson_counts = {}
    for q in all_questions:
        lesson = q.get('lesson', 1)
        lesson_counts[lesson] = lesson_counts.get(lesson, 0) + 1
    
    st.markdown("""
    <div style='text-align: right; font-size: 1.1rem; line-height: 2;'>
    
    ### 📋 محتوى التطبيق:
    
    <div class='info-box'>
    <b>📘 الوحدة الأولى: الطاقة الحرارية وتغيرات المادة</b><br>
    • {lesson1} سؤال - الدرس الأول: التغيرات الفيزيائية<br>
    • {lesson2} سؤال - الدرس الثاني: التغيرات الكيميائية<br>
    • {lesson3} سؤال - الدرس الثالث: التطبيقات العملية<br>
    </div>
    
    <div class='info-box'>
    <b>📗 الوحدة الثانية: الكيمياء الكهروكيميائية</b><br>
    • {lesson4} سؤال - الكهروكيمياء<br>
    </div>
    
    <div class='success-box'>
    ✅ <b>مميزات التطبيق:</b><br>
    • أسئلة بنفس الترتيب دائماً (للمذاكرة الجماعية)<br>
    • شرائح تفاعلية<br>
    • تتبع الإجابات الصحيحة والخاطئة لكل سؤال<br>
    • إحصائيات التقدم
    </div>
    
    </div>
    """.format(
        lesson1=lesson_counts.get(1, 0),
        lesson2=lesson_counts.get(2, 0),
        lesson3=lesson_counts.get(3, 0),
        lesson4=lesson_counts.get(4, 0)
    ), unsafe_allow_html=True)

elif page == "📖 الوحدة الأولى":
    st.markdown("<div class='unit-badge unit-1'>الوحدة الأولى</div>", unsafe_allow_html=True)
    st.title("التغيرات الحرارية")
    st.markdown("---")
    
    # Progress
    st.markdown(f"<p class='progress-text'>الشريحة {st.session_state.current_slide + 1} من {len(unit1_slides)}</p>", unsafe_allow_html=True)
    st.progress((st.session_state.current_slide + 1) / len(unit1_slides))
    
    # Navigation
    st.markdown("<div style='text-align: center; margin: 20px 0;'><b>اختر الشريحة:</b></div>", unsafe_allow_html=True)
    cols = st.columns(7)
    for i in range(min(7, len(unit1_slides))):
        btn_type = "primary" if i == st.session_state.current_slide else "secondary"
        if cols[i].button(f"{i+1}", key=f"u1_{i}", type=btn_type):
            st.session_state.current_slide = i
            st.rerun()
    
    if len(unit1_slides) > 7:
        cols2 = st.columns(6)
        for i in range(6):
            idx = i + 7
            if idx < len(unit1_slides):
                btn_type = "primary" if idx == st.session_state.current_slide else "secondary"
                if cols2[i].button(f"{idx+1}", key=f"u1_{idx}", type=btn_type):
                    st.session_state.current_slide = idx
                    st.rerun()
    
    st.markdown("---")
    
    # Content
    current = unit1_slides[st.session_state.current_slide]
    st.markdown(f"<h2 style='text-align: center; color: #667eea;'>{current['title']}</h2>", unsafe_allow_html=True)
    st.markdown(current['content'], unsafe_allow_html=True)
    
    # Nav buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.session_state.current_slide < len(unit1_slides) - 1:
            if st.button("⬅️ التالي", use_container_width=True):
                st.session_state.current_slide += 1
                st.rerun()
    with col3:
        if st.session_state.current_slide > 0:
            if st.button("السابق ➡️", use_container_width=True):
                st.session_state.current_slide -= 1
                st.rerun()

elif page == "📖 الوحدة الثانية":
    st.markdown("<div class='unit-badge unit-2'>الوحدة الثانية</div>", unsafe_allow_html=True)
    st.title("الكيمياء الكهروكيميائية")
    st.markdown("---")
    
    current_slide = st.session_state.current_slide_u2
    
    # Progress
    st.markdown(f"<p class='progress-text'>الشريحة {current_slide + 1} من {len(unit2_slides)}</p>", unsafe_allow_html=True)
    st.progress((current_slide + 1) / len(unit2_slides))
    
    # Navigation
    st.markdown("<div style='text-align: center; margin: 20px 0;'><b>اختر الشريحة:</b></div>", unsafe_allow_html=True)
    cols = st.columns(6)
    for i in range(min(6, len(unit2_slides))):
        btn_type = "primary" if i == current_slide else "secondary"
        if cols[i].button(f"{i+1}", key=f"u2_{i}", type=btn_type):
            st.session_state.current_slide_u2 = i
            st.rerun()
    
    if len(unit2_slides) > 6:
        cols2 = st.columns(5)
        for i in range(5):
            idx = i + 6
            if idx < len(unit2_slides):
                btn_type = "primary" if idx == current_slide else "secondary"
                if cols2[i].button(f"{idx+1}", key=f"u2_{idx}", type=btn_type):
                    st.session_state.current_slide_u2 = idx
                    st.rerun()
    
    st.markdown("---")
    
    # Content
    current = unit2_slides[current_slide]
    st.markdown(f"<h2 style='text-align: center; color: #ff6b6b;'>{current['title']}</h2>", unsafe_allow_html=True)
    st.markdown(current['content'], unsafe_allow_html=True)
    
    # Nav buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if current_slide < len(unit2_slides) - 1:
            if st.button("⬅️ التالي", use_container_width=True):
                st.session_state.current_slide_u2 += 1
                st.rerun()
    with col3:
        if current_slide > 0:
            if st.button("السابق ➡️", use_container_width=True):
                st.session_state.current_slide_u2 -= 1
                st.rerun()

elif page == "❓ اختبار MCQ":
    st.title("❓ اختبار الأسئلة متعددة الخيارات")
    st.markdown("---")
    
    if not st.session_state.quiz_started:
        st.markdown("<h3 style='text-align: right;'>⚙️ إعدادات الاختبار</h3>", unsafe_allow_html=True)
        
        # Count available questions
        lesson_counts = {}
        for q in all_questions:
            lesson = q.get('lesson', 1)
            lesson_counts[lesson] = lesson_counts.get(lesson, 0) + 1
        
        unit1_total = lesson_counts.get(1, 0) + lesson_counts.get(2, 0) + lesson_counts.get(3, 0)
        unit2_total = lesson_counts.get(4, 0)
        
        # Number of questions - allow ALL questions
        max_questions = len(all_questions)
        
        col1, col2 = st.columns(2)
        with col1:
            # Allow up to all questions (531)
            num_q_options = [10, 20, 50, 100, 200, "الكل"]
            num_q_choice = st.selectbox("عدد الأسئلة:", num_q_options, index=3)
            if num_q_choice == "الكل":
                num_q = max_questions
            else:
                num_q = num_q_choice
        
        with col2:
            filter_options = [
                "الكل",
                "📘 الوحدة الأولى - الدرس الأول (التغيرات الفيزيائية)",
                "📘 الوحدة الأولى - الدرس الثاني (التغيرات الكيميائية)",
                "📘 الوحدة الأولى - الدرس الثالث (التطبيقات)",
                "📗 الوحدة الثانية (الكهروكيمياء)"
            ]
            lesson_filter = st.selectbox("تصفية حسب:", filter_options)
        
        # Show count
        filtered_preview = all_questions.copy()
        if lesson_filter == "📘 الوحدة الأولى - الدرس الأول (التغيرات الفيزيائية)":
            filtered_preview = [q for q in filtered_preview if q.get('lesson', 1) == 1]
        elif lesson_filter == "📘 الوحدة الأولى - الدرس الثاني (التغيرات الكيميائية)":
            filtered_preview = [q for q in filtered_preview if q.get('lesson', 1) == 2]
        elif lesson_filter == "📘 الوحدة الأولى - الدرس الثالث (التطبيقات)":
            filtered_preview = [q for q in filtered_preview if q.get('lesson', 1) == 3]
        elif lesson_filter == "📗 الوحدة الثانية (الكهروكيمياء)":
            filtered_preview = [q for q in filtered_preview if q.get('lesson', 1) == 4]
        
        available_count = len(filtered_preview)
        actual_num_q = min(num_q, available_count) if isinstance(num_q, int) else available_count
        
        st.markdown(f"""
        <div class='info-box' style='text-align: right;'>
        ℹ️ <b>عدد الأسئلة المتاحة:</b> {available_count} سؤال
        </div>
        """, unsafe_allow_html=True)
        
        # Question stats
        st.markdown("<h4 style='text-align: right;'>📊 توزيع الأسئلة:</h4>", unsafe_allow_html=True)
        stat_cols = st.columns(4)
        with stat_cols[0]:
            st.metric("الدرس الأول", lesson_counts.get(1, 0))
        with stat_cols[1]:
            st.metric("الدرس الثاني", lesson_counts.get(2, 0))
        with stat_cols[2]:
            st.metric("الدرس الثالث", lesson_counts.get(3, 0))
        with stat_cols[3]:
            st.metric("الوحدة الثانية", lesson_counts.get(4, 0))
        
        if st.button("🚀 بدء الاختبار", use_container_width=True):
            filtered = all_questions.copy()
            
            # Apply lesson filter
            if lesson_filter == "📘 الوحدة الأولى - الدرس الأول (التغيرات الفيزيائية)":
                filtered = [q for q in filtered if q.get('lesson', 1) == 1]
            elif lesson_filter == "📘 الوحدة الأولى - الدرس الثاني (التغيرات الكيميائية)":
                filtered = [q for q in filtered if q.get('lesson', 1) == 2]
            elif lesson_filter == "📘 الوحدة الأولى - الدرس الثالث (التطبيقات)":
                filtered = [q for q in filtered if q.get('lesson', 1) == 3]
            elif lesson_filter == "📗 الوحدة الثانية (الكهروكيمياء)":
                filtered = [q for q in filtered if q.get('lesson', 1) == 4]
            
            # Sequential order (not random)
            if isinstance(num_q, int):
                n = min(num_q, len(filtered))
            else:
                n = len(filtered)
            
            st.session_state.selected_questions = filtered[:n]
            st.session_state.quiz_started = True
            st.session_state.current_question = 0
            st.session_state.correct_count = 0
            st.session_state.wrong_count = 0
            st.session_state.show_answer = False
            # Reset question results for new quiz
            st.session_state.question_results = {}
            st.rerun()
    else:
        current_q = st.session_state.selected_questions[st.session_state.current_question]
        q_num = st.session_state.current_question + 1
        total_q = len(st.session_state.selected_questions)
        q_id = f"q_{st.session_state.current_question}"
        
        # Unit and lesson badge
        unit_color = "#667eea" if current_q.get('unit', 1) == 1 else "#ff6b6b"
        unit_name = "الوحدة الأولى" if current_q.get('unit', 1) == 1 else "الوحدة الثانية"
        lesson_num = current_q.get('lesson', 1)
        lesson_name = lesson_names.get(lesson_num, f"الدرس {lesson_num}")
        
        # Show question result indicator if already answered
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
            <span class='lesson-tag lesson-tag-{lesson_num}' style='margin-right: 10px;'>{lesson_name}</span>
            {question_status}
        </div>
        """, unsafe_allow_html=True)
        
        st.progress(q_num / total_q)
        st.markdown(f"<p class='progress-text'>السؤال {q_num} من {total_q}</p>", unsafe_allow_html=True)
        
        lesson_class = f"lesson-{current_q.get('lesson', 1)}"
        st.markdown(f"<div class='question-card {lesson_class}'><h3 style='font-size: 1.3rem;'>❓ {current_q['q']}</h3></div>", unsafe_allow_html=True)
        
        if not st.session_state.show_answer:
            for i, opt in enumerate(current_q['options']):
                if st.button(f"{i+1}. {opt}", key=f"opt_{i}", use_container_width=True):
                    st.session_state.user_answer = i
                    st.session_state.show_answer = True
                    is_correct = (i == current_q['correct'])
                    # Store result for this question
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
        
        # Show question status summary
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

elif page == "📊 إحصائيات":
    st.title("📊 إحصائيات التعلم")
    st.markdown("---")
    
    unit1_count = len([q for q in all_questions if q.get('unit', 1) == 1])
    unit2_count = len([q for q in all_questions if q.get('unit', 1) == 2])
    
    # Count by lesson
    lesson_counts = {}
    for q in all_questions:
        lesson = q.get('lesson', 1)
        lesson_counts[lesson] = lesson_counts.get(lesson, 0) + 1
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class='stat-card'>
            <div style='font-size: 2.5rem;'>📚</div>
            <h3>{len(all_questions)}</h3>
            <p>إجمالي الأسئلة</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class='stat-card'>
            <div style='font-size: 2.5rem;'>📘</div>
            <h3>{unit1_count}</h3>
            <p>الوحدة الأولى</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class='stat-card'>
            <div style='font-size: 2.5rem;'>📗</div>
            <h3>{unit2_count}</h3>
            <p>الوحدة الثانية</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Lesson breakdown
    st.markdown("---")
    st.markdown("<h3 style='text-align: right;'>📊 توزيع الأسئلة حسب الدرس</h3>", unsafe_allow_html=True)
    
    lesson_cols = st.columns(4)
    lesson_data = [
        ("الدرس الأول", lesson_counts.get(1, 0), "#667eea"),
        ("الدرس الثاني", lesson_counts.get(2, 0), "#11998e"),
        ("الدرس الثالث", lesson_counts.get(3, 0), "#f093fb"),
        ("الوحدة الثانية", lesson_counts.get(4, 0), "#ff6b6b"),
    ]
    for i, (name, count, color) in enumerate(lesson_data):
        lesson_cols[i].markdown(f"""
        <div style='background: {color}; color: white; padding: 20px; border-radius: 15px; text-align: center;'>
            <div style='font-size: 1.5rem; font-weight: bold;'>{count}</div>
            <div>{name}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<h3 style='text-align: right;'>📈 تقدمك في الاختبارات</h3>", unsafe_allow_html=True)
    
    total_answered = st.session_state.correct_count + st.session_state.wrong_count
    if total_answered > 0:
        c1, c2 = st.columns(2)
        c1.metric("✅ الإجابات الصحيحة", st.session_state.correct_count)
        c2.metric("❌ الإجابات الخاطئة", st.session_state.wrong_count)
        
        try:
            import plotly.graph_objects as go
            fig = go.Figure(data=[go.Pie(
                labels=['صحيحة', 'خاطئة'],
                values=[st.session_state.correct_count, st.session_state.wrong_count],
                marker_colors=['#28a745', '#dc3545'],
                textinfo='percent+label',
                textfont=dict(size=16)
            )])
            fig.update_layout(
                title_text='نسبة الإجابات',
                title_x=0.5,
                title_font_size=20
            )
            st.plotly_chart(fig, use_container_width=True)
        except:
            pass
    else:
        st.info("📝 لم تقم بأي اختبارات بعد. ابدأ من صفحة 'اختبار MCQ'")
    
    st.markdown("---")
    if st.button("🔄 إعادة تعيين الإحصائيات", use_container_width=True):
        st.session_state.correct_count = 0
        st.session_state.wrong_count = 0
        st.session_state.question_results = {}
        st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style='text-align: right;'>
📝 <b>تطبيق مينا للمذاكرة</b><br><br>
تعلم الكيمياء بطريقة تفاعلية!<br><br>
✅ <b>مميزات التطبيق:</b><br>
• {total} سؤال متاح<br>
• أسئلة بنفس الترتيب دائماً<br>
• تصفية حسب الدرس<br>
• شرائح تفاعلية
</div>
""".format(total=len(all_questions)), unsafe_allow_html=True)
