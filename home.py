import streamlit as st
import streamlit.components.v1 as components

# Configuração da página
st.set_page_config(layout="wide", page_title="Portfólio - Alan Barros", page_icon="📊")

# --- CSS Personalizado ---
custom_css = """
<style>
/* Importando fontes do Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Roboto:wght@400;700&display=swap');

/* Fonte Global */
body, .css-1d391kg, .css-18e3th9 {
    font-family: 'Roboto', sans-serif;
    color: #f0f0f0;
}

/* Sidebar */
.sidebar .sidebar-content {
    background-color: #2c3e50;
    color: #ecf0f1;
    padding: 20px;
    border-radius: 10px;
}

/* Título da Sidebar */
.sidebar .sidebar-content h2 {
    font-family: 'Montserrat', sans-serif;
    font-size: 24px;
    text-align: center;
    color: #ecf0f1;
    margin-bottom: 20px;
}

/* Imagem na Sidebar */
.sidebar .sidebar-content img {
    border-radius: 50%;
    margin-bottom: 20px;
    border: 3px solid #1abc9c;
}

/* Divisória na Sidebar */
.sidebar .sidebar-content hr {
    border: 1px solid #ecf0f1;
    margin: 20px 0;
}

/* Estilização dos Botões da Sidebar */
.sidebar .sidebar-content .stButton button {
    background-color: #34495e;
    color: #ecf0f1;
    border: none;
    border-radius: 5px;
    padding: 10px 15px;
    width: 100%;
    text-align: left;
    font-size: 18px;
    font-family: 'Montserrat', sans-serif;
    cursor: pointer;
    transition: background-color 0.3s, transform 0.2s;
    margin-bottom: 10px;
}

.sidebar .sidebar-content .stButton button:hover {
    background-color: #3d566e;
    transform: scale(1.02);
}

.sidebar .sidebar-content .stButton button:active {
    background-color: #1abc9c;
    color: #2c3e50;
}

/* Expanders */
.st-expander > button {
    background-color: #34495e;
    color: #ecf0f1;
    font-size: 18px;
    font-family: 'Montserrat', sans-serif;
    border-radius: 5px;
    padding: 10px;
    display: flex;
    align-items: center;
    transition: background-color 0.3s, transform 0.3s;
}

.st-expander > button:hover {
    background-color: #3d566e;
    transform: scale(1.02);
}

.st-expander > button:after {
    content: '▼';
    margin-left: auto;
    transition: transform 0.3s;
}

.st-expander[aria-expanded="true"] > button:after {
    transform: rotate(180deg);
}

.st-expander > div {
    background-color: #3d566e;
    color: #ecf0f1;
    font-size: 16px;
    font-family: 'Roboto', sans-serif;
    padding: 15px;
    border-radius: 0 0 5px 5px;
}

.st-expander p, .st-expander h1, .st-expander h2, .st-expander h3, .st-expander h4, .st-expander h5, .st-expander h6 {
    color: #ecf0f1;
    line-height: 1.6;
}

/* Links */
a {
    color: #1abc9c;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

/* Títulos no Conteúdo Principal */
.content h1 {
    font-family: 'Montserrat', sans-serif;
    color: #ecf0f1;
    margin-bottom: 10px;
}

/* Ajustes Responsivos */
@media (max-width: 600px) {
    .sidebar .sidebar-content h2 {
        font-size: 20px;
    }
    .sidebar .sidebar-content .stButton button {
        font-size: 16px;
        padding: 8px 12px;
    }
    .st-expander > button {
        font-size: 16px;
    }
    .st-expander > div {
        font-size: 14px;
    }
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# HTML e JavaScript para a animação particles.js com altura reduzida
particles_js = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Particles.js</title>
  <style>
    #particles-js {
      position: fixed;
      width: 100vw;
      height: 100vh; /* Manter a altura total para a animação */
      top: 0;
      left: 0;
      z-index: -1; 
    }
    .content {
      position: relative;
      z-index: 1;
      color: white;
      padding: 20px; /* Ajustar padding para menos espaço */
      text-align: center;
      max-width: 800px;
      margin: 0 auto;
    }
    h1 {
      font-size: 60px; /* Reduzir tamanho da fonte */
      font-family: 'Montserrat', sans-serif;
      text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }
    p {
      font-size: 18px; /* Reduzir tamanho da fonte */
      line-height: 1.5;
      text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
    }
    @media (max-width: 600px) {
      .content {
        padding: 20px;
      }
      h1 {
        font-size: 40px; /* Reduzir ainda mais para telas pequenas */
      }
      p {
        font-size: 16px; 
      }
    }
  </style>
</head>
<body>
  <div id="particles-js"></div>
  <div class="content">
    <h1>ALAN BARROS</h1>
    <p>🎲 Ajudando empresas a tomar decisões estratégicas com base em dados 🎲</p>
  </div>
  <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
  <script>
    particlesJS("particles-js", {
      "particles": {
        "number": {
          "value": 150,
          "density": {
            "enable": true,
            "value_area": 800
          }
        },
        "color": {
          "value": "#ffffff"
        },
        "shape": {
          "type": "circle",
          "stroke": {
            "width": 0,
            "color": "#000000"
          },
          "polygon": {
            "nb_sides": 5
          }
        },
        "opacity": {
          "value": 0.5,
          "random": false,
          "anim": {
            "enable": false,
            "speed": 1,
            "opacity_min": 0.2,
            "sync": false
          }
        },
        "size": {
          "value": 3,
          "random": true,
          "anim": {
            "enable": false,
            "speed": 40,
            "size_min": 0.1,
            "sync": false
          }
        },
        "line_linked": {
          "enable": true,
          "distance": 150,
          "color": "#ffffff",
          "opacity": 0.4,
          "width": 1
        },
        "move": {
          "enable": true,
          "speed": 2,
          "direction": "none",
          "random": false,
          "straight": false,
          "out_mode": "out",
          "bounce": false,
          "attract": {
            "enable": false,
            "rotateX": 600,
            "rotateY": 1200
          }
        }
      },
      "interactivity": {
        "detect_on": "canvas",
        "events": {
          "onhover": {
            "enable": true,
            "mode": "repulse"
          },
          "onclick": {
            "enable": true,
            "mode": "push"
          },
          "resize": true
        },
        "modes": {
          "grab": {
            "distance": 400,
            "line_linked": {
              "opacity": 1
            }
          },
          "bubble": {
            "distance": 400,
            "size": 40,
            "duration": 2,
            "opacity": 8,
            "speed": 3
          },
          "repulse": {
            "distance": 200,
            "duration": 0.4
          },
          "push": {
            "particles_nb": 4
          },
          "remove": {
            "particles_nb": 2
          }
        }
      },
      "retina_detect": true
    });
  </script>
</body>
</html>
"""

