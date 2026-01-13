from IPython.display import HTML

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
    body { font-family: 'Arial', sans-serif; background: #eef2f3; display: flex; justify-content: center; padding: 20px; }
    .lab-box { width: 850px; background: white; border-radius: 15px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
    
    .screen { 
        height: 380px; background: white; border-radius: 10px; position: relative; 
        overflow: hidden; border: 2px solid #ddd; display: flex; justify-content: center; align-items: flex-end;
    }

    /* Орталық пробирка */
    .center-tube { 
        width: 60px; height: 180px; border: 4px solid #333; border-radius: 0 0 30px 30px; 
        position: relative; z-index: 5; margin-bottom: 30px; background: rgba(255,255,255,0.1);
    }
    .main-liquid { position: absolute; bottom: 0; width: 100%; height: 0%; transition: 2s; border-radius: 0 0 25px 25px; }

    /* Жылжымалы пробиркалар */
    .tube-container { 
        position: absolute; bottom: 40px; width: 45px; height: 150px; 
        transition: all 1.2s cubic-bezier(0.45, 0.05, 0.55, 0.95); z-index: 10;
    }
    .glass-body { 
        width: 100%; height: 100%; border: 3px solid #444; border-radius: 0 0 22px 22px; 
        position: relative; background: rgba(255,255,255,0.3); overflow: hidden;
    }
    .fluid { position: absolute; bottom: 0; width: 100%; height: 70%; transition: 1s; }

    /* Молекулалар шарлары */
    .molecule { position: absolute; width: 7px; height: 7px; border-radius: 50%; animation: move 3s infinite alternate; }
    @keyframes move { from { transform: translate(0,0); } to { transform: translate(6px, -12px); } }

    /* Құю анимациясы: Центрге бағыттау */
    #t_left { left: 15%; }
    #t_right { right: 15%; }

    .pour-l { left: 38% !important; bottom: 180px !important; transform: rotate(-45deg); }
    .pour-r { right: 38% !important; bottom: 180px !important; transform: rotate(45deg); }

    /* Интерфейс */
    .ui { display: grid; grid-template-columns: 1fr 1.2fr 1fr; gap: 15px; margin-top: 20px; background: #f8f9fa; padding: 20px; border-radius: 10px; }
    .btn-start { grid-column: span 3; padding: 12px; background: #27ae60; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; }
    .btn-start:hover { background: #219150; }
    label { font-size: 13px; display: block; margin-bottom: 3px; }
</style>
</head>
<body>

<div class="lab-box">
    <h3 style="text-align:center;">🔬 Молекулалық деңгейдегі 5-реагентті лаборатория</h3>
    
    <div class="screen">
        <div id="t_left" class="tube-container"><div class="glass-body"><div id="f_left" class="fluid"></div><div id="m_left"></div></div></div>
        <div class="center-tube"><div id="f_main" class="main-liquid"></div><div id="m_main"></div></div>
        <div id="t_right" class="tube-container"><div class="glass-body"><div id="f_right" class="fluid"></div><div id="m_right"></div></div></div>
    </div>

    <div class="ui">
        <div>
            <b>1. Тапсырма:</b><br>
            <select id="task" onchange="setupLab()" style="width:100%"><option value="alkane">Метанды хлорлау</option><option value="alkene">Этилен + KMnO4</option><option value="silver">Күміс айна</option></select>
        </div>
        <div>
            <b>2. Реагенттер (тек қажеттісі):</b><br>
            <div id="reagents_area"></div>
        </div>
        <div>
            <b>3. Жағдай:</b><br>
            <select id="cond" style="width:100%"><option value="std">стандартты</option><option value="hv">hv (жарық)</option><option value="t">t (қыздыру)</option></select>
        </div>
        <button class="btn-start" onclick="run()">РЕАКЦИЯНЫ БАСТАУ</button>
    </div>
    <div id="log" style="text-align:center; margin-top:10px; font-weight:bold; height: 20px;"></div>
</div>

<script>
const data = {
    alkane: { r: ["CH4", "Cl2", "NaOH", "H2O", "KMnO4"], corr: ["CH4", "Cl2"], c: "hv", c1: "#fff", c2: "#fff176", res: "#f8f9fa", info: "Метан хлорланды!" },
    alkene: { r: ["C2H4", "KMnO4", "H2O", "C2H6", "HCl"], corr: ["C2H4", "KMnO4", "H2O"], c: "std", c1: "#fff", c2: "#9c27b0", res: "#5d4037", info: "Этилен тотығып, диол түзілді!" },
    silver: { r: ["R-CHO", "Ag2O", "NH3", "NaOH", "CH3OH"], corr: ["R-CHO", "Ag2O", "NH3"], c: "t", c1: "#f1f1f1", c2: "#cfd8dc", res: "#bdc3c7", info: "Күміс айна түзілді!" }
};

function createMols(id, color, n) {
    const el = document.getElementById(id); el.innerHTML = '';
    for(let i=0; i<n; i++) {
        let m = document.createElement('div'); m.className = 'molecule';
        m.style.background = color; m.style.left = Math.random()*25+5+'px'; m.style.bottom = Math.random()*80+10+'px';
        el.appendChild(m);
    }
}

function setupLab() {
    const v = document.getElementById('task').value;
    const d = data[v];
    const area = document.getElementById('reagents_area'); area.innerHTML = '';
    d.r.forEach(n => { area.innerHTML += `<label><input type="checkbox" class="r-chk" value="${n}"> ${n}</label>`; });
    document.getElementById('f_left').style.background = d.c1;
    document.getElementById('f_right').style.background = d.c2;
    document.getElementById('f_main').style.height = '0%';
    document.getElementById('t_left').className = 'tube-container';
    document.getElementById('t_right').className = 'tube-container';
    document.getElementById('log').innerText = '';
    createMols('m_left', '#3498db', 8); createMols('m_right', '#f1c40f', 8);
    document.getElementById('m_main').innerHTML = '';
}

function run() {
    const v = document.getElementById('task').value;
    const d = data[v];
    const sel = Array.from(document.querySelectorAll('.r-chk:checked')).map(x => x.value);
    const cond = document.getElementById('cond').value;
    const isOk = sel.length === d.corr.length && d.corr.every(x => sel.includes(x)) && cond === d.c;

    if(isOk) {
        document.getElementById('t_left').classList.add('pour-l');
        document.getElementById('t_right').classList.add('pour-r');
        document.getElementById('log').innerText = "⏳ Молекулалар әрекеттесуде...";
        setTimeout(() => {
            const f = document.getElementById('f_main');
            f.style.height = '85%'; f.style.background = d.res;
            if(v==='silver') f.style.boxShadow = "inset 0 0 25px white";
            createMols('m_main', '#2c3e50', 12);
            document.getElementById('log').innerHTML = "<span style='color:green'>✅ " + d.info + "</span>";
        }, 1300);
    } else {
        document.getElementById('log').innerHTML = "<span style='color:red'>❌ Реагент немесе жағдай қате!</span>";
    }
}
setupLab();
</script>
</body>
</html>
"""
HTML(html_code)
