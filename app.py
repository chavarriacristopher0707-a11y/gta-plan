import streamlit as st

# 1. Configuración de la página (Sidebar siempre abierto al inicio)
st.set_page_config(
    page_title="GTA Plan", 
    page_icon="💸", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ENLACES DE IMAGEN ---
url_fondo_banner = "https://i.ibb.co/bjYpX6GL/Gemini-Generated-Image-ykn7hwykn7hwykn7.png"
url_logo = "https://i.ibb.co/zW79cKSM/Whats-App-Image-2026-05-03-at-8-00-53-PM-removebg-preview.png"
url_planificador_banner = "https://i.ibb.co/jvM1n1zB/Gemini-Generated-Image-7uheox7uheox7uhe.png"

# --- ESTILO CSS ELITE (REPARACIÓN DE RAYITAS Y DISEÑO) ---
style = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;900&display=swap');

    html, body, [data-testid="stAppViewContainer"] {{
        font-family: 'Inter', sans-serif;
        background-color: #050505;
        color: #ffffff;
    }}

    /* BOTÓN DE MENÚ (RAYITAS) SIEMPRE VISIBLE Y NARANJA */
    header[data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0) !important;
        visibility: visible !important;
    }}

    button[kind="headerNoPadding"] {{
        color: #FF8C00 !important;
        background-color: rgba(255, 140, 0, 0.1) !important;
        border-radius: 10px !important;
        padding: 5px !important;
    }}

    /* CONTENEDOR PRINCIPAL */
    [data-testid="stAppViewBlockContainer"] {{
        background: rgba(15, 15, 15, 0.95);
        backdrop-filter: blur(20px);
        padding: 40px !important;
        border-radius: 40px;
        border: 1px solid rgba(255, 255, 255, 0.03);
        margin-top: -80px;
        box-shadow: 0 50px 100px rgba(0,0,0,0.9);
    }}

    /* BANNER HERO */
    .hero-section {{
        background-size: cover;
        background-position: center center;
        height: 450px;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end;
        border-radius: 0 0 50px 50px;
        padding-bottom: 40px;
        margin-bottom: 20px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.8);
    }}

    .orange-text {{
        color: #FF8C00;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 2px;
    }}

    .rec-card {{
        background: linear-gradient(145deg, rgba(255,140,0,0.2) 0%, rgba(10,10,10,1) 100%);
        padding: 30px;
        border-radius: 25px;
        border: 1px solid rgba(255,140,0,0.4);
        margin-bottom: 20px;
    }}

    footer, #MainMenu {{ visibility: hidden; }}
