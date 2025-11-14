# Utilise une image légère de Streamlit
FROM python:3.10-slim

WORKDIR /app

# Copie du code
COPY app.py /app/

# Installation des dépendances
RUN pip install streamlit requests

# Exposition du port Streamlit
EXPOSE 8501

# Commande de lancement
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
