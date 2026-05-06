import streamlit as st

# 1. Configuración de la página
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

# --- ESTILO CSS PRO ---
style = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;900&display=swap');

    html, body, [data-testid="stAppViewContainer"] {{
        font-family: 'Inter', sans-serif;
        background-color: #050505;
        color: #ffffff;
    }}

    /* SIDEBAR FIJO Y VISIBLE */
    [data-testid="stSidebar"] {{
        background-color: #0a0a0a !important;
        border-right: 1px solid rgba(255,140,0,0.2);
    }}

    /* BANNER HERO (DINÁMICO) */
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

    /* CONTENEDOR PRINCIPAL */
    [data-testid="stAppViewBlockContainer"] {{
        background: rgba(15, 15, 15, 0.95);
        backdrop-filter: blur(20px);
        padding: 40px !important;
        border-radius: 40px;
        border: 1px solid rgba(255, 255, 255, 0.03);
        margin-top: -50px;
    }}

    .orange-text {{
        color: #FF8C00;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 2px;
    }}

    /* TARJETAS DE RECOMENDACIÓN */
    .rec-card {{
        background: linear-gradient(145deg, rgba(255,140,0,0.15) 0%, rgba(10,10,10,1) 100%);
        padding: 30px;
        border-radius: 25px;
        border: 1px solid rgba(255,140,0,0.4);
        margin-bottom: 20px;
    }}

    /* OCULTAR BASURA */
    footer, #MainMenu, [data-testid="stHeader"] {{ visibility: hidden; }}
