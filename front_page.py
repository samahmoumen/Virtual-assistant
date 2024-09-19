import streamlit as st
from app import main as app
from form_recup import main as form_recup
from form_reparation import main as form_reparation
from form_ordre import main as form_ordre
from form_stage import main as form_stage
from streamlit_app import email_generator

# Configuration de la page
st.set_page_config(page_title="Page Principale", page_icon=":sparkles:", layout="wide")
col1, col2 = st.columns([2, 100])

with col1:
    st.image("C:/Users/Lenovo/app-starter-kit/myenv/logo.jpg", width=150)

with col2:
    st.markdown('<div class="welcome-message" style="font-size: 24px; font-weight: bold; color: #004080; margin: 20px 0;">Bienvenue sur notre plateforme d\'assistance administrative virtuelle</div>', unsafe_allow_html=True)


# Style CSS amélioré pour une mise en page sophistiquée
st.markdown("""
    <style>
    body {
        background-color: #003d7a; /* Couleur de fond bleu très foncé */
        color: #ffffff; 
        font-family: 'Arial', sans-serif;
        margin: 0;
        padding: 0;
    }
    .nav-wrapper {
        position: fixed;
        top: 0;
        width: 100%;
        background-color: #FFA500; /* Couleur orange de la barre de navigation */
        z-index: 1000;
        border-bottom: 10px solid #ddd;
    }
    .nav-bar {
        display: flex;
        justify-content: center;
        padding: 10px;
    }
    .nav-button {
        margin: 0 15px;
        font-size: 18px;
        font-weight: bold;
        color: black;
        text-decoration: none;
        cursor: pointer;
        padding: 10px 20px;
        border-radius: 5px;
        background-color: #FFA500; /* Couleur orange des boutons */
        transition: background-color 0.3s, transform 0.3s;
    }
    .nav-button:hover {
        background-color: #003d7a;
        transform: scale(1.05);
        color: #FFA500;
    }
    .nav-button:active {
        background-color: #FFA500;
        transform: scale(0.95);
        color: #FFA500;
    }
    .section-title {
        font-size: 28px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 20px;
        color: #004080;
        text-align: center;
    }
    .contact-info {
        list-style-type: none;
        padding: 0;
        text-align: center;
        font-size: 18px;
    }
    .contact-info li {
        margin: 10px 0;
    }
    .social-icons {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .social-icons a {
        margin: 0 10px;
        font-size: 24px;
        color: white;
        text-decoration: none;
        transition: color 0.3s, transform 0.3s;
    }
    .social-icons a:hover {
        color: #003060;
        transform: scale(1.1);
    }
    .welcome-message {
        font-size: 24px;
        font-weight: bold;
        color: #004080;
        text-align: center;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    .footer {
        background-color: #FFA500;
        color: white;
        text-align: center;
        padding: 10px;
        position: fixed;
        width: 100%;
        bottom: 0;
        font-size: 14px;
        border-top: 1px solid #444;
    }
    </style>
    """, unsafe_allow_html=True)

# Barre de navigation avec fond orange fixe
st.markdown('<div class="nav-wrapper">', unsafe_allow_html=True)
st.markdown('<div class="nav-bar">', unsafe_allow_html=True)

# Variables de session pour la navigation
if 'section' not in st.session_state:
    st.session_state['section'] = 'documents'

# Navigation horizontale
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
    if st.button('Documents', key='docs', use_container_width=True):
        st.session_state['section'] = 'documents'
with col2:
    if st.button('Générateur d\'emails', key='email-gen', use_container_width=True):
        st.session_state['section'] = 'email-generator'
with col3:
    if st.button('Contactez-nous', key='contact', use_container_width=True):
        st.session_state['section'] = 'contactez-nous'
with col4:
    if st.button('Qui nous sommes', key='about', use_container_width=True):
        st.session_state['section'] = 'qui-nous-sommes'

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Contenu de la page
st.markdown('<div class="page-container" style="margin-top: 10px;">', unsafe_allow_html=True)  # Add margin-top to avoid content overlapping with navbar


# Vérifier l'état de la section actuelle
section = st.session_state['section']

# Section Documents
if section == "documents":
    st.markdown('<div class="section-title">Documents</div>', unsafe_allow_html=True)
    doc_page = st.selectbox("Choisissez un formulaire", [
        "Formulaire du départ en Congé", 
        "Formulaire Récupération pièces sur matériel", 
        "Formulaire de passer matériel sous Réparation",
        "Ordre de Mission",
        "Attestation de Stage"
    ])
    if doc_page == "Formulaire du départ en Congé":
        app()
    elif doc_page == "Formulaire Récupération pièces sur matériel":
        form_recup()
    elif doc_page == "Formulaire de passer matériel sous Réparation":
        form_reparation()
    elif doc_page == "Ordre de Mission":
        form_ordre()
    elif doc_page == "Attestation de Stage":
        form_stage()

# Section Générateur d'emails
elif section == "email-generator":
    st.markdown('<div class="section-title">Générateur d\'emails</div>', unsafe_allow_html=True)
    email_generator()

# Section Contactez-nous
elif section == "contactez-nous":
    st.markdown('<div class="section-title">Contactez-nous</div>', unsafe_allow_html=True)
    st.markdown("""
        <ul class="contact-info">
            <li>Email : contact@example.com</li>
            <li>Téléphone : +123 456 7890</li>
            <li>
                Suivez-nous sur les réseaux sociaux :
                <div class="social-icons">
                    <a href="https://facebook.com" target="_blank">F</a>
                    <a href="https://whatsapp.com" target="_blank">W</a>
                    <a href="https://instagram.com" target="_blank">I</a>
                </div>
            </li>
        </ul>
        """, unsafe_allow_html=True)

# Section Qui nous sommes
elif section == "qui-nous-sommes":
    st.markdown('<div class="section-title">Qui sommes nous</div>', unsafe_allow_html=True)
    st.markdown("""
        <p>Nous sommes une entreprise dédiée à fournir des solutions administratives de haute qualité. 
        Notre équipe est composée de professionnels expérimentés dans divers domaines pour vous assister dans vos besoins quotidiens.</p>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Pied de page
st.markdown('<div class="footer">© 2024 FORGES DE BAZAS. All rights reserved.</div>', unsafe_allow_html=True)
