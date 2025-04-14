#!/bin/bash

# Définir les chemins
PROJECT_DIR="$HOME/Bureau/devchat"
VENV_DIR="$PROJECT_DIR/dev-chat"
PYTHON_SCRIPT="$PROJECT_DIR/devchat.py"

# Liste des dépendances requises
REQUIRED_PACKAGES=("llama-index" "llama-index-llms-ollama" "rich")

# Fonction pour vérifier si toutes les dépendances sont installées
check_dependencies() {
    for package in "${REQUIRED_PACKAGES[@]}"; do
        if ! "$VENV_DIR/bin/pip" show "$package" &> /dev/null; then
            return 1
        fi
    done
    return 0
}

# Créer l'environnement virtuel si nécessaire
if [ ! -d "$VENV_DIR" ]; then
    echo "[*] Environnement virtuel non trouvé. Création..."
    python3 -m venv "$VENV_DIR"
fi

# Activer l'environnement
source "$VENV_DIR/bin/activate"

# Vérifier et installer les dépendances si besoin
if check_dependencies; then
    echo "[*] Dépendances déjà installées. Lancement de l'application..."
else
    echo "[*] Installation des dépendances manquantes..."
    pip install --upgrade pip
    pip install "${REQUIRED_PACKAGES[@]}"
fi

# Lancer le script
echo "[*] Exécution de devchat.py..."
python3 "$PYTHON_SCRIPT"

