import streamlit as st
import time

# Беттің баптаулары
st.set_page_config(page_title="Органикалық химия зертханасы", layout="wide")

# CSS стильдері (Пробирка мен эффектілер үшін)
st.markdown("""
    <style>
    .test-tube {
        height: 250px;
        width: 60px;
        border: 3px solid #ccc;
        border-radius: 0 0 30px 30px;
        margin: auto;
        position: relative;
        background: rgba(255, 255, 255, 0.1);
        overflow: hidden;
    }
    .liquid {
        position: absolute;
        bottom: 0;
        width: 100%;
        transition: all 1s ease;
    }
    .bubble {
        position: absolute;
        bottom: 10%;
        left: 50%;
        width: 10px;
        height: 10px;
        background: rgba(255, 255, 255, 0.5);
        border-radius: 50%;
        animation: rise 2s infinite;
    }
    @keyframes rise {
        0% { bottom: 10%; opacity: 1; }
        100% { bottom: 90%; opacity: 0; }
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔬 Органикалық химия: Виртуалды зертхана")
st.write("Реактивтерді таңдап, зертханалық жұмысты орындаңыз.")

# Зертханалық жұмыстар тізімі
lab_works = {
    "Альдегидтерді анықтау": {
        "reagent_a": "Формальдегид",
        "reagent_b": "AgNO3 + NH4OH (Күміс оксидінің аммиактағы ерітіндісі)",
        "result_text": "Пробирка қабырғасында жылтыр күміс қабаты түзілді.",
        "color": "#C0C0C0", # Күміс түс
        "gas": False,
        "precipitate": "Металл күміс (тұнба)",
        "equation": "$$R-CHO + 2[Ag(NH_3)_2]OH \\xrightarrow{t} R-COONH_4 + 2Ag↓ + 3NH_3 + H_2O$$"
    },
    "Қанықпаған көмірсутектер (Этилен)": {
        "reagent_a": "Этилен (C2H4)",
        "reagent_b": "Бром суы (Br2 ерітіндісі)",
        "result_text": "Бром суының сары-қоңыр түсі жойылды.",
        "color": "rgba(255, 255, 255, 0.2)", # Түссіз
        "gas": True,
        "precipitate": "Жоқ",
        "equation": "$$CH_2=CH_2 + Br_2 \\rightarrow CH_2Br-CH_2Br$$"
    },
    "Ақуызды анықтау (Биурет реакциясы)": {
        "reagent_a": "Жұмыртқа ақуызы",
        "reagent_b": "NaOH + CuSO4",
        "result_text": "Ерітінді ашық күлгін түске боялды.",
        "color": "#8A2BE2", # Күлгін
        "gas": False,
        "precipitate": "Жоқ (Кешенді қосылыс)",
        "equation": "Ақуыз + Cu^{2+} \\xrightarrow{OH^-} \\text{Күлгін кешенді қосылыс}"
    }
}

# Сол жақ панель - Басқару
st.sidebar.header("🛠 Зертханалық үстел")
choice = st.sidebar.selectbox("Зертханалық жұмысты таңдаңыз:", list(lab_works.keys()))
start_btn = st.sidebar.button("Реакцияны бастау")

# Орталық бөлім - Эксперимент
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📋 Жұмыс барысы")
    work = lab_works[choice]
    st.write(f"**1-ші зат:** {work['reagent_a']}")
    st.write(f"**2-ші зат:** {work['reagent_b']}")
    
    if start_btn:
        st.info("Процесс: Реактивтер араластырылуда...")
        time.sleep(2)
        st.success("Нәтиже дайын!")
        st.write(f"**Бақылау:** {work['result_text']}")
        st.write(f"**Тұнба:** {work['precipitate']}")
        st.write("**Химиялық теңдеуі:**")
        st.write(work['equation'])

with col2:
    st.subheader("🧪 Пробирка")
    
    # Реакцияға дейінгі және кейінгі визуалдау
    fill_height = "60%" if start_btn else "0%"
    liquid_color = work['color'] if start_btn else "#E0E0E0"
    
    # Пробирканың HTML/CSS кодын шығару
    gas_html = '<div class="bubble"></div><div class="bubble" style="left:30%; animation-delay:0.5s"></div>' if (start_btn and work['gas']) else ""
    
    st.markdown(f"""
        <div class="test-tube">
            <div class="liquid" style="height: {fill_height}; background-color: {liquid_color};">
                {gas_html}
            </div>
        </div>
        <p style="text-align:center; margin-top:10px;">{'Реакциядан кейін' if start_btn else 'Бос пробирка'}</p>
    """, unsafe_allow_html=True)

# Тапсырмалар бөлімі
st.divider()
st.subheader("📝 Бекіту тапсырмалары")
q1 = st.radio("1. Бром суының түссізденуі ненің белгісі?", ["Қаныққан байланыс", "Қос байланыс (қанықпаған)", "Оттегінің бөлінуі"])
if st.button("Тексеру"):
    if q1 == "Қос байланыс (қанықпаған)":
        st.balloons()
        st.success("Дұрыс!")
    else:
        st.error("Қайта ойланып көріңіз.")
