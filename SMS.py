import streamlit as st

def quiz_sms():
    """Função que guarda e corre o quiz dos Sulfuretos (SMS)"""
    
    st.write("Responda às seguintes questões sobre a formação e exploração de depósitos SMS:")
    
    q1 = st.radio(
        "**1. Qual é o principal mecanismo que faz com que os metais precipitem e formem as chaminés de SMS no fundo do mar?**",
        [
            "A) O arrefecimento lento do magma em profundidade.",
            "B) O choque térmico e químico entre o fluido hidrotermal a ~350°C e a água do mar a ~2°C.",
            "C) A compactação dos sedimentos marinhos devido ao peso da coluna de água.",
            "D) A oxidação das rochas basálticas pela luz solar."
        ],
        index=None
    )

    q2 = st.radio(
        "**2. Se fores avaliar a viabilidade de uma exploração mineira de um depósito análogo em terra (VMS), que diferença física fundamental esperas encontrar em relação a um SMS fresco do fundo do mar?**",
        [
            "A) O depósito em terra será muito mais poroso e leve.",
            "B) O depósito em terra não terá sulfuretos, apenas óxidos.",
            "C) O depósito em terra será muito mais denso, compacto e menos friável devido à compressão tectónica.",
            "D) Não haverá diferença, a rocha mantém-se intacta para sempre."
        ],
        index=None
    )

    q3 = st.radio(
        "**3. Quais são os dois metais base mais rentáveis e abundantes extraídos deste tipo de sulfuretos (tanto SMS como VMS)?**",
        [
            "A) Alumínio e Níquel.",
            "B) Ferro e Manganês.",
            "C) Cobre e Zinco.",
            "D) Lítio e Cobalto."
        ],
        index=None
    )

    q4 = st.radio(
        "**4. O que acontece à rocha por baixo do depósito maciço (a chamada zona de stockwork ou condutas) devido à passagem contínua dos fluidos quentes?**",
        [
            "A) Fica mais dura e resistente que o basalto original.",
            "B) Sofre alteração hidrotermal, tornando-se uma zona fraturada e frequentemente argilizada, com implicações na estabilidade mecânica.",
            "C) Transforma-se em calcário puro.",
            "D) Derrete completamente, formando um lago de lava subterrâneo."
        ],
        index=None
    )

    st.write("") # Espaço em branco
    
    if st.button("Submeter Respostas"):
        # Variável para contar a pontuação
        pontuacao = 0
        
        # Verificação da Q1
        if q1 and q1.startswith("B)"):
            st.success("1. Correto!")
            pontuacao += 1
        elif q1:
            st.error("1. Incorreto. A resposta certa era a B.")
            
        # Verificação da Q2
        if q2 and q2.startswith("C)"):
            st.success("2. Correto!")
            pontuacao += 1
        elif q2:
            st.error("2. Incorreto. A resposta certa era a C.")
            
        # Verificação da Q3
        if q3 and q3.startswith("C)"):
            st.success("3. Correto!")
            pontuacao += 1
        elif q3:
            st.error("3. Incorreto. A resposta certa era a C.")
            
        # Verificação da Q4
        if q4 and q4.startswith("B)"):
            st.success("4. Correto!")
            pontuacao += 1
        elif q4:
            st.error("4. Incorreto. A resposta certa era a B.")
            
        # Resultado Final
        st.divider()
        if pontuacao == 4:
            st.balloons()
            st.success(f"🎉 Brilhante! Acertou {pontuacao} em 4 questões!")
        elif q1 and q2 and q3 and q4:
            st.info(f"Acertou {pontuacao} em 4. Reveja as opções incorretas e tente novamente!")
        else:
            st.warning("⚠️ Responda a todas as perguntas para ver o seu resultado final.")