</style>
"""
st.markdown(style, unsafe_allow_html=True)

# --- BASE DE DATOS COMPLETA ---
db = {
    "Negocios": [
        {"n": "Sede de Moteros", "p": 0.20, "d": "Base para el imperio de drogas."},
        {"n": "Documentos Falsos", "p": 0.65, "d": "Rentabilidad baja, útil para Club Nocturno."},
        {"n": "Laboratorio de Ácido", "p": 0.75, "d": "¡LA MEJOR inversión inicial! Rápido y rentable."},
        {"n": "Fábrica de Dinero", "p": 0.85, "d": "Negocio medio de moteros."},
        {"n": "Oficina de CEO", "p": 1.00, "d": "Acceso a Almacenes y Exportación de vehículos."},
        {"n": "Club Nocturno", "p": 1.10, "d": "Dinero pasivo masivo ($50k/hora)."},
        {"n": "Búnker", "p": 1.16, "d": "Tráfico de armas y mejoras de armamento."},
        {"n": "Hangar", "p": 1.20, "d": "Contrabando aéreo y garaje de aviones."},
        {"n": "Laboratorio de Meta", "p": 1.30, "d": "Muy rentable tras suministros."},
        {"n": "Desguace", "p": 1.62, "d": "Robos de vehículos de lujo semanales."},
        {"n": "Taller de Coches", "p": 1.70, "d": "Contratos tipo 'mini-golpes' y tunning."},
        {"n": "Fábrica de Cocaína", "p": 1.85, "d": "El rey de los negocios de moteros."},
        {"n": "Maquinitas (Arcade)", "p": 1.87, "d": "Indispensable para el Golpe al Casino."},
        {"n": "La Agencia", "p": 2.01, "d": "Misiones de Dr. Dre ($1M asegurado)."},
        {"n": "Kosatka", "p": 2.20, "d": "PRIORIDAD ABSOLUTA. El Golpe a Cayo Perico."}
    ],
    "Vehículos (Autos/Motos)": [
        {"n": "Bati 801", "p": 0.015, "d": "Moto rápida y extremadamente barata."},
        {"n": "Duke O'Death", "p": 0.66, "d": "Blindado pesado para novatos."},
        {"n": "Karin Kuruma (Blindado)", "p": 0.69, "d": "El coche definitivo para misiones."},
        {"n": "Hakuchou Drag", "p": 0.97, "d": "Velocidad pura (compatible con HSW)."},
        {"n": "Nightshark", "p": 1.24, "d": "Tanque personal, resiste 27 misiles."},
        {"n": "Insurgent Pick-Up", "p": 1.79, "d": "Blindaje y ametralladora pesada."},
        {"n": "Western Reever", "p": 1.90, "d": "La moto más rápida del juego."},
        {"n": "Buffalo STX", "p": 2.15, "d": "Tecnología Imani (antimísiles)."},
        {"n": "Pegassi Ignus", "p": 2.76, "d": "Superdeportivo con manejo perfecto."},
        {"n": "Benefactor Krieger", "p": 2.87, "d": "El mejor para ganar carreras."},
        {"n": "Ocelot Virtue", "p": 2.98, "d": "Aceleración eléctrica instantánea."},
        {"n": "Vigilante", "p": 4.75, "d": "El Batmóvil con el turbo más fuerte."},
        {"n": "Deluxo", "p": 5.75, "d": "Coche volador con misiles de alta precisión."},
        {"n": "Oppressor Mk II", "p": 8.00, "d": "La herramienta definitiva de transporte."}
    ],
    "Aéreos (Helis/Aviones)": [
        {"n": "Buzzard", "p": 1.75, "d": "Helicóptero de ataque versátil para CEOs."},
        {"n": "Sparrow", "p": 1.81, "d": "Aparece al lado tuyo. Clave para grindear."},
        {"n": "Savage", "p": 2.59, "d": "Cañón explosivo sin recarga."},
        {"n": "Avenger", "p": 3.45, "d": "Fortaleza con taller de armas y vehículos."},
        {"n": "Akula", "p": 3.70, "d": "Modo sigilo: desaparece del mapa."},
        {"n": "Hydra", "p": 3.99, "d": "Caza con despegue vertical."},
        {"n": "P-996 Lazer", "p": 6.50, "d": "Caza legendario por su agilidad."},
        {"n": "F-160 Raiju", "p": 6.80, "d": "Sigilo + VTOL + La mayor velocidad aérea."}
    ],
    "Propiedades": [
        {"n": "Del Perro Heights", "p": 0.20, "d": "Apartamento para iniciar Golpes."},
        {"n": "Eclipse Towers", "p": 0.50, "d": "Vistas de lujo y garaje de 10 plazas."},
        {"n": "Instalaciones", "p": 1.25, "d": "Necesario para el Golpe del Juicio Final."},
        {"n": "Penthouse Casino", "p": 1.50, "d": "Lujo extremo y misiones de Agatha Baker."},
        {"n": "Garaje de 50 Plazas", "p": 2.74, "d": "Espacio masivo en el centro."},
        {"n": "Yate Galaxy", "p": 6.00, "d": "Símbolo de estatus (poca utilidad)."}
    ]
}

# --- SIDEBAR NAVEGACIÓN ---
with st.sidebar:
    st.image(url_logo, use_container_width=True)
    st.markdown("<h1 class='orange-text'>MENU</h1>", unsafe_allow_html=True)
    nav = st.radio("IR A:", ["🏠 Inicio", "💰 Planificador", "📍 Mapa Interactivo"])
    st.markdown("---")
    st.caption("GTA Plan v3.5 | Elite Series")

# --- LÓGICA DE PÁGINAS ---

if nav == "🏠 Inicio":
    st.markdown(f'<div class="hero-section" style="background-image: linear-gradient(180deg, transparent 0%, #050505 100%), url({url_fondo_banner});"></div>', unsafe_allow_html=True)
    st.markdown(f'<center><img src="{url_logo}" style="width:250px; filter: drop-shadow(0 0 10px #FF8C00);"></center>', unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; padding:20px; font-weight:300; font-size:1.2rem;'>GTA Plan es una herramienta pensada para jugadores de Grand Theft Auto Online que buscan progresar más rápido y tomar mejores decisiones dentro del juego, ya que analiza el dinero que tienes y te recomienda en qué invertirlo de forma inteligente, como negocios, propiedades o vehículos, con el objetivo de maximizar tus ganancias y evitar compras innecesarias; además, sirve como una guía estratégica que te muestra un camino claro para crecer económicamente dentro del juego, ayudándote a pasar de tener poco dinero a construir un imperio rentable de manera más eficiente y organizada.</div>", unsafe_allow_html=True)

elif nav == "💰 Planificador":
    # BANNER IGUAL AL DEL MENÚ (COMO PEDISTE)
    st.markdown(f'<div class="hero-section" style="background-image: linear-gradient(180deg, transparent 0%, #050505 100%), url({url_planificador_banner});"></div>', unsafe_allow_html=True)
    
    st.markdown("<h2 class='orange-text'>PLANIFICADOR ELITE</h2>", unsafe_allow_html=True)
    presupuesto = st.number_input("¿De cuántos millones dispones? (M)", min_value=0.0, value=2.2, step=0.1)
    
    tabs = st.tabs(list(db.keys()))
    
    for i, categoria in enumerate(db.keys()):
        with tabs[i]:
            opciones = [item for item in db[categoria] if item["p"] <= presupuesto]
            
            if opciones:
                # El más recomendado (el más caro que te alcance, asumiendo que es el mejor)
                mejor = max(opciones, key=lambda x: x["p"])
                
                st.markdown(f"""
                <div class="rec-card">
                    <h4 style="color:#FF8C00; margin:0;">💎 RECOMENDACIÓN PREMIUM:</h4>
                    <h2 style="margin:10px 0;">{mejor['n']}</h2>
                    <p style="font-size:1.5rem; font-weight:bold; color:white;">COSTO: ${mejor['p']:.2f}M</p>
                    <p style="color:#aaa;">{mejor['d']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                with st.expander("VER TODAS LAS OPCIONES DISPONIBLES"):
                    for opt in sorted(opciones, key=lambda x: x["p"], reverse=True):
                        st.write(f"✅ **{opt['n']}** — ${opt['p']:.2f}M")
            else:
                st.error("⚠️ No hay opciones disponibles con ese presupuesto en esta categoría.")

elif nav == "📍 Mapa Interactivo":
    st.markdown("<h2 class='orange-text'>MAPA DE LOS SANTOS</h2>", unsafe_allow_html=True)
    st.markdown("""
        <a href="https://gta-5-map.com" target="_blank" style="text-decoration:none;">
            <div style="background: #FF8C00; color: black; padding: 20px; border-radius: 20px; text-align: center; font-weight: 900; font-size: 1.5rem;">
                LANZAR MAP GENIE 📍
            </div>
        </a>
    """, unsafe_allow_html=True)

st.markdown("<br><br><center style='color:#333;'>GTA PLAN © 2026</center>", unsafe_allow_html=True)