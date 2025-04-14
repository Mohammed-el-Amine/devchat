#!/bin/bash

# Vérifier si le dossier dev-chat existe
if [ ! -d "/home/amine/Bureau/devchat/dev-chat" ]; then
    # Si le dossier n'existe pas, créer l'environnement virtuel
    python3 -m venv /home/amine/Bureau/devchat/dev-chat
fi

# Activer l'environnement virtuel
source /home/amine/Bureau/devchat/dev-chat/bin/activate

# Lancer le script Python dans un nouveau terminal GNOME
#gnome-terminal -- bash -c "python3 /home/amine/Bureau/devchat/devchat.py; exec bash"
python3 /home/amine/Bureau/devchat/devchat.py
