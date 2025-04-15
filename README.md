
# DevChat CLI – Spécialiser Ollama pour le Développement

## 🎯 Objectif

Créer un petit **chat CLI local** spécialisé pour le développement avec un modèle Ollama local (`deepseek-coder:6.7b`).

---

## 🛠️ Dépendances à installer

```bash
curl -fsSL https://ollama.com/install.sh | sh
python3 -m venv dev-chat
source dev-chat/bin/activate
pip install --upgrade pip
pip install llama-index llama-index-llms-ollama rich python-dotenv mysql-connector-python
```

---

## 📁 Structure du projet recommandée

```
ton-projet/
├── devchat.py
├── lancement.sh
├── .env.example                  # renomé par .env et remmplir les informations
├── create_chat_history_db.sql
├── README.md
├── wrapper.c
├── lancement                     # éxécutable
├── .gitignore
└── code_docs/
    ├── DOCKER.md
    ├── react_patterns.md
    ├── backend_tips.md
    ├── cheatsheet.txt
    └── ...
```

---

## 🧠 Description du script

- Connecte ton modèle local via `ollama`
- Utilise un prompt système spécialisé développeur
- Permet de discuter directement via terminal
- Sauvegarde tout les échange en base de donnée

---

## ✅ Lancement du chat

```bash
python3 devchat.py
# OU
# double clique sur lancement
# OU
./lancement.sh
# OU clique droit sur lancement.sh ---> éxécuter comme un programme ENJOY :)
```

---

## 💬 Exemples de questions

- "Comment configurer Docker pour un projet Node.js ?"
- "Quel est un bon pattern pour une API REST Express ?"
- "Comment organiser un projet React avec Redux Toolkit ?"
- "Donne un exemple de middleware en Express"

---

## 🚀 Options possibles à ajouter

- Interface graphique (`textual`, `gradio`, `streamlit`)
- Historique de conversation sauvegardé
- Analyse directe de code avec coloration syntaxique

---

## 🗄️ Créer la base de données et les tables nécessaires

1. **Téléchargez le fichier SQL** [ici](create_chat_history_db.sql).

2. **Connectez-vous à MySQL** en utilisant la commande suivante (en remplaçant `user` par votre utilisateur MySQL) :

    ```bash
    mysql -u user -p
    ```

    Il vous sera demandé de fournir le mot de passe associé à votre utilisateur MySQL.

3. **Créez la base de données (si elle n'existe pas déjà)** :

    ```sql
    CREATE DATABASE chat_history;
    ```

4. **Sélectionnez la base de données** :

    ```sql
    USE chat_history;
    ```

5. **Exécutez le fichier SQL** pour créer les tables. Remplacez `/chemin/vers/le/fichier/create_chat_history_db.sql` par le chemin complet du fichier téléchargé :

    ```sql
    source /chemin/vers/le/fichier/create_chat_history_db.sql;
    ```

6. **Vérifiez que les tables sont créées** :

    ```sql
    SHOW TABLES;
    ```

7. **Quittez MySQL** lorsque vous avez terminé :

    ```sql
    exit;
    ```
Maintenant, vous êtes prêt à utiliser le chat avec un historique sauvegardé dans MySQL !

---


## COMPILER LE FICHIER 'SH' AVEC DU 'C'



```
# Si gcc n'est pas installer:
# sudo apt install gcc
gcc -o /home/amine/Bureau/devchat/lancement wrapper.c   #création du fichier lancement executable (double clique)

```
