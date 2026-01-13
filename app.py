import streamlit as st
import time

# 1. Бет баптаулары
st.set_page_config(page_title="AI Virtual Lab", layout="wide")

# Пробирка анимациясы үшін CSS стильдері
st.markdown("""
<style>
    .test-tube-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px;
    }
    .test-tube {
        width: 70px;
        height: 200px;
        border: 4px solid #f0f0f0;
        border-radius: 0 0 40px 40px;
        position: relative;
        background: rgba(255, 255, 255, 0.1);
        overflow: hidden;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .liquid {
        position: absolute;
        bottom: 0;
        width: 100%;
        transition: all 1.5s ease-in-out;
    }
</style>
""", unsafe_allow_html=True)

# 2. Мәліметтер қоры (Нақты химиялық теңдеулермен)
lab_data = {
    "Этиленді бромдау": {
        "reagents": ["C2H4", "Br2"],
        "condition": "стандартты",
        "effect": "Қызғылт-сары түсті бром суы түссізденді.",
        "equation": r"CH_2=CH_2 + Br_2 \rightarrow CH_2Br-CH_2Br",
        "start_color": "#FF8C00", # Orange
        "end_color": "rgba(255, 255, 255, 0.4)", # Colorless
        "show_bubbles": True
    },
    "Күміс айна реакциясы": {
        "reagents": ["CH3CHO", "AgNO3", "NH3"],
        "condition": "t (қыздыру)",
        "effect": "Пробирка қабырғасында жылтыр күміс қабаты пайда болды.",
        "equation": r"CH_3CHO + 2[Ag(NH_3)_2]OH \xrightarrow{t} CH_3COONH_4 + 2Ag \downarrow + 3NH_3 + H_2O",
        "start_color": "#D3D3D3", # Gray
        "end_color": "#C0C0C0", # Silver
        "show_bubbles": False
    },
    "Глюкозаны анықтау": {
        "reagents": ["C6H12O6", "Cu(OH)2"],
        "condition": "t (қыздыру)",
        "effect": "Көгілдір тұнба кірпіш-қызыл түске ауысты.",
        "equation": r"C_6H_{12}O_6 + 2Cu(OH)_2 \xrightarrow{t} C_6H_{12}O_7 + Cu_2O \downarrow + 2H_2O",
        "start_color": "#0000FF", # Blue
        "end_color": "#B22222", # Brick red
        "show_bubbles": False
    },
    "Биурет реакциясы": {
        "reagents": ["Protein", "CuSO4", "NaOH"],
        "condition": "сілтілі",
        "effect": "Ерітінді ашық күлгін түске боялды.",
        "equation": r"\text{Белок} + Cu^{2+} \xrightarrow{NaOH} \text{Күлгін кешенді қосылыс}",
        "start_color": "#E0FFFF", # Light Cyan
        "end_color": "#8A2BE2", # Violet
        "show_bubbles": False
    }
}

# 3. Интерфейс
st.title("🧪 10-сынып Органикалық химия: Виртуалды лаборатория")
selected_lab = st.sidebar.selectbox("Зертханалық жұмысты таңдаңыз:", list(lab_data.keys()))

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🔬 Эксперимент алаңы")
    data = lab_data[selected_lab]
    
    # Реагенттерді таңдау
    all_reagents = ["C2H4", "Br2", "CH3CHO", "AgNO3", "NH3", "C6H12O6", "Cu(OH)2", "Protein", "CuSO4", "NaOH"]
    user_reagents = st.multiselect("Реагенттерді қосыңыз:", all_reagents)
    user_cond = st.radio("Жағдайды таңдаңыз:", ["стандартты", "t (қыздыру)", "сілтілі"])

    # Пробирка орны
    tube_placeholder = st.empty()
    
    # Бастапқы күйі
    tube_placeholder.markdown(f"""
        <div class="test-tube-container">
            <div class="test-tube">
                <div class="liquid" style="background-color: {data['start_color']}; height: 40%;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    if st.button("🧪 Реакцияны іске қосу"):
        check_reagents = all(r in user_reagents for r in data["reagents"])
        
        if check_reagents and user_cond == data["condition"]:
            # Анимация
            for i in range(1, 11):
                height = 40 + i * 2
                tube_placeholder.markdown(f"""
                <div class="test-tube-container">
                    <div class="test-tube">
                        <div class="liquid" style="background-color: {data['end_color']}; height: {height}%;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                time.sleep(0.2)
            
            st.success(f"Нәтиже: {data['effect']}")
            if selected_lab == "Этиленді бромдау": st.snow() 
            else: st.balloons()
        else:
            st.error("❌ Реакция жүрмеді. Реагенттерді немесе жағдайды (t, сілті) тексеріңіз.")

with col2:
    st.subheader("📝 Химиялық теңдеу")
    st.latex(data["equation"])
    
    st.markdown("---")
    st.write("**Сұрақ:** Бұл реакцияның сапалық белгісі қандай?")
    answer = st.text_input("Жауабыңызды жазыңыз:")
    if st.button("Тексеру"):
        if any(word in answer.lower() for word in ["түс", "тұнба", "күміс", "қызыл"]):
            st.success("Дұрыс! Сіз реакцияның мәнін түсіндіңіз.")
        else:
            st.warning("Қайта ойланып көріңіз.")
