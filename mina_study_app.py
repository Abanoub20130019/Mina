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

# CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@400;600;700&display=swap');
    * { font-family: 'Noto Naskh Arabic', sans-serif; }
    
    .content-box {
        background: #f8f9fa;
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        border-right: 5px solid #667eea;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .question-card {
        background: #f8f9fa;
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        border-right: 5px solid #11998e;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .formula-box {
        background: #1e3a5f;
        color: #00d4ff;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin: 15px 0;
        font-family: monospace;
    }
    
    .stat-card {
        background: linear-gradient(145deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
    }
    
    .correct-answer {
        background: #28a745;
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    .wrong-answer {
        background: #dc3545;
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    .info-box {
        background: #e3f2fd;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-right: 4px solid #2196f3;
    }
    
    .warning-box {
        background: #fff3cd;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-right: 4px solid #ffc107;
    }
    
    .highlight {
        background: #a8edea;
        padding: 2px 8px;
        border-radius: 4px;
    }
    
    .lesson-1 { border-right-color: #667eea !important; }
    .lesson-2 { border-right-color: #11998e !important; }
    .lesson-3 { border-right-color: #f093fb !important; }
    .lesson-4 { border-right-color: #ff6b6b !important; }
    
    h1 {
        color: #1e3a5f;
        text-align: center;
        border-bottom: 3px solid #667eea;
        padding-bottom: 10px;
    }
    
    h2, h3 { color: #1e3a5f; }
    
    .progress-text {
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        color: #1e3a5f;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
for key in ['current_slide', 'current_question', 'quiz_started', 'show_answer', 'correct_count', 'wrong_count', 'selected_unit']:
    if key not in st.session_state:
        st.session_state[key] = 0 if 'count' in key or 'slide' in key or 'question' in key else False

# Combine all questions with unit identifiers
all_questions = []
for q in unit1_questions:
    q_copy = q.copy()
    q_copy['unit'] = 1
    all_questions.append(q_copy)
for q in unit2_questions:
    q_copy = q.copy()
    q_copy['unit'] = 2
    q_copy['lesson'] = 4  # Unit 2 is lesson 4
    all_questions.append(q_copy)

# Unit 1 slides
unit1_slides = [
    {"title": "📘 الوحدة الأولى: التغيرات الفيزيائية للتغيرات الحرارية", "content": """
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
st.sidebar.title("📚 قائمة التنقل")
page = st.sidebar.radio("", ["🏠 الرئيسية", "📖 الوحدة الأولى", "📖 الوحدة الثانية", "❓ اختبار MCQ", "📊 إحصائيات"], label_visibility="collapsed")

if page == "🏠 الرئيسية":
    st.title("📚 مرحباً بك في تطبيق مينا للمذاكرة")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='stat-card'><h2>📖</h2><h3>25 شريحة</h3><p>وحدتان تعليميتان</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='stat-card'><h2>❓</h2><h3>{len(all_questions)} سؤال</h3><p>أسئلة متعددة الخيارات</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='stat-card'><h2>🎯</h2><h3>100% مجاني</h3><p>تعلم بلا حدود</p></div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
    ### 📋 محتوى التطبيق:
    
    **الوحدة الأولى: الطاقة الحرارية وتغيرات المادة**
    - التغيرات الفيزيائية (الذوبان)
    - التغيرات الكيميائية (التفاعلات)
    
    **الوحدة الثانية: الكيمياء الكهروكيميائية**
    - الخلايا الجلفانية
    - الخلايا التحليلية
    - التآكل والحماية
    """)

elif page == "📖 الوحدة الأولى":
    st.title("📖 الوحدة الأولى: التغيرات الحرارية")
    st.markdown("---")
    
    # Navigation
    cols = st.columns(7)
    for i in range(min(7, len(unit1_slides))):
        if cols[i].button(f"{i+1}", key=f"u1_{i}"):
            st.session_state.current_slide = i
            st.rerun()
    
    if len(unit1_slides) > 7:
        cols2 = st.columns(len(unit1_slides) - 7)
        for i in range(len(unit1_slides) - 7):
            idx = i + 7
            if cols2[i].button(f"{idx+1}", key=f"u1_{idx}"):
                st.session_state.current_slide = idx
                st.rerun()
    
    current = unit1_slides[st.session_state.current_slide]
    st.markdown(f"<p class='progress-text'>الشريحة {st.session_state.current_slide + 1} من {len(unit1_slides)}</p>", unsafe_allow_html=True)
    st.progress((st.session_state.current_slide + 1) / len(unit1_slides))
    st.markdown(f"<h2 style='text-align: center; color: #667eea;'>{current['title']}</h2>", unsafe_allow_html=True)
    st.markdown(current['content'], unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.session_state.current_slide < len(unit1_slides) - 1:
            if st.button("التالي ⬅️"):
                st.session_state.current_slide += 1
                st.rerun()
    with col3:
        if st.session_state.current_slide > 0:
            if st.button("➡️ السابق"):
                st.session_state.current_slide -= 1
                st.rerun()

elif page == "📖 الوحدة الثانية":
    st.title("📖 الوحدة الثانية: الكيمياء الكهروكيميائية")
    st.markdown("---")
    
    # Navigation for unit 2
    if 'current_slide_u2' not in st.session_state:
        st.session_state.current_slide_u2 = 0
    
    cols = st.columns(min(6, len(unit2_slides)))
    for i in range(min(6, len(unit2_slides))):
        if cols[i].button(f"{i+1}", key=f"u2_{i}"):
            st.session_state.current_slide_u2 = i
            st.rerun()
    
    if len(unit2_slides) > 6:
        cols2 = st.columns(len(unit2_slides) - 6)
        for i in range(len(unit2_slides) - 6):
            idx = i + 6
            if cols2[i].button(f"{idx+1}", key=f"u2_{idx}"):
                st.session_state.current_slide_u2 = idx
                st.rerun()
    
    current = unit2_slides[st.session_state.current_slide_u2]
    st.markdown(f"<p class='progress-text'>الشريحة {st.session_state.current_slide_u2 + 1} من {len(unit2_slides)}</p>", unsafe_allow_html=True)
    st.progress((st.session_state.current_slide_u2 + 1) / len(unit2_slides))
    st.markdown(f"<h2 style='text-align: center; color: #ff6b6b;'>{current['title']}</h2>", unsafe_allow_html=True)
    st.markdown(current['content'], unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.session_state.current_slide_u2 < len(unit2_slides) - 1:
            if st.button("التالي ⬅️"):
                st.session_state.current_slide_u2 += 1
                st.rerun()
    with col3:
        if st.session_state.current_slide_u2 > 0:
            if st.button("➡️ السابق"):
                st.session_state.current_slide_u2 -= 1
                st.rerun()

elif page == "❓ اختبار MCQ":
    st.title("❓ اختبار الأسئلة متعددة الخيارات")
    st.markdown("---")
    
    if not st.session_state.quiz_started:
        st.markdown("<h3>⚙️ إعدادات الاختبار</h3>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            num_q = st.slider("عدد الأسئلة:", 5, min(100, len(all_questions)), 20)
        with col2:
            unit_filter = st.selectbox("اختر الوحدة:", ["الكل", "الوحدة الأولى فقط", "الوحدة الثانية فقط"])
        
        st.info("ℹ️ الأسئلة تظهر بنفس الترتيب دائماً للمذاكرة الجماعية")
        
        if st.button("🚀 بدء الاختبار"):
            filtered = all_questions.copy()
            if unit_filter == "الوحدة الأولى فقط":
                filtered = [q for q in filtered if q.get('unit', 1) == 1]
            elif unit_filter == "الوحدة الثانية فقط":
                filtered = [q for q in filtered if q.get('unit', 1) == 2]
            
            # Sequential order (not random) for group study
            n = min(num_q, len(filtered))
            st.session_state.selected_questions = filtered[:n]  # Take first n questions in order
            st.session_state.quiz_started = True
            st.session_state.current_question = 0
            st.session_state.correct_count = 0
            st.session_state.wrong_count = 0
            st.session_state.show_answer = False
            st.rerun()
    else:
        current_q = st.session_state.selected_questions[st.session_state.current_question]
        q_num = st.session_state.current_question + 1
        total_q = len(st.session_state.selected_questions)
        
        # Show unit indicator
        unit_color = "#667eea" if current_q.get('unit', 1) == 1 else "#ff6b6b"
        unit_name = "الوحدة الأولى" if current_q.get('unit', 1) == 1 else "الوحدة الثانية"
        st.markdown(f"<div style='text-align: center; color: {unit_color}; font-weight: bold;'>{unit_name}</div>", unsafe_allow_html=True)
        
        st.progress(q_num / total_q)
        st.markdown(f"<p class='progress-text'>السؤال {q_num} من {total_q}</p>", unsafe_allow_html=True)
        
        lesson_class = f"lesson-{current_q.get('lesson', 1)}"
        st.markdown(f"<div class='question-card {lesson_class}'><h3>❓ {current_q['q']}</h3></div>", unsafe_allow_html=True)
        
        if not st.session_state.show_answer:
            for i, opt in enumerate(current_q['options']):
                if st.button(f"{i+1}. {opt}", key=f"opt_{i}"):
                    st.session_state.user_answer = i
                    st.session_state.show_answer = True
                    if i == current_q['correct']:
                        st.session_state.correct_count += 1
                    else:
                        st.session_state.wrong_count += 1
                    st.rerun()
        else:
            user_ans = st.session_state.user_answer
            correct_ans = current_q['correct']
            
            if user_ans == correct_ans:
                st.markdown(f"<div class='correct-answer'>✅ إجابة صحيحة!<br>الإجابة: {current_q['options'][correct_ans]}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='wrong-answer'>❌ إجابة خاطئة!<br>إجابتك: {current_q['options'][user_ans]}<br>الصحيحة: {current_q['options'][correct_ans]}</div>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col1:
                if q_num < total_q:
                    if st.button("التالي ⬅️"):
                        st.session_state.current_question += 1
                        st.session_state.show_answer = False
                        st.rerun()
                else:
                    if st.button("🏁 إنهاء"):
                        st.session_state.quiz_started = False
                        st.rerun()
            with col3:
                if q_num > 1:
                    if st.button("➡️ السابق"):
                        st.session_state.current_question -= 1
                        st.session_state.show_answer = False
                        st.rerun()
        
        st.markdown("---")
        c1, c2, c3 = st.columns(3)
        c1.metric("✅ صحيحة", st.session_state.correct_count)
        c2.metric("❌ خاطئة", st.session_state.wrong_count)
        total = st.session_state.correct_count + st.session_state.wrong_count
        pct = (st.session_state.correct_count / total * 100) if total > 0 else 0
        c3.metric("📊 النسبة", f"{pct:.0f}%")

elif page == "📊 إحصائيات":
    st.title("📊 إحصائيات التعلم")
    st.markdown("---")
    
    unit1_count = len([q for q in all_questions if q.get('unit', 1) == 1])
    unit2_count = len([q for q in all_questions if q.get('unit', 1) == 2])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='stat-card'><h2>📚</h2><h3>{len(all_questions)}</h3><p>إجمالي الأسئلة</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='stat-card'><h2>📘</h2><h3>{unit1_count}</h3><p>الوحدة الأولى</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='stat-card'><h2>📗</h2><h3>{unit2_count}</h3><p>الوحدة الثانية</p></div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<h3>📈 تقدمك في الاختبارات</h3>", unsafe_allow_html=True)
    
    total_answered = st.session_state.correct_count + st.session_state.wrong_count
    if total_answered > 0:
        c1, c2 = st.columns(2)
        c1.metric("✅ صحيحة", st.session_state.correct_count)
        c2.metric("❌ خاطئة", st.session_state.wrong_count)
        
        try:
            import plotly.graph_objects as go
            fig = go.Figure(data=[go.Pie(
                labels=['صحيحة', 'خاطئة'],
                values=[st.session_state.correct_count, st.session_state.wrong_count],
                marker_colors=['#28a745', '#dc3545'],
                textinfo='percent+label'
            )])
            fig.update_layout(title_text='نسبة الإجابات', title_x=0.5)
            st.plotly_chart(fig, use_container_width=True)
        except:
            pass
    else:
        st.info("📝 لم تقم بأي اختبارات بعد")
    
    st.markdown("---")
    if st.button("🔄 إعادة تعيين الإحصائيات"):
        st.session_state.correct_count = 0
        st.session_state.wrong_count = 0
        st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("📝 **تطبيق مينا للمذاكرة**<br>تعلم الكيمياء بطريقة تفاعلية!<br><br>✅ الأسئلة بنفس الترتيب دائماً للمذاكرة الجماعية", unsafe_allow_html=True)
