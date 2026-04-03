# ===============================
# BIBLIOTECAS EXTERNAS
# ===============================

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import Fullscreen

# ===============================
# MÓDULOS DO PROJETO
# ===============================

from hidrogenio import (
    mostrar_caracteristicas_hidrogenio,
    mostrar_confusoes_hidrogenio,
    quiz_hidrogenio,
    checklist_hidrogenio,
    mapa_hidrogenio,
    referencias_hidrogenio
)

from petroleo_gas import (
    mostrar_caracteristicas_petroleo,
    mostrar_confusoes_petroleo,
    quiz_petroleo,
    checklist_petroleo,
    mapa_petroleo,
    referencias_petroleo
)

from metano import (
    mostrar_caracteristicas_metano,
    mostrar_confusoes_metano,
    quiz_metano,
    checklist_metano,
    mapa_metano,
    referencias_metano
)

from litio import (
    mostrar_caracteristicas_litio,
    mostrar_confusoes_litio,
    quiz_litio,
    checklist_litio,
    mapa_litio,
    referencias_litio
)

from uranio import (
    mostrar_caracteristicas_uranio,
    mostrar_confusoes_uranio,
    quiz_uranio,
    checklist_uranio,
    mapa_uranio,
    referencias_uranio
)

from torio import (
    mostrar_caracteristicas_torio,
    mostrar_confusoes_torio,
    quiz_torio,
    checklist_torio,
    mapa_torio,
    referencias_torio
)

from sms_cobalto import (
    mostrar_caracteristicas_sms,
    mostrar_confusoes_sms,
    quiz_sms,
    checklist_sms,
    mapa_sms,
    referencias_sms
)

from quartzo import (
    mostrar_caracteristicas_quartzo,
    mostrar_confusoes_quartzo,
    quiz_quartzo,
    checklist_quartzo,
    mapa_quartzo,
    referencias_quartzo
)

from monazite import (
    mostrar_caracteristicas_monazite,
    mostrar_confusoes_monazite,
    quiz_monazite,
    checklist_monazite,
    mapa_monazite,
    referencias_monazite
)

from ortoclase import (
    mostrar_caracteristicas_ortoclase,
    mostrar_confusoes_ortoclase,
    quiz_ortoclase,
    checklist_ortoclase,
    mapa_ortoclase,
    referencias_ortoclase
)

# ===============================
# 1. CONFIGURAÇÕES
# ===============================

st.set_page_config(
    page_title="Explorador de Recursos Energéticos",
    layout="wide",
    page_icon= "Logótipo.png"
)

# ===============================
# 2. BASE DE DADOS
# ===============================

materias_primas = [
    "Hidrogénio (Geração natural e armazenamento)",
    "Petróleo e Gás (Sistemas convencionais)",
    "Metano (Hidratos e recursos não convencionais)",
    "Lítio (Rocha dura versus salmouras)",
    "Urânio (Combustíveis nucleares)",
    "Tório (Combustíveis nucleares)",
    "Sulfuretos maciços do fundo oceânico (SMS) e crostas de cobalto",
    "Quartzo",
    "Monazite",
    "Ortoclase"
]

depositos = {
    "Hidrogénio (Geração natural e armazenamento)": [
        "Serpentinização",
        "Radiólise da água",
    ],
    "Petróleo e Gás (Sistemas convencionais)": [
        "Reservatório de óleo",
        "Reservatórios de gás",
        "Reservatórios de misto (óleo + gás)",

    ],
    "Metano (Hidratos e recursos não convencionais)": [
        "Biogénico",
        "Termogénico",
    ],
    "Lítio (Rocha dura versus salmouras)": [
        "Pegmatitos (rocha dura)",
        "Salmouras continentais",
        "Argilas ricas em lítio"
    ],
    "Urânio (Combustíveis nucleares)": [
        "Arenitos",
        "Discordâncias",
        "Intrusivos e Magmáticos",
        "Hidrotermal e Metassomática",
        "Superficiais e Sedimentares",
        "Brechas"
    ],
    "Tório (Combustíveis nucleares)": [
        "Depósitos tipo unconformity",
        "Depósitos em arenitos",
        "Depósitos hidrotermais"
    ],
    "Sulfuretos maciços do fundo oceânico (SMS) e crostas de cobalto": [
        "Dorsais médio-oceânicas",
        "Arcos vulcânicos submarinos",
        "Bacias de retro-arco"
    ],
    "Quartzo": [
        "Veios hidrotermais",
        "Pegmatitos",
        "Depósitos aluviais"
    ],
    "Monazite": [
        "Depósitos de Placer",
        "Depósitos ígneos",
        "Depósitos metamórficos"
    ],
    "Ortoclase": [
        "Pegmatitos graníticos",
        "Granitos",
        "Depósitos residuais"
    ]
}

# ===============================
# 3. SIDEBAR
# ===============================

