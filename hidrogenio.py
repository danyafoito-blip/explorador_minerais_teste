# ===============================
# BIBLIOTECAS EXTERNAS
# ===============================

import streamlit as st
import streamlit.components.v1 as components


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_hidrogenio(deposito):

    st.markdown("### Hidrogénio geológico")
    
    st.markdown(
        """
        O **hidrogénio geológico** corresponde ao hidrogénio molecular (**H₂**) gerado
        *in situ* por processos geoquímicos naturais na crosta e no manto, 
        como a **serpentinização** e a **radiólise da água**.  
    
        Este gás ocorre e acumula-se no subsolo sem intervenção antrópica, sendo
        frequentemente designado como **hidrogénio** **branco** ou **dourado**, e é
        considerado uma potencial fonte de energia primária com relevância
        crescente na **transição energética**.
        """
    )
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
    
        st.success("**Propriedades físicas**")
    
        st.write("- Gás incolor, inodoro e insípido")
        st.write("- Densidade extremamente baixa (gás mais leve)")
        st.write("- Pontos de fusão e ebulição muito baixos")
        st.write("- Alta densidade energética por massa")
        st.write("- Difusividade muito elevada")
    
    with col2:
    
        st.info("**Propriedades químicas**")
    
        st.write("- Molécula H₂ com ligação covalente forte")
        st.write("- Baixa reatividade em condições normais")
        st.write("- Elevada reatividade a altas temperaturas")
        st.write("- Altamente inflamável")
        st.write("- Forte agente redutor")
    
    st.divider()

    if "Serpentinização" in deposito:

        st.markdown("### Serpentinização")
    
        st.markdown(
        """
        A **serpentinização** é um processo **metamórfico-hidrotermal** em que 
        a água reage com **rochas ultramáficas** (ricas em ferro e magnésio), 
        levando à produção de **hidrogénio (H₂)**.
    
        É o **principal mecanismo natural de geração de hidrogénio** na crosta 
        terrestre.
        """
        )
    
        st.success("💡 Ideia-chave: água + minerais ricos em ferro → produção de H₂")
        
        st.divider()

        st.markdown("### Mecanismos de geração de hidrogénio geológico")
    
        st.markdown(
        """
        O processo baseia-se numa **reação redox**:
    
        - O **ferro (Fe²⁺)** nos minerais oxida-se para **Fe³⁺**
        - A **água reduz-se**, formando **hidrogénio (H₂)**
    
        **Minerais principais:**
        - Olivina (mais reativa)
        - Piroxenas
        """
        )
    
        st.code(
            """
        3Fe₂SiO₄ + 2H₂O → 2Fe₃O₄ + 3SiO₂ + 2H₂
        (Olivina → Magnetite + Sílica + Hidrogénio)
            """
        )
    
        st.info(
        "✔ A produção de H₂ aumenta quando há consumo de sílica "
        "(formação de serpentina favorece a reação)."
        )
        
        st.divider()
    
        st.markdown("### Condições físico-químicas")
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            st.metric("Temperatura ideal", "200–320 °C")
            st.caption("Baixa eficiência <100 °C | Inibe >350 °C")
    
        with col2:
            st.metric("Pressão", "Elevada")
            st.caption("Aumenta taxa de reação")
    
        with col3:
            st.metric("Fluidos", "Essenciais")
            st.caption("Água do mar, meteórica ou de subducção")
    
        st.warning(
            "⚠️ O processo requer circulação contínua de fluidos através de fraturas."
        )
        
        st.divider()

        st.markdown("### Ambientes geológicos favoráveis")
    
        st.write("""
    - Dorsais médio-oceânicas  
    - Ofiolitos  
    - Zonas de subducção  
    - Cratões e greenstone belts  
        """)
    
        st.success("💡 Fator crítico: presença de fraturas para circulação de fluidos")
    
        st.divider()
    
        st.markdown("### Rocha geradora")
    
        st.markdown(
        """
        **Rocha geradora**: formação rochosa onde o hidrogénio é **gerado in situ**
        por reações geoquímicas.
        """
        )
        
        st.info(
        """        
        **Rochas ultramáficas** (ex: peridotitos)
        
        ✔ Ricas em ferro e magnésio  
        ✔ Pobres em sílica  
        ✔ Contêm olivina (mineral-chave)
        """
        )
        
        st.divider()
    
        st.markdown("### Migração")
        
        st.markdown(
        """
        **Migração**: movimento do hidrogénio (**H₂**) desde a sua **geração**
        até à sua **acumulação num reservatório** ou escape para a superfície.
        """
        )
        
        st.markdown("#### Tipos de migração")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(" - **Primária**")
            st.write(
                "Libertação do H₂ da rocha onde é gerado, migrando para fraturas "
                "ou poros adjacentes devido à acumulação de pressão"
            )
        
        with col2:
            st.write(" - **Secundária**")
            st.write(
                "Transporte do H₂ através de formações permeáveis até reservatórios "
                "ou até à superfície (seepage)"
            )
        
        st.info("✔ A migração secundária é essencial para formar acumulações exploráveis")

        st.markdown("#### Mecanismos de migração")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(" - **Advecção**")
            st.write(
                "Transporte rápido devido a gradientes de pressão e à baixa densidade "
                "do H₂ (flutuabilidade), predominando em fraturas e falhas"
            )
        
        with col2:
            st.write(" - **Difusão**")
            st.write(
                "Transporte lento devido a gradientes de concentração, importante em "
                "rochas pouco permeáveis ou através de selantes"
            )
        
        st.warning(
            """⚠️ Devido à elevada difusividade do hidrogénio, 
            a retenção eficiente requer boas rochas selantes."""
        )
        
        st.divider()

        st.markdown("### Rocha reservatório")

        st.markdown(
        """
        **Rocha reservatório**: formação rochosa **porosa e permeável** 
        onde o hidrogénio (**H₂**) se acumula após a sua migração, 
        permitindo o seu armazenamento.
        """
        )
        
        st.write("""
        - Arenitos  
        - Carbonatos (carstificados)  
        - Peridotitos fraturados  
        """)
    
        st.success("💡 Necessário: alta porosidade + permeabilidade")
    
        st.divider()
        
        st.markdown("### Rocha selante")

        st.markdown(
        """
        **Rocha selante**: formação rochosa de **baixa permeabilidade** 
        que impede a fuga do hidrogénio (**H₂**), atuando como uma barreira 
        acima do reservatório.
        """
        )
        
        st.write("""
        - Evaporitos (sal)  
        - Intrusões de dolerito (sills)  
        - Argilito (shales)  
        - Rochas ígneas e metamórficas não fraturadas  
        - Argilas e metassedimentos  
        """)
    
        st.warning("⚠️ Essencial para impedir fuga do H₂")
    
        st.divider()

        st.markdown("### Armadilhas")
        
        st.markdown(
        """
        **Armadilhas**: configurações de rochas reservatório e selantes que permitem a 
        **acumulação e retenção do hidrogénio (H₂)**, impedindo a sua fuga para a superfície.
        """
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Estruturais")
            st.write("""
            - Anticlinais  
            - Falhas  
            - Domos de sal  
            - Horsts e grabens  
            """)
        
        with col2:
            st.markdown("#### Estratigráficas")
            st.write("""
            - Cársticas  
            - Discordâncias  
            - Canais sedimentares  
            """)
        
        st.success(
            "💡 Armadilhas permitem acumulação económica de hidrogénio."
        )

    elif "Radiólise da água" in deposito:
    
        st.markdown("### Radiólise da água")
    
        st.markdown(
        """
        A **radiólise da água** é um processo geoquímico no qual a água é dissociada
        pela **radiação natural** emitida por elementos radioativos presentes nas rochas.
    
        Este processo gera **hidrogénio (H₂)** de forma contínua ao longo de **escalas de tempo geológicas**.
        """
        )
    
        st.success("💡 Ideia-chave: radiação + água → dissociação → produção de H₂")
    
        st.divider()

        st.markdown("### Mecanismos de geração de hidrogénio geológico")
        
        st.markdown(
        """
        A radiação ionizante (α, β, γ) emitida por elementos como:
        
        - Urânio (U)  
        - Tório (Th)  
        - Potássio (K)  
        
        Interage com a água, provocando a sua dissociação em espécies reativas.
        """
        )
        
        st.code("""
        H₂O → H∙ + OH∙
        (Água → Radical de hidrogénio + Radical hidroxilo)
        
        H∙ + H∙ → H₂
        (Radicais de hidrogénio → Hidrogénio molecular)
        
        OH∙ + OH∙ → H₂O₂
        (Radicais hidroxilo → Peróxido de hidrogénio)
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("✔ O H₂ forma-se pela recombinação de radicais de hidrogénio.")
        
        with col2:
            st.info("✔ Subprodutos oxidantes (ex: H₂O₂) podem consumir parte do H₂.")
    
        st.divider()

        st.markdown("### Condições físico-químicas")
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            st.metric("Radiação", "Elevada")
            st.caption("Controla a taxa de produção de H₂")
    
        with col2:
            st.metric("Fluidos", "Essenciais")
            st.caption("Água em poros/fraturas (salmouras aumentam eficiência)")
    
        with col3:
            st.metric("Tempo", "Muito longo")
            st.caption("Milhões a biliões de anos")
    
        st.warning(
            "⚠️ Processo lento, mas contínuo e cumulativo ao longo do tempo geológico."
        )
    
        st.divider()

        st.markdown("### Ambientes geológicos favoráveis")
    
        st.write("""
    - Cratões e escudos pré-cambrianos  
    - Depósitos de urânio  
    - Ambientes crustais profundos  
    - Sistemas hidrotermais  
        """)
    
        st.success(
            "💡 Ambientes estáveis favorecem acumulação prolongada de H₂."
        )
    
        st.divider()

        st.markdown("### Rocha geradora")
        
        st.markdown(
        """
        **Rocha geradora**: formação rochosa onde o hidrogénio é **gerado in situ**
        por reações geoquímicas.
        """
        )     
    
        st.info(
        """
        **Rochas graníticas e cristalinas radiogénicas**
    
        ✔ Ricas em U, Th e K  
        ✔ Elevada produção de radiação  
        ✔ Associadas a basement antigo  
        """
        )
    
        st.divider()
        
        st.markdown("### Migração")
        
        st.markdown(
        """
        **Migração**: movimento do hidrogénio (**H₂**) desde a sua **geração**
        até à sua **acumulação num reservatório** ou escape para a superfície.
        """
        )
        
        st.markdown("#### Tipos de migração")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(" - **Primária**")
            st.write(
                "Libertação do H₂ da rocha onde é gerado, migrando para fraturas "
                "ou poros adjacentes devido à acumulação de pressão"
            )
        
        with col2:
            st.write(" - **Secundária**")
            st.write(
                "Transporte do H₂ através de formações permeáveis até reservatórios "
                "ou até à superfície (seepage)"
            )
        
        st.info("✔ A migração secundária é essencial para formar acumulações exploráveis")
        
        st.markdown("#### Mecanismos de migração")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(" - **Advecção**")
            st.write(
                "Transporte rápido devido a gradientes de pressão e à baixa densidade "
                "do H₂ (flutuabilidade), predominando em fraturas e falhas"
            )
        
        with col2:
            st.write(" - **Difusão**")
            st.write(
                "Transporte lento devido a gradientes de concentração, importante em "
                "rochas pouco permeáveis ou através de selantes"
            )
        
        st.warning(
            """⚠️ Devido à elevada difusividade do hidrogénio, 
            a retenção eficiente requer boas rochas selantes."""
        )
    
        st.divider()
    
        st.markdown("### Rocha reservatório")
        
        st.markdown(
        """
        **Rocha reservatório**: formação rochosa **porosa e permeável** 
        onde o hidrogénio (**H₂**) se acumula após a sua migração, 
        permitindo o seu armazenamento.
        """
        )
    
        st.write("""
    - Arenitos  
    - Carbonatos  
    - Fraturas e inclusões no embasamento  
        """)
    
        st.success(
            "💡 Pode ocorrer armazenamento direto no basement fraturado."
        )
    
        st.divider()
        
        st.markdown("### Rocha selante")

        st.markdown(
        """
        **Rocha selante**: formação rochosa de **baixa permeabilidade** 
        que impede a fuga do hidrogénio (**H₂**), atuando como uma barreira 
        acima do reservatório.
        """
        )
        
        st.write("""
        - Evaporitos (sal)  
        - Intrusões de dolerito (sills)  
        - Argilito (shales)  
        - Rochas ígneas e metamórficas não fraturadas  
        - Argilas e metassedimentos  
        """)
    
        st.warning("⚠️ Essencial para impedir fuga do H₂")

        st.divider()
    
        st.markdown("### Armadilhas")
        
        st.markdown(
        """
        **Armadilhas**: configurações de rochas reservatório e selantes que permitem a 
        **acumulação e retenção do hidrogénio (H₂)**, impedindo a sua fuga para a superfície.
        """
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Estruturais")
            st.write("""
            - Anticlinais  
            - Falhas  
            - Domos de sal  
            - Horsts e grabens  
            """)
        
        with col2:
            st.markdown("#### Estratigráficas")
            st.write("""
            - Cársticas  
            - Discordâncias  
            - Canais sedimentares  
            """)
        
        st.success(
            "💡 Armadilhas permitem acumulação económica de hidrogénio."
        )

    else:

        st.info("Selecione um tipo de depósito válido.")

# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_hidrogenio():

    st.markdown("### Confusões comuns")

    st.markdown("**1. Serpentinização vs Radiólise da água**")

    st.write("""
- **Serpentinização**:
  - Processo **hidrotermal** em rochas ultramáficas (ex: peridotitos)
  - Reação água–rocha com oxidação do ferro (Fe²⁺ → Fe³⁺)
  - Produção de H₂ geralmente **mais rápida e localizada**
  - Requer temperaturas moderadas (~200–320 °C)

- **Radiólise da água**:
  - Processo **radiogénico** em rochas ricas em U, Th e K
  - Dissociação da água por radiação ionizante
  - Produção de H₂ **lenta, mas contínua ao longo do tempo geológico**
  - Pode ocorrer em maior profundidade e ampla gama de temperaturas
    """)

    st.info("💡 Ocorrem em contextos geológicos distintos.")

    st.divider()

    st.markdown("**2. Fonte do hidrogénio**")

    st.write("""
- **Serpentinização** → reações **redox água–minerais**
- **Radiólise da água** → **radiação ionizante** quebra a molécula de água
    """)

    st.info("💡 Nem todo o H₂ tem origem em reações geoquímicas clássicas.")

    st.divider()

    st.markdown("**3. Taxa de produção vs Tempo**")

    st.write("""
- **Serpentinização** → produção mais elevada, dependente de circulação de fluidos
- **Radiólise da água** → produção baixa, mas contínua durante milhões a biliões de anos
    """)

    st.info("💡 Processos lentos podem gerar volumes significativos ao longo do tempo.")

    st.divider()

    st.markdown("**4. Rocha geradora**")

    st.write("""
- **Serpentinização** → rochas ultramáficas (ricas em olivina)
- **Radiólise da água** → rochas graníticas/cristalinas radiogénicas
    """)

    st.info("💡 A composição mineralógica é determinante para a geração de H₂.")

    st.divider()

    st.markdown("**5. Papel dos fluidos**")

    st.write("""
- **Serpentinização** → requer circulação ativa de água
- **Radiólise da água** → pode ocorrer com água aprisionada em poros/fraturas
    """)

    st.info("💡 Nem todos os sistemas requerem fluxo hidrotermal ativo.")

    st.divider()

    st.markdown("**6. Contexto geológico**")

    st.write("""
- **Serpentinização** → dorsais oceânicas, ofiolitos, zonas de subducção
- **Radiólise da água** → cratões antigos e embasamento profundo
    """)

    st.info("💡 O ambiente geológico é chave para identificar o processo.")

    st.divider()

    st.markdown("**7. Associação com outros gases**")

    st.write("""
- **Serpentinização** → frequentemente associada a metano (CH₄)
- **Radiólise da água** → pode gerar espécies oxidantes (ex: H₂O₂)
    """)

    st.info("💡 O contexto geoquímico ajuda a distinguir a origem do H₂.")

    st.divider()

    st.markdown("**8. Potencial económico**")

    st.write("""
- **Serpentinização** → maior potencial de acumulação explorável
- **Radiólise da água** → contributo mais difuso, mas relevante em sistemas antigos
    """)

    st.info("💡 Ambos os processos podem ser relevantes dependendo do contexto.")
    
# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_hidrogenio(deposito):

    st.markdown("### Quiz interativo")
    st.caption("Testa os teus conhecimentos")

    if "Serpentinização" in deposito:

        if "corrigido_serp" not in st.session_state:
            st.session_state.corrigido_serp = False

        corretas = [
            "Reação água–rocha (redox)",
            "Olivina",
            "200–320 ºC",
            "Rochas ultramáficas",
            "Circulação de fluidos"
        ]

        q1 = st.radio("1️⃣ Processo dominante:",
                      ["Radiação ionizante", "Reação água–rocha (redox)", "Combustão", "Evaporação"],
                      key="serp_q1", index=None)

        if st.session_state.corrigido_serp:
            if q1 == corretas[0]:
                st.success("Correto ✅")
            elif q1 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[0]}**")

        st.divider()

        q2 = st.radio("2️⃣ Mineral-chave:",
                      ["Quartzo", "Olivina", "Calcite", "Gesso"],
                      key="serp_q2", index=None)

        if st.session_state.corrigido_serp:
            if q2 == corretas[1]:
                st.success("Correto ✅")
            elif q2 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[1]}**")

        st.divider()

        q3 = st.radio("3️⃣ Intervalo de temperatura típico:",
                      ["<100 ºC", "200–320 ºC", "500–700 ºC", "0–50 ºC"],
                      key="serp_q3", index=None)

        if st.session_state.corrigido_serp:
            if q3 == corretas[2]:
                st.success("Correto ✅")
            elif q3 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[2]}**")

        st.divider()

        q4 = st.radio("4️⃣ Tipo de rocha geradora:",
                      ["Granito", "Rochas ultramáficas", "Arenito", "Basalto"],
                      key="serp_q4", index=None)

        if st.session_state.corrigido_serp:
            if q4 == corretas[3]:
                st.success("Correto ✅")
            elif q4 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[3]}**")

        st.divider()

        q5 = st.radio("5️⃣ Fator essencial para geração contínua:",
                      ["Ausência de água", "Circulação de fluidos", "Baixa pressão", "Ambiente seco"],
                      key="serp_q5", index=None)

        if st.session_state.corrigido_serp:
            if q5 == corretas[4]:
                st.success("Correto ✅")
            elif q5 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[4]}**")

        if st.button("Concluir"):
            st.session_state.corrigido_serp = True

        if st.session_state.corrigido_serp:
            respostas = [q1, q2, q3, q4, q5]
            score = sum([r == c for r, c in zip(respostas, corretas)])
            st.markdown(f"### 🎯 Pontuação: {score}/5")

    elif "Radiólise da água" in deposito:

        if "corrigido_rad" not in st.session_state:
            st.session_state.corrigido_rad = False

        corretas = [
            "Radiação ionizante",
            "Urânio, Tório e Potássio",
            "Muito longo (milhões a biliões de anos)",
            "Rochas graníticas/cristalinas",
            "Baixa taxa mas contínua"
        ]

        q1 = st.radio("1️⃣ Processo dominante:",
                      ["Reação redox", "Radiação ionizante", "Fotossíntese", "Combustão"],
                      key="rad_q1", index=None)

        if st.session_state.corrigido_rad:
            if q1 == corretas[0]:
                st.success("Correto ✅")
            elif q1 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[0]}**")

        st.divider()

        q2 = st.radio("2️⃣ Elementos responsáveis:",
                      ["Ferro e magnésio", "Urânio, Tório e Potássio", "Carbono", "Enxofre"],
                      key="rad_q2", index=None)

        if st.session_state.corrigido_rad:
            if q2 == corretas[1]:
                st.success("Correto ✅")
            elif q2 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[1]}**")

        st.divider()

        q3 = st.radio("3️⃣ Escala temporal:",
                      ["Horas", "Dias", "Muito longo (milhões a biliões de anos)", "Semanas"],
                      key="rad_q3", index=None)

        if st.session_state.corrigido_rad:
            if q3 == corretas[2]:
                st.success("Correto ✅")
            elif q3 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[2]}**")

        st.divider()

        q4 = st.radio("4️⃣ Tipo de rocha geradora:",
                      ["Peridotitos", "Rochas graníticas/cristalinas", "Arenitos", "Basaltos"],
                      key="rad_q4", index=None)

        if st.session_state.corrigido_rad:
            if q4 == corretas[3]:
                st.success("Correto ✅")
            elif q4 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[3]}**")

        st.divider()

        q5 = st.radio("5️⃣ Característica da produção de H₂:",
                      ["Alta e instantânea", "Baixa taxa mas contínua", "Inexistente", "Explosiva"],
                      key="rad_q5", index=None)

        if st.session_state.corrigido_rad:
            if q5 == corretas[4]:
                st.success("Correto ✅")
            elif q5 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[4]}**")

        if st.button("Concluir"):
            st.session_state.corrigido_rad = True

        if st.session_state.corrigido_rad:
            respostas = [q1, q2, q3, q4, q5]
            score = sum([r == c for r, c in zip(respostas, corretas)])
            st.markdown(f"### 🎯 Pontuação: {score}/5")

    else:
        st.info("Selecione um tipo de depósito válido.")

# ===============================
# 4. CHECKLIST DE CAMPO
# ===============================

def checklist_hidrogenio():

    st.markdown("### Checklist de campo")

    st.write("Avaliação integrada de um sistema de hidrogénio geológico:")

    st.markdown("**1. Geração de hidrogénio**")

    st.checkbox("Identificar evidências de serpentinização (rochas ultramáficas, serpentina)")
    st.checkbox("Identificar rochas radiogénicas (granitos ricos em U, Th, K)")
    st.checkbox("Confirmar presença de água (fluido essencial)")
    st.checkbox("Avaliar condições de temperatura e pressão adequadas")
    st.checkbox("Analisar mineralogia (olivina, piroxenas, minerais alterados)")

    st.divider()

    st.markdown("**2. Rocha geradora**")

    st.checkbox("Confirmar presença de rochas ultramáficas (peridotitos)")
    st.checkbox("Identificar rochas graníticas/cristalinas radiogénicas")
    st.checkbox("Avaliar grau de alteração (ex: serpentinização ativa ou relicta)")

    st.divider()

    st.markdown("**3. Migração**")

    st.checkbox("Mapear falhas, fraturas e zonas de cisalhamento")
    st.checkbox("Avaliar conectividade de fraturas (permeabilidade)")
    st.checkbox("Identificar evidências de migração ativa (seepage de H₂)")
    st.checkbox("Medir emissões gasosas (H₂, CH₄)")
    st.checkbox("Avaliar mecanismos dominantes (advecção e difusão)")

    st.divider()

    st.markdown("**4. Rocha reservatório**")

    st.checkbox("Identificar formações porosas e permeáveis (arenitos, carbonatos)")
    st.checkbox("Avaliar porosidade e permeabilidade")
    st.checkbox("Verificar presença de fraturação no reservatório")
    st.checkbox("Confirmar capacidade de armazenamento de gás")

    st.divider()

    st.markdown("**5. Rocha selante**")

    st.checkbox("Identificar rochas de baixa permeabilidade (argilas, evaporitos, shales)")
    st.checkbox("Verificar continuidade lateral do selante")
    st.checkbox("Avaliar integridade (ausência de fraturas abertas)")
    st.checkbox("Confirmar capacidade de retenção de H₂")

    st.divider()

    st.markdown("**6. Armadilha**")

    st.checkbox("Identificar armadilhas estruturais (anticlinais, falhas, domos de sal)")
    st.checkbox("Identificar armadilhas estratigráficas (discordâncias, pinch-outs)")
    st.checkbox("Confirmar geometria favorável à acumulação")
    st.checkbox("Verificar relação reservatório–selante")

    st.divider()

    st.markdown("**7. Indicadores complementares**")

    st.checkbox("Presença de gases associados (CH₄, He)")
    st.checkbox("Anomalias geoquímicas no solo")
    st.checkbox("Avaliação da atividade microbiana (consumo de H₂)")
    st.checkbox("Indício de sistema ativo")
    st.checkbox("Indício de sistema relicto")

    st.success("💡 Um sistema viável requer: geração + migração + reservatório + selante + armadilha.")

# ===============================
# 5. MAPA GLOBAL
# ===============================

def mapa_hidrogenio():

    st.markdown("### 🌍 Mapa global de ocorrências de hidrogénio")

    with open("occurrences_hydrogen.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    html_with_fullscreen = f"""
    <button onclick="openFullscreen()" style="
        position: fixed;
        top: 10px;
        right: 10px;
        z-index: 9999;
        padding: 8px 12px;
        background-color: #1f77b4;
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;">
        ⛶ Fullscreen
    </button>

    <script>
    function openFullscreen() {{
        var elem = document.documentElement;
        if (elem.requestFullscreen) {{
            elem.requestFullscreen();
        }} else if (elem.webkitRequestFullscreen) {{
            elem.webkitRequestFullscreen();
        }} else if (elem.msRequestFullscreen) {{
            elem.msRequestFullscreen();
        }}
    }}
    </script>

    {html_content}
    """

    components.html(html_with_fullscreen, height=700, scrolling=True)

# ===============================
# 6. REFERÊNCIAS
# ===============================

def referencias_hidrogenio():

    st.markdown("### 📚 Referências bibliográficas")

    st.write(
    "- Etiope, G., Ellis, G. S., Ardakani, O. H., Boreham, C. J., Klitzke, P., "
    "Martín-Monge, A., Reisi, H. L. S., Templeton, A. S., Kim, H. S., Gaucher, E., "
    "& Sissmann, O. (2026). Understanding the resource potential of natural hydrogen "
    "on Earth: Scientific gaps, uncertainties and recommendations. Earth-Science Reviews, "
    "275, 105413."
    )
    
    st.write(
    "- Mao, S., Yu, S., Xu, J., Chen, H., Zhao, W., Blunt, M. J., Kang, Q., Gross, M., "
    "Chen, B., Van Wijk, J., Yuan, Q., Gao, K., Kazi, S. R., & Mehanah, M. (2025). "
    "Geologic hydrogen: A review of resource potential, subsurface dynamics, exploration, "
    "production, transportation, and research opportunities. Energy & Environmental Science, "
    "18, 9991–10035."
    )
    
    st.write(
    "- Liang, Y., Meng, Q., Huang, X., Lu, W., Wei, Y., Liu, J., Zhou, Y., Huang, L., "
    "Li, Q., Chen, J., & Zhou, D. (2025). Global distribution, genesis, and enrichment "
    "characteristics of high-concentration natural hydrogen. Frontiers in Marine Science, "
    "12, 1688404."
    )
    
    st.write(
    "- Levikhin, A. A., & Boryaev, A. A. (2024). Physical properties and thermodynamic "
    "characteristics of hydrogen. Heliyon, 10, e36414."
    )
    
    st.write(
    "- Woo, J., Kim, W.-K., Rhee, C. W., & Lee, S. (2025). A review of hydrogen systems "
    "and exploration methodologies for natural hydrogen exploration. Journal of the Korean "
    "Society of Mineral and Energy Resources Engineers, 62(3), 312–326."
    )
    
    st.write(
    "- Matyasik, I., & Ciechanowska, M. (2024). Possibilities of natural hydrogen deposits "
    "in Polish conditions. Nafta-Gaz, 6, 327–334."
    )
    
    st.write(
    "- Jackson, O., Lawrence, S. R., Hutchinson, I. P., Stocks, A. E., Barnicoat, A. C., "
    "& Powney, M. (2024). Natural hydrogen: Sources, systems and exploration plays. "
    "Geoenergy, 2, geoenergy2024-002."
    )
    
    st.write(
    "- Gelman, S. E., Hearon, J. S., & Ellis, G. S. (2025). Prospectivity mapping for "
    "geologic hydrogen (Version 1.2, January 22, 2025). U.S. Geological Survey."
    )

    st.caption("Referências utilizadas.")
    