# Renderizar a animação
components.html(particles_js, height=375, scrolling=False)

# --- SIDEBAR --- 
st.sidebar.markdown("<h2>Portfólio</h2>", unsafe_allow_html=True)
st.sidebar.image("eu.png", use_column_width=True, caption="Data Analyst")

# Adicionando mais informações à sidebar
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

# Inicializar a seleção no estado da sessão
if 'selection' not in st.session_state:
    st.session_state['selection'] = "Sobre mim"

# Funções para atualizar a seleção
def set_selection(option):
    st.session_state['selection'] = option

# Botões com estilo tecnológico
buttons = ["Sobre mim", "Projetos", "Contato"]

for btn in buttons:
    if st.sidebar.button(btn):
        set_selection(btn)

# Atualizar a seleção com base no estado da sessão
selection = st.session_state['selection']

# --- CONTEÚDO PRINCIPAL --- 
if selection == "Sobre mim":
    with st.expander("🔍 Sobre Mim", expanded=True): 
        st.markdown(""" 
        🔍 **Especialista em análise de dados** com vasta experiência em transformar dados complexos em insights acionáveis.  
        📊 **Possuo expertise em Power BI, SQL, e Python**, focado em gerar resultados que impulsionam eficiência operacional e otimização de custos. Sou apaixonado por resolver problemas de negócios através da automação de relatórios, visualização de dados e modelagem preditiva.  
        🎓 **Graduado em Administração** pela Universidade Estadual do Maranhão, e atualmente cursando uma especialização em **Análise de Dados e Inteligência Artificial** na Universidade Federal do Maranhão.

        ### Experiência Profissional
        #### HealthBit - Inteligência em Saúde · Tempo integral
        *Jan de 2023 - Presente · 1 ano 10 meses*
        - Desenvolvimento de dashboards interativos no Power BI para monitorar a utilização de planos de saúde e identificar oportunidades de **redução de custos**.
        - Aplicação de ETL para tratar grandes volumes de dados e gerar relatórios automatizados.
        - Criação de modelos preditivos utilizando Python para melhorar a tomada de decisões em saúde corporativa.

        #### RankMyApp · Tempo integral
        *Ago de 2022 - Nov de 2022 · 4 meses*
        - Supervisão de campanhas publicitárias utilizando análise de dados para otimizar taxas de conversão e engajamento.
        - Criação de relatórios dinâmicos e painéis interativos para acompanhamento de KPIs de marketing.

        #### Gupy · Analista de Negócios
        *Out de 2019 - Jul de 2022 · 2 anos 10 meses*
        - Responsável por levantamento de requisitos, análise de processos, gestão de projetos, colaboração com equipe de desenvolvimento, treinamento e suporte, e análise de dados.

        #### Sá Cavalcante · Estagiário de Auditoria em Dados
        *Abr de 2016 - Mar de 2018 · 2 anos*
        - Análise de rotinas do controle interno, controle de faturamento de lojas, coleta e análise de informações de vendas, além de suporte a rotinas administrativas e contábeis.
        """)

elif selection == "Projetos":
    with st.expander("💼 Projetos", expanded=True):  
        st.markdown(""" 
        ### Análise de custo de aluguel
        Análise feita para o curso de análise de dados e inteligência artificial da Universidade Federal do Maranhão.
        [🔗 Ver Projeto](https://dashufmav5-3u2ic5yjy38tmxzjka83ri.streamlit.app/)

        ### Análise de Performance no Instagram
        Criação de um dashboard no Streamlit que compara dados do Instagram de qualquer perfil solicitado com o perfil do usuário e gera um relatório simples. Oferece um relatório mais detalhado mediante compra.
        [🔗 Ver Projeto](https://bn9xtzmakupwckg4aatsjm.streamlit.app/)

        ### Custo de Reuniões
        Um projeto para calcular o custo de reuniões em empresas, focando na redução de custos operacionais e aumento da eficiência.
        [🔗 Ver Projeto](https://www.linkedin.com/in/alan-barros/)

        ### Análise de Conversas do WhatsApp
        Projeto que analisa conversas de grupos do WhatsApp, com a intenção de apresentar insights divertidos sobre as interações.
        [🔗 Ver Projeto](https://www.linkedin.com/in/alan-barros/)
        """)

elif selection == "Contato":
    with st.expander("📧 Contato", expanded=True):
        st.markdown("""
        Estou sempre aberto a novas oportunidades e colaborações! 
        📩 **Email:** alanbarros33f@gmail.com
        📱 **LinkedIn:** [alan-barros](https://www.linkedin.com/in/alan-barros/)
        💼 **GitHub:** [alan-barros](https://github.com/alanbarros33)
        """)