with st.sidebar:

    try:
        st.image("Logótipo.png")
    except Exception:
        st.write("*(Logótipo)*")

    st.markdown("<h3 style='text-align: center;'>⚙️ Painel de Controlo</h3>", unsafe_allow_html=True)
    
    st.divider()

    recurso_selecionado = st.selectbox(
        "Selecione a Matéria-Prima:",
        materias_primas
    )

    deposito_selecionado = st.selectbox(
        "Selecione o Tipo de Depósito:",
        depositos.get(recurso_selecionado, []),
        key=f"dep_{recurso_selecionado}"
    )

    st.divider()

    st.info("💡 Utilize os separadores no ecrã principal para navegar.")

# ===============================
# 4. HEADER
# ===============================

st.markdown(f"## 🔎 Análise: {recurso_selecionado}")
st.caption(f"Tipo de depósito selecionado: **{deposito_selecionado}**")


# ===============================
# 5. TABS
# ===============================

tab_caract, tab_conf, tab_quiz, tab_check, tab_mapa, tab_ref = st.tabs([
    "📊 Características",
    "⚠️ Confusões",
    "🧠 Quiz",
    "✅ Checklist",
    "🗺️ Mapa",
    "📚 Referências"
])

# ===============================
# 6. CARACTERÍSTICAS
# ===============================

with tab_caract:

    if recurso_selecionado == "Hidrogénio (Geração natural e armazenamento)":
        mostrar_caracteristicas_hidrogenio(deposito_selecionado)
        
    elif recurso_selecionado == "Petróleo e Gás (Sistemas convencionais)":
        mostrar_caracteristicas_petroleo(deposito_selecionado)
    
    elif recurso_selecionado == "Metano (Hidratos e recursos não convencionais)":
        mostrar_caracteristicas_metano(deposito_selecionado)
    
    elif recurso_selecionado == "Lítio (Rocha dura versus salmouras)":
        mostrar_caracteristicas_litio (deposito_selecionado)
  
    elif recurso_selecionado == "Urânio (Combustíveis nucleares)":
        mostrar_caracteristicas_uranio(deposito_selecionado)
        
    elif recurso_selecionado == "Tório (Combustíveis nucleares)":
        mostrar_caracteristicas_torio(deposito_selecionado)
    
    elif recurso_selecionado == "Sulfuretos maciços do fundo oceânico (SMS) e crostas de cobalto":
        mostrar_caracteristicas_sms(deposito_selecionado)
    
    elif recurso_selecionado == "Quartzo":
        mostrar_caracteristicas_quartzo(deposito_selecionado)
    
    elif recurso_selecionado == "Monazite":
        mostrar_caracteristicas_monazite(deposito_selecionado)
    
    elif recurso_selecionado == "Ortoclase":
        mostrar_caracteristicas_ortoclase(deposito_selecionado)

    else:
        st.info("Conteúdo ainda não disponível.")

# ===============================
# 7. CONFUSÕES
# ===============================

with tab_conf:

    if recurso_selecionado == "Hidrogénio (Geração natural e armazenamento)":
        mostrar_confusoes_hidrogenio()
        
    elif recurso_selecionado == "Petróleo e Gás (Sistemas convencionais)":
        mostrar_confusoes_petroleo()
        
    elif recurso_selecionado == "Metano (Hidratos e recursos não convencionais)":
        mostrar_confusoes_metano()
        
    elif recurso_selecionado == "Lítio (Rocha dura versus salmouras)":
        mostrar_confusoes_litio()
        
    elif recurso_selecionado == "Urânio (Combustíveis nucleares)":
        mostrar_confusoes_uranio()
        
    elif recurso_selecionado == "Tório (Combustíveis nucleares)":
        mostrar_confusoes_torio()
        
    elif recurso_selecionado == "Sulfuretos maciços do fundo oceânico (SMS) e crostas de cobalto":
        mostrar_confusoes_sms(deposito_selecionado) # Adicionado aqui
        
    elif recurso_selecionado == "Quartzo":
        mostrar_confusoes_quartzo()
        
    elif recurso_selecionado == "Monazite":
        mostrar_confusoes_monazite()
        
    elif recurso_selecionado == "Ortoclase":
        mostrar_confusoes_ortoclase()

    else:
        st.info("Conteúdo ainda não disponível.")

# ===============================
# 8. QUIZ
# ===============================

with tab_quiz:

    if recurso_selecionado == "Hidrogénio (Geração natural e armazenamento)":
        quiz_hidrogenio(deposito_selecionado)

    elif recurso_selecionado == "Petróleo e Gás (Sistemas convencionais)":
        quiz_petroleo(deposito_selecionado)
        
    elif recurso_selecionado == "Metano (Hidratos e recursos não convencionais)":
        quiz_metano(deposito_selecionado)
        
    elif recurso_selecionado == "Lítio (Rocha dura versus salmouras)":
        quiz_litio(deposito_selecionado)
        
    elif recurso_selecionado == "Urânio (Combustíveis nucleares)":
        quiz_uranio(deposito_selecionado)
        
    elif recurso_selecionado == "Tório (Combustíveis nucleares)":
        quiz_torio(deposito_selecionado)
        
    elif recurso_selecionado == "Sulfuretos maciços do fundo oceânico (SMS) e crostas de cobalto":
        quiz_sms() # Removido daqui
        
    elif recurso_selecionado == "Quartzo":
        quiz_quartzo(deposito_selecionado)
        
    elif recurso_selecionado == "Monazite":
        quiz_monazite(deposito_selecionado)
        
    elif recurso_selecionado == "Ortoclase":
        quiz_ortoclase(deposito_selecionado)

    else:
        st.info("Quiz em desenvolvimento.")

