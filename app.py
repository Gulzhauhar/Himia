import streamlit as st
import time

# 1. Беттің баптаулары
st.set_page_config(page_title="Advanced Organic Chemistry Lab", layout="wide")

# 2. Стильдер (Анимация және пробирка визуалдау үшін)
st.markdown("""
<style>
    .test-tube {
        width: 60px;
        height: 180px;
        border: 3px solid #ccc;
        border-radius: 0 0 30px 30px;
        margin: 0 auto;
        position: relative;
        background: rgba(255, 255, 255, 0.1);
        overflow: hidden;
    }
    .liquid {
        position: absolute;
        bottom: 0;
        width: 100%;
        transition: all 2s ease;
    }
    .bubbles {
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 100%;
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# 3. Реакциялар базасы (Нақтыланған теңдеулер)
labs = {
    "Этиленнің бромдалуы (Қанықпағандық)": {
        "reagents": ["C2H4", "Br2"],
        "equation": r"CH_2=CH_2 + Br_2 \rightarrow CH_2Br-CH_2Br",
        "start_color": "#FF8C00",  # Қызғылт-сары
        "end_color": "rgba(255, 255, 255, 0.5)",  # Түссіз
        "desc": "Бром суы түссізденеді.",
        "bubbles": True
    },
    "Күміс айна реакциясы (Альдегид)": {
        "reagents": ["CH3CHO", "AgNO3", "NH3"],
        "equation": r"CH_3CHO + 2[Ag(NH_3)_2]OH \xrightarrow{t} CH_3COONH_4 + 2Ag \downarrow + 3NH_3 + H_2O",
        "start_color": "#E0E0E0", 
        "end_color": "#C0C0C0",  # Күміс түс
        "desc": "Пробирка қабырғасында жылтыр күміс тұнбасы түзіледі.",
        "bubbles": False
    },
    "Глюкозаның Cu(OH)2-мен тотығуы": {
        "reagents": ["C6H12O6", "Cu(OH)2"],
        "equation": r"C_6H_{12}O_6 + 2Cu(OH)_2 \xrightarrow{t} C_6H_{12}O_7 + Cu_2O \downarrow + 2H_2O",
        "start_color": "#0000FF", # Көк
        "end_color": "#B22222", # Кірпіш-қызыл
        "desc": "Көгілдір тұнба қыздырғанда кірпіш-қызыл түске өзгереді.",
        "bubbles": False
    },
    "Биурет реакциясы (Ақуыз)": {
        "reagents": ["Protein", "CuSO4", "NaOH"],
        "equation": r"\text{Пептидтік байланыс} + Cu^{2+} \xrightarrow{NaOH} \text{Күлгін кешенді қосылыс}",
        "start_color": "#ADD8E6", 
        "end_color": "#8A2BE2", # Күлгін
        "desc": "Ерітінді ашық күлгін түске боялады.",
        "bubbles": False
    }
}

# 4. Интерфейс
st.title("🧪 Органикалық химия: Анимациялық лаборатория")
st.sidebar.header("Тәжірибені таңдаңыз")
choice = st.sidebar.selectbox("Зертханалық жұмыс:", list(labs.keys()))

col1, col2 = st.columns([1, 1])

with col1:
    st.header("🔬 Лабораториялық үстел")
    st.latex(labs[choice]["equation"])
    
    # Визуалды пробирка (Анимация алдындағы күйі)
    liquid_html = st.empty()
    
    if st.button("🧪 Реакцияны бастау"):
        # Анимация қадамдары
        for i in range(11):
            color = labs[choice]["start_color"] if i < 3 else labs[choice]["end_color"]
            height = 30 + i * 5
            bubble_display = "block" if labs[choice]["bubbles"] and i > 5 else "none"
            
            liquid_html.markdown(f"""
                <div class="test-tube">
                    <div class="liquid" style="background-color: {color}; height: {height}%;"></div>
                    <div class="bubbles" style="display: {bubble_display};">🫧🫧🫧</div>
                </div>
                """, unsafe_allow_html=True)
            time.sleep(0.3)
        
        st.success(f"Нәтиже: {labs[choice]['desc']}")
        st.snow() if "түссіз" in labs[choice]['desc'] else st.balloons()
    else:
        # Бастапқы күйі
        liquid_html.markdown(f"""
            <div class="test-tube">
                <div class="liquid" style="background-color: {labs[choice]['start_color']}; height: 30%;"></div>
            </div>
            """, unsafe_allow_html=True)

with col2:
    st.header("📝 Бақылау парағы")
    st.write(f"**Қолданылатын заттар:** {', '.join(labs[choice]['reagents'])}")
    
    st.info("Тапсырма: Реакция теңдеуіндегі коэффициенттерді тексеріп, дәптеріңізге жазыңыз.")
    
    # Оқушы жауабын тексеру бөлімі
    st.subheader("🤖 Тексеруші")
    answer = st.text_input("Бұл реакцияның белгісі қандай?")
    if st.button("Жауапты тексеру"):
        if any(word in answer.lower() for word in ["тұнба", "түс", "газ", "күміс"]):
            st.success("Дұрыс! Сіз реакцияның негізгі белгісін таныдыңыз.")
        else:
            st.warning("Оқулықты қайта қараңыз. Реакция өніміне назар аударыңыз.")

st.markdown("---")
st.caption("© 2026 Virtual Chemistry Simulator - Оқушылар мен мұғалімдерге арналған.")