</style>
"""
st.markdown(style, unsafe_allow_html=True)

# --- BASE DE DATOS MASIVA ---
db = {
    "Negocios": [
        {"n": "Sede de Moteros", "p": 0.20, "d": "Base necesaria para negocios de drogas."},
        {"n": "Documentos Falsos", "p": 0.65, "d": "Baja rentabilidad, pero suma al Club Nocturno."},
        {"n": "Laboratorio de Ácido", "p": 0.75, "d": "¡EL MEJOR! Muy rentable y misiones fáciles."},
        {"n": "Fábrica de Dinero", "p": 0.85, "d": "Negocio básico de moteros."},
        {"n": "Oficina de CEO", "p": 1.00, "d": "Permite ser Jefe y comprar almacenes."},
        {"n": "Club Nocturno", "p": 1.10, "d": "El mejor dinero pasivo del juego ($50k/hora)."},
        {"n": "Búnker", "p": 1.16, "d": "Tráfico de armas y mejoras de armamento."},
        {"n": "Hangar", "p": 1.20, "d": "Contrabando y garaje para tus naves."},
        {"n": "Laboratorio de Meta", "p": 1.30, "d": "Segundo mejor negocio de moteros."},
        {"n": "Desguace", "p": 1.62, "d": "Robos de coches de lujo semanales."},
        {"n": "Taller de Coches", "p": 1.70, "d": "Contratos rápidos y tuneos de clientes."},
        {"n": "Fábrica de Cocaína", "p": 1.85, "d": "El negocio de moteros más lucrativo."},
        {"n": "Maquinitas (Arcade)", "p": 1.87, "d": "Centro de mando para el Golpe al Casino."},
        {"n": "La Agencia", "p": 2.01, "d": "Contratos de Dr. Dre ($1M) y tecnología Imani."},
        {"n": "Kosatka", "p": 2.20, "d": "¡PRIORIDAD 1! Desbloquea Cayo Perico."},
        {"n": "Salvage Yard", "p": 2.60, "d": "Negocio de desmantelamiento de piezas de lujo."}
    ],
    "Carros": [
        {"n": "Duke O'Death", "p": 0.66, "d": "Blindado pesado muy resistente."},
        {"n": "Karin Kuruma (Blindado)", "p": 0.69, "d": "Rey de las misiones contra NPCs."},
        {"n": "Nightshark", "p": 1.24, "d": "Indispensable contra la Oppressor Mk2."},
        {"n": "Insurgent Pick-Up", "p": 1.79, "d": "Camioneta blindada con torreta pesada."},
        {"n": "Buffalo STX", "p": 2.15, "d": "El mejor coche con tecnología Imani."},
        {"n": "Pegassi Ignus", "p": 2.76, "d": "Superdeportivo con tracción total increíble."},
        {"n": "Benefactor Krieger", "p": 2.87, "d": "Dominador en carreras de circuitos."},
        {"n": "Ocelot Virtue", "p": 2.98, "d": "Eléctrico con aceleración de infarto."},
        {"n": "Toreador", "p": 3.60, "d": "Coche anfibio con misiles y turbo infinito."},
        {"n": "Vigilante", "p": 4.75, "d": "Turbo masivo y misiles de gran alcance."},
        {"n": "Deluxo", "p": 5.75, "d": "Coche volador ideal para misiones diarias."}
    ],
    "Motos": [
        {"n": "Sanchez", "p": 0.008, "d": "La reina del campo y la montaña."},
        {"n": "Bati 801", "p": 0.015, "d": "La mejor calidad-precio del juego."},
        {"n": "Hakuchou Drag", "p": 0.97, "d": "Velocidad punta brutal (Mejora HSW)."},
        {"n": "Western Reever", "p": 1.90, "d": "Moto más rápida en velocidad final."},
        {"n": "Shotaro", "p": 2.22, "d": "La moto de 'Tron' con manejo perfecto."},
        {"n": "Oppressor Mk I", "p": 3.48, "d": "Moto voladora con planeo."},
        {"n": "Oppressor Mk II", "p": 8.00, "d": "La herramienta más eficiente para grindear."}
    ],
    "Helicópteros": [
        {"n": "Buzzard", "p": 1.75, "d": "Helicóptero de combate básico de todo CEO."},
        {"n": "Sparrow", "p": 1.81, "d": "Sale del Kosatka, el más rápido para moverse."},
        {"n": "Savage", "p": 2.59, "d": "Cañón explosivo de muerte instantánea."},
        {"n": "Akula", "p": 3.70, "d": "Helicóptero invisible en el radar (Modo Sigilo)."},
        {"n": "Hunter", "p": 4.10, "d": "Fortaleza aérea con misiles y contramedidas."}
    ],
    "Aviones": [
        {"n": "Hydra", "p": 3.99, "d": "Caza VTOL clásico con cañón explosivo."},
        {"n": "Avenger", "p": 3.45, "d": "Centro de operaciones volador ultrarresistente."},
        {"n": "B-11 Strikeforce", "p": 3.80, "d": "Avión de ataque pesado muy ágil."},
        {"n": "P-996 Lazer", "p": 6.50, "d": "El caza con mejor movilidad de combate."},
        {"n": "F-160 Raiju", "p": 6.80, "d": "El avión más rápido y potente del juego."}
    ],
    "Propiedades": [
        {"n": "Apto. Del Perro Heights", "p": 0.20, "d": "Base barata para los primeros golpes."},
        {"n": "Eclipse Towers", "p": 0.50, "d": "Lujo máximo y mejores vistas de la ciudad."},
        {"n": "Instalaciones", "p": 1.25, "d": "Necesarias para el Golpe del Juicio Final."},
        {"n": "Penthouse del Casino", "p": 1.50, "d": "Servicios VIP y misiones exclusivas."},
        {"n": "Garaje 50 Plazas", "p": 2.74, "d": "El sueño de cualquier coleccionista."},
        {"n": "Yate Galaxy", "p": 6.00, "d": "El capricho más caro de Los Santos."}
    ]
}

# --- NAVEGACIÓN ---
with st.sidebar:
    st.image(url_logo, use_container_width=True)
    st.markdown("<h1 class='orange-text'>MENU</h1>", unsafe_allow_html=True)
    nav = st.radio("IR A:", ["🏠 Inicio", "💰 Planificador", "📍 Mapa Interactivo"])
    st.markdown("---")
    st.info("Usa las rayitas naranjas arriba a la izquierda si el menú se oculta.")

# --- PÁGINAS ---
if nav == "🏠 Inicio":
    st.markdown(f'<div class="hero-section" style="background-image: linear-gradient(180deg, transparent 0%, #050505 100%), url({url_fondo_banner});"></div>', unsafe_allow_html=True)
    st.markdown(f'<center><img src="{url_logo}" style="width:250px; filter: drop-shadow(0 0 10px #FF8C00);"></center>', unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; padding:20px; font-weight:300;'>GTA Plan es una herramienta táctica diseñada para maximizar tus ganancias en Los Santos.</div>", unsafe_allow_html=True)

elif nav == "💰 Planificador":
    # Banner de Planificación HD
    st.markdown(f'<div class="hero-section" style="background-image: linear-gradient(180deg, transparent 0%, #050505 100%), url({url_planificador_banner});"></div>', unsafe_allow_html=True)
    st.markdown("<h2 class='orange-text'>PLANIFICADOR ELITE</h2>", unsafe_allow_html=True)
    presupuesto = st.number_input("¿Cuántos millones tienes? (M)", min_value=0.0, value=2.2, step=0.1)
    
    tabs = st.tabs(list(db.keys()))
    for i, cat in enumerate(db.keys()):
        with tabs[i]:
            opciones = [item for item in db[cat] if item["p"] <= presupuesto]
            if opciones:
                mejor = max(opciones, key=lambda x: x["p"])
                st.markdown(f"""
                <div class="rec-card">
                    <h4 style="color:#FF8C00; margin:0;">⭐ RECOMENDACIÓN PREMIUM:</h4>
                    <h2 style="margin:10px 0;">{mejor['n']}</h2>
                    <p style="font-size:1.8rem; font-weight:900; color:white;">${mejor['p']:.2f}M</p>
                    <p style="color:#bbb;">{mejor['d']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                with st.expander("VER OTRAS OPCIONES DISPONIBLES"):
                    for opt in sorted(opciones, key=lambda x: x["p"], reverse=True):
                        if opt != mejor:
                            st.write(f"✅ **{opt['n']}** — ${opt['p']:.2f}M")
            else:
                st.warning("⚠️ No tienes presupuesto suficiente para esta categoría.")

elif nav == "📍 Mapa Interactivo":
    st.markdown("<h2 class='orange-text'>MAPA DE LOS SANTOS</h2>", unsafe_allow_html=True)
    st.markdown('<a href="https://gta-5-map.com" target="_blank" style="text-decoration:none;"><div style="background:#FF8C00; color:black; padding:20px; border-radius:20px; text-align:center; font-weight:900; font-size:1.5rem;">ABRIR MAP GENIE 📍</div></a>', unsafe_allow_html=True)

st.markdown("<br><br><center style='color:#333;'>GTA PLAN © 2026</center>", unsafe_allow_html=True)
