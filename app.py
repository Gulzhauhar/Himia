import streamlit as st
import time

# Беттің негізгі баптаулары
st.set_page_config(page_title="Alkanes Lab Simulator", layout="wide")

# Деректер базасы
alkane_experiments = {
    "Метанның жануы": {
        "steps": ["Газды жағу", "Пробирканы төңкеру", "Әк суын қосу"],
        "visual": "🔥 Көгілдір жалынмен жанады. Әк суы лайланады.",
        "observation": "Көмірқышқыл газы мен су түзіледі.",
        "equation": "$CH_4 + 2O_2 \\rightarrow CO_2 + 2H_2O$",
        "color": "#FF4B4B"
    },
    "Метанның хлорлануы (Орынбасу)": {
        "steps": ["Метан мен хлорды араластыру", "Ультракүлгін сәуле түсіру", "Индикатор қағазын жақындату"],
        "visual": "🟡 Хлордың сары түсі жоғалып, пробирка қабырғасында тамшылар пайда болады.",
        "observation": "Индикатор қағазы қызарады (HCl түзілуі).",
        "equation": "$CH_4 + Cl_2 \\xrightarrow{hv} CH_3Cl + HCl$",
        "color": "#F0E68C"
    },
    "Алкандардың қышқылдарға қатынасы": {
        "steps": ["Парафин (қатты алкан) салу", "Концентрлі күкірт қышқылын қосу", "Қыздыру"],
        "visual": "⚪ Ешқандай өзгеріс байқалмайды.",
        "observation": "Алкандар химиялық белсенділігі төмен қосылыстар (парафиндер).",
        "equation": "$C_nH_{2n+2} + H_2SO_4 \\rightarrow \\text{реакция жүрмейді}$",
        "color": "#D3D3D3"
    }
}

st.title("🧪 Алкандардың химиялық қасиеттері: Виртуалды зертхана")
st.markdown("---")

# Сол жақ мәзір
st.sidebar.header("🔬 Тәжірибені таңдау")
lab_selection = st.sidebar.selectbox("Зертханалық жұмыс:", list(alkane_experiments.keys()))

col1, col2 = st.columns([1, 1])

with col1:
    st.header("🧪 Тәжірибе алаңы")
    st.info(f"Тапсырма: {lab_selection}")
    
    # Реакция барысын көрсету
    for i, step in enumerate(alkane_experiments[lab_selection]["steps"]):
        st.write(f"{i+1}. {step}")

    if st.button("🚀 Реакцияны бастау"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
            status_text.text(f"Пробиркадағы процесс: {percent_complete + 1}%")
        
        st.subheader("👀 Бақылау:")
        st.markdown(f"**{alkane_experiments[lab_selection]['visual']}**")
        
        # Визуалды пробирка моделі (CSS арқылы)
        tube_color = alkane_experiments[lab_selection]["color"]
        st.markdown(f"""
            <div style="border: 4px solid #555; border-radius: 0 0 50px 50px; 
            width: 80px; height: 200px; background-color: {tube_color}; 
            margin: 20px auto; position: relative; box-shadow: inset 0 0 20px rgba(0,0,0,0.2);">
                <div style="position: absolute; bottom: 10px; width: 100%; text-align: center; font-size: 10px;">Пробирка</div>
            </div>
            """, unsafe_allow_html=True)

with col2:
    st.header("📊 Қорытынды")
    st.warning(f"**Нәтиже:** {alkane_experiments[lab_selection]['observation']}")
    
    st.markdown("### Химиялық теңдеу:")
    st.latex(alkane_experiments[lab_selection]["equation"])
    
    st.markdown("---")
    st.write("**Сұрақ:** Неліктен алкандарды 'парафиндер' деп атайды?")
    user_answer = st.text_input("Жауабыңызды жазыңыз:")
    if st.button("Тексеру"):
        if "белсенділігі төмен" in user_answer.lower() or "аз" in user_answer.lower():
            st.success("Дұрыс! Олар химиялық тұрғыдан өте енжар.")
        else:
            st.info("Кеңес: Латынша 'parum affinis' сөзінің мағынасын ойлаңыз.")

st.sidebar.markdown("---")
st.sidebar.write("**Нұсқаулық:**")
st.sidebar.caption("1. Тәжірибені таңдаңыз. \n2. 'Реакцияны бастау' батырмасын басыңыз. \n3. Пробиркадағы өзгерісті бақылаңыз.")