# ===============================
# 9. CHECKLIST
# ===============================

with tab_check:

    if recurso_selecionado == "Hidrogénio (Geração natural e armazenamento)":
        checklist_hidrogenio()
        
    elif recurso_selecionado == "Petróleo e Gás (Sistemas convencionais)":
        checklist_petroleo()
        
    elif recurso_selecionado == "Metano (Hidratos e recursos não convencionais)":
        checklist_metano()
        
    elif recurso_selecionado == "Lítio (Rocha dura versus salmouras)":
        checklist_litio(deposito_selecionado)
        
    elif recurso_selecionado == "Urânio (Combustíveis nucleares)":
        checklist_uranio()
        
    elif recurso_selecionado == "Tório (Combustíveis nucleares)":
        checklist_torio()
        
    elif recurso_selecionado == "Sulfuretos maciços do fundo oceânico (SMS) e crostas de cobalto":
        checklist_sms()
        
    elif recurso_selecionado == "Quartzo":
        checklist_quartzo()
        
    elif recurso_selecionado == "Monazite":
        checklist_monazite()
        
    elif recurso_selecionado == "Ortoclase":
        checklist_ortoclase()       

    else:
        st.checkbox("Verificar propriedades gerais")
        st.checkbox("Testar dureza")
        st.checkbox("Observar fratura")

# ===============================
# 10. MAPA
# ===============================

with tab_mapa:

    if recurso_selecionado == "Hidrogénio (Geração natural e armazenamento)":
        mapa_hidrogenio()
        
    elif recurso_selecionado == "Petróleo e Gás (Sistemas convencionais)":
        mapa_petroleo()
              
    elif recurso_selecionado == "Metano (Hidratos e recursos não convencionais)":
        mapa_metano()
        
    elif recurso_selecionado == "Lítio (Rocha dura versus salmouras)":
        mapa_litio()
        
    elif recurso_selecionado == "Urânio (Combustíveis nucleares)":
        mapa_uranio()
        
    elif recurso_selecionado == "Tório (Combustíveis nucleares)":
        mapa_torio()
        
    elif recurso_selecionado == "Sulfuretos maciços do fundo oceânico (SMS) e crostas de cobalto":
        mapa_sms()
        
    elif recurso_selecionado == "Quartzo":
        mapa_quartzo()
        
    elif recurso_selecionado == "Monazite":
        mapa_monazite()
        
    elif recurso_selecionado == "Ortoclase":
        mapa_ortoclase()      

    else:

        st.info("Mapa genérico")

        uploaded_file = st.file_uploader("CSV", type=["csv"])

        if uploaded_file:
            df = pd.read_csv(uploaded_file)

            mapa = folium.Map(location=[20, 0], zoom_start=2)
            Fullscreen().add_to(mapa)

            for _, row in df.iterrows():
                if pd.notna(row["Latitude"]) and pd.notna(row["Longitude"]):
                    folium.CircleMarker(
                        [row["Latitude"], row["Longitude"]],
                        radius=5
                    ).add_to(mapa)

            st_folium(mapa, use_container_width=True)

# ===============================
# 11. REFERÊNCIAS
# ===============================

with tab_ref:

    if recurso_selecionado == "Hidrogénio (Geração natural e armazenamento)":
        referencias_hidrogenio()
        
    elif recurso_selecionado == "Petróleo e Gás (Sistemas convencionais)":
        referencias_petroleo()
        
    elif recurso_selecionado == "Metano (Hidratos e recursos não convencionais)":
        referencias_metano()
        
    elif recurso_selecionado == "Lítio (Rocha dura versus salmouras)":
        referencias_litio()
        
    elif recurso_selecionado == "Urânio (Combustíveis nucleares)":
        referencias_uranio()
        
    elif recurso_selecionado == "Tório (Combustíveis nucleares)":
        referencias_torio()
        
    elif recurso_selecionado == "Sulfuretos maciços do fundo oceânico (SMS) e crostas de cobalto":
        referencias_sms()
        
    elif recurso_selecionado == "Quartzo":
        referencias_quartzo()
        
    elif recurso_selecionado == "Monazite":
        referencias_monazite()
        
    elif recurso_selecionado == "Ortoclase":
        referencias_ortoclase()      

    else:
        st.info("Referências em desenvolvimento.")
        



