import streamlit as st

# Configuración de la web
st.set_page_config(page_title="GTA plan", page_icon="💸", layout="wide")

# --- URLs de Imágenes Actualizadas ---
url_logo = "https://i.ibb.co/zW79cKSM/Whats-App-Image-2026-05-03-at-8-00-53-PM-removebg-preview.png"
url_fondo_banner = "https://i.ibb.co/bjYpX6GL/Gemini-Generated-Image-ykn7hwykn7hwykn7.png"
url_fondo_palmeras = "https://i.ibb.co/FL0rByyC/Picsart-26-05-03-21-26-20-333.jpg"

# --- ESTILO CSS AVANZADO ---
page_bg_img = f"""
<style>
/* 1. FONDO DEL BANNER SUPERIOR (CIUDAD) */
[data-testid="stAppViewContainer"] {{
    background-image: url("{url_fondo_banner}");
    background-size: 100% 550px; 
    background-position: top center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-color: #000;
}}

/* 2. FONDO DE LA SEGUNDA INTERFAZ (PALMERAS) */
[data-testid="stAppViewBlockContainer"] {{
    background-image: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.2)), url("{url_fondo_palmeras}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    margin-top: 420px; 
    padding: 50px 60px;
    border-radius: 40px 40px 0 0; 
    border-top: 4px solid #FF8C00; 
    box-shadow: 0px -20px 40px rgba(0,0,0,0.9);
}}

/* Transparencia en el encabezado */
[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

/* Tarjetas con Glassmorphism */
div.stAlert {{
    border-radius: 20px;
    border: 1px solid rgba(255, 140, 0, 0.5);
    background-color: rgba(0, 0, 0, 0.85) !important;
    backdrop-filter: blur(15px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.8);
    color: white;
}}

/* Ajustes de texto */
h1, h2, h3, h4, p, span, li {{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: white;
    text-shadow: 2px 2px 10px rgba(0,0,0,1);
}}

/* Pestañas color naranja GTA */
.stTabs [data-baseweb="tab-list"] button {{
    color: #bbb;
    font-size: 18px;
}}
.stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {{
    color: #FF8C00 !important; 
    font-weight: 900;
    border-bottom: 4px solid #FF8C00 !important;
}}

/* Caja flotante (Logo y Presupuesto) */
.floating-overlay {{
    background-color: rgba(0,0,0,0.8);
    padding: 35px;
    border-radius: 25px;
    margin-top: -420px; 
    text-align: center;
    border: 2px solid rgba(255, 140, 0, 0.6);
    backdrop-filter: blur(12px);
    box-shadow: 0 15px 45px rgba(0,0,0,0.9);
}}

[data-testid="stToolbar"] {{
    visibility: hidden;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# --- BASE DE DATOS COMPLETA ---
db = {
    "Negocios": [
        {"n": "Sede de Moteros", "p": 0.20, "d": "Base necesaria para negocios de drogas."},
        {"n": "Documentos Falsos (MC)", "p": 0.65, "d": "El menos rentable, pero sirve para el Club Nocturno."},
        {"n": "Laboratorio de Ácido", "p": 0.75, "d": "Mejor inversión inicial. Dinero pasivo rápido."},
        {"n": "Fábrica de Dinero (MC)", "p": 0.85, "d": "Negocio medio de moteros."},
        {"n": "Oficina de CEO", "p": 1.00, "d": "Permite comprar almacenes de cajas y coches."},
        {"n": "Club Nocturno", "p": 1.10, "d": "Genera $50k cada 48 min (pasivo total)."},
        {"n": "Laboratorio de Meta (MC)", "p": 1.30, "d": "Segundo mejor negocio de moteros."},
        {"n": "Hangar", "p": 1.20, "d": "Contrabando aéreo y guarda tus aviones."},
        {"n": "Búnker", "p": 1.16, "d": "Investigación de armas y dinero pasivo."},
        {"n": "Desguace", "p": 1.62, "d": "Robos de vehículos de lujo semanales."},
        {"n": "Taller de Coches", "p": 1.70, "d": "Contratos rápidos y tuneo con descuento."},
        {"n": "Fábrica de Cocaína (MC)", "p": 1.85, "d": "El mejor negocio de moteros."},
        {"n": "Maquinitas (Arcade)", "p": 1.87, "d": "Necesario para el Golpe al Casino."},
        {"n": "La Agencia", "p": 2.01, "d": "Contrato de Dr. Dre ($1M) y misiones de Franklin."},
        {"n": "Kosatka", "p": 2.20, "d": "¡PRIORIDAD! Abre Cayo Perico (dinero infinito)."}
    ],
    "Autos": [
        {"n": "Duke O'Death", "p": 0.66, "d": "Coche blindado potente y rápido."},
        {"n": "Karin Kuruma Blindado", "p": 0.69, "d": "Indispensable para misiones (a prueba de balas)."},
        {"n": "Nightshark", "p": 1.24, "d": "Resiste 27 misiles. Ideal para defenderse de MK2."},
        {"n": "Insurgent Pick-Up", "p": 1.79, "d": "Camioneta blindada con torreta."},
        {"n": "Buffalo STX", "p": 2.15, "d": "Tecnología Imani (Inhibidor de misiles)."},
        {"n": "Pegassi Ignus", "p": 2.76, "d": "Súper auto con gran manejo."},
        {"n": "Benefactor Krieger", "p": 2.87, "d": "El más rápido en circuitos."},
        {"n": "Ocelot Virtue", "p": 2.98, "d": "Aceleración eléctrica extrema."},
        {"n": "Vigilante (Batmobile)", "p": 4.75, "d": "El coche con el turbo más potente."},
        {"n": "Deluxo", "p": 5.75, "d": "Coche volador con misiles precisos."}
    ],
    "Motos": [
        {"n": "Sanchez", "p": 0.008, "d": "Barata y excelente para el campo."},
        {"n": "Bati 801", "p": 0.015, "d": "Sigue siendo de las mejores del juego."},
        {"n": "Hakuchou Drag", "p": 0.97, "d": "Increíble velocidad punta (HSW disponible)."},
        {"n": "Western Reever", "p": 1.90, "d": "La moto más rápida en velocidad final."},
        {"n": "Oppressor Mk I", "p": 3.48, "d": "Moto voladora con planeo."},
        {"n": "Oppressor Mk II", "p": 8.00, "d": "La mejor para moverse por el mapa."}
    ],
    "Helis y Aviones": [
        {"n": "Buzzard", "p": 1.75, "d": "Helicóptero de combate básico para CEO."},
        {"n": "Sparrow", "p": 1.81, "d": "Aparece al lado tuyo. Ideal para grindear."},
        {"n": "Savage", "p": 2.59, "d": "Cañón explosivo devastador."},
        {"n": "Avenger", "p": 3.45, "d": "Fortaleza voladora y taller de vehículos."},
        {"n": "Akula", "p": 3.70, "d": "Sigilo total: desapareces del radar."},
        {"n": "Hydra", "p": 3.99, "d": "Caza con despegue vertical (VTOL)."},
        {"n": "P-996 Lazer", "p": 6.50, "d": "El caza más ágil de los clásicos."},
        {"n": "F-160 Raiju", "p": 6.80, "d": "Sigilo + VTOL + Velocidad récord."}
    ],
    "Casas y Otros": [
        {"n": "Apto. Del Perro Heights", "p": 0.20, "d": "El más barato para misiones de golpes."},
        {"n": "Eclipse Towers", "p": 0.50, "d": "Vistas al centro de la ciudad."},
        {"n": "Instalaciones", "p": 1.25, "d": "Para el Golpe del Juicio Final."},
        {"n": "Penthouse del Casino", "p": 1.50, "d": "Lujo, misiones y bar privado."},
        {"n": "Longfin (Barco)", "p": 2.12, "d": "El mejor barco para entrar a Cayo Perico."},
        {"n": "Garaje 50 Plazas", "p": 2.74, "d": "El paraíso del coleccionista."},
        {"n": "Yate Galaxy", "p": 6.00, "d": "Lujo extremo sin mucha utilidad."}
    ]
}

# --- BARRA LATERAL ---
st.sidebar.markdown("### Ajustes de Plan")
margen_ayuda = st.sidebar.slider("Flexibilidad de presupuesto (%)", 0, 20, 5)

# --- CONTENIDO ---
c1, c2, c3 = st.columns([1, 1.5, 1])

with c2:
    st.markdown('<div class="floating-overlay">', unsafe_allow_html=True)
    st.image(url_logo, use_container_width=True)
    presupuesto = st.number_input("¿Cuántos Millones tienes?", min_value=0.0, value=2.2, step=0.1)
    st.markdown('</div>', unsafe_allow_html=True)

tabs = st.tabs([f" {cat}" for cat in db.keys()])

for i, categoria in enumerate(db.keys()):
    with tabs[i]:
        items = db[categoria]
        limite = presupuesto * (1 + (margen_ayuda/100))
        opciones = [item for item in items if item["p"] <= limite]
        
        if opciones:
            mejor = max(opciones, key=lambda x: x["p"])
            st.markdown(f"#### 🏆 Sugerencia estrella: **{mejor['n']}**")
            
            if mejor['p'] <= presupuesto:
                st.success(f"Precio: ${mejor['p']:.2f}M — ¡Adquisición inmediata!")
            else:
                st.warning(f"Precio: ${mejor['p']:.2f}M — Ajustado con flexibilidad.")
            
            st.markdown(f"> {mejor['d']}")
            
            with st.expander("Explorar alternativas"):
                for opt in sorted(opciones, key=lambda x: x["p"], reverse=True):
                    if opt != mejor:
                        st.write(f"• **{opt['n']}** — ${opt['p']:.2f}M")
        else:
            st.error("Presupuesto insuficiente para esta categoría.")

st.markdown("<br><hr>", unsafe_allow_html=True)
st.caption("GTA Plan - Base de datos completa.")