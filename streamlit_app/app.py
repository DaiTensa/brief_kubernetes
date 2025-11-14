import streamlit as st
import requests

# nom du service Kubernetes
API_URL = "http://api-svc"  

st.set_page_config(page_title="Clients App", layout="wide")

st.title("📋 Gestion des Clients")

# --- Vérification de santé ---
try:
    health = requests.get(f"{API_URL}/health").json()
    st.success("✅ API connectée")
except Exception as e:
    st.error(f"❌ Impossible de se connecter à l’API : {e}")

# --- Liste des clients ---
st.header("Liste des clients")
if st.button("🔄 Rafraîchir"):
    try:
        resp = requests.get(f"{API_URL}/clients")
        if resp.status_code == 200:
            clients = resp.json()
            if clients:
                st.table(clients)
            else:
                st.info("Aucun client trouvé.")
        else:
            st.error(f"Erreur : {resp.status_code}")
    except Exception as e:
        st.error(f"Erreur : {e}")

# --- Ajouter un client ---
st.header("Ajouter un client")
with st.form("add_client_form"):
    first_name = st.text_input("Prénom")
    last_name = st.text_input("Nom")
    email = st.text_input("Email")
    submitted = st.form_submit_button("Ajouter")
    if submitted:
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        }
        resp = requests.post(f"{API_URL}/clients", json=payload)
        if resp.status_code == 201:
            st.success("Client ajouté avec succès ✅")
        elif resp.status_code == 409:
            st.warning("⚠️ Email déjà existant")
        else:
            st.error(f"Erreur ({resp.status_code}) : {resp.text}")


# --- Supprimer un client ---
st.header("Supprimer un client")
client_id = st.number_input("ID du client à supprimer", min_value=1, step=1)
if st.button("🗑️ Supprimer"):
    resp = requests.delete(f"{API_URL}/clients/{client_id}")
    if resp.status_code == 204:
        st.success("Client supprimé ✅")
    elif resp.status_code == 404:
        st.warning("Client introuvable")
    else:
        st.error(f"Erreur : {resp.status_code}")
