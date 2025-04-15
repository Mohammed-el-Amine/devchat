#!/bin/bash

PROJECT_DIR="$HOME/Bureau/devchat"
VENV_DIR="$PROJECT_DIR/dev-chat"
PYTHON_SCRIPT="$PROJECT_DIR/devchat.py"

REQUIRED_PACKAGES=("llama-index" "llama-index-llms-ollama" "rich" "mysql-connector-python" "python-dotenv")

check_dependencies() {
    for package in "${REQUIRED_PACKAGES[@]}"; do
        if ! "$VENV_DIR/bin/pip" show "$package" &> /dev/null; then
            return 1
        fi
    done
    return 0
}

if [ ! -d "$VENV_DIR" ]; then
    echo "[*] Environnement virtuel non trouvé. Création..."
    python3 -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"

if check_dependencies; then
    echo "[*] Dépendances déjà installées. Lancement de l'application..."
else
    echo "[*] Installation des dépendances manquantes..."
    pip install --upgrade pip
    pip install "${REQUIRED_PACKAGES[@]}"
fi

clear

echo "[*] Exécution de devchat.py..."
gnome-terminal -- bash -c "python3 /home/amine/Bureau/devchat/devchat.py; exec bash"
