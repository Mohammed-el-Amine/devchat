
# DevChat CLI – Spécialiser Ollama pour le Développement

## 🎯 Objectif

Créer un petit **chat CLI local** spécialisé pour le développement avec un modèle Ollama local (`deepseek-r1:8b`), combiné à un RAG sur des documents de code.

---

## 🛠️ Dépendances à installer

```bash
curl -fsSL https://ollama.com/install.sh | sh
python3 -m venv dev-chat
source devchat/bin/activate
pip install --upgrade pip
pip install llama-index llama-index-llms-ollama rich
```

---

## 📁 Structure du projet recommandée

```
ton-projet/
├── devchat.py
└── code_docs/
    ├── DOCKER.md
    ├── react_patterns.md
    ├── backend_tips.md
    ├── cheatsheet.txt
    └── ...
```

---

## 🧠 Description du script

- Charge tous les fichiers dans `code_docs/`
- Crée un index vectoriel (via `llama-index`)
- Connecte ton modèle local via `ollama`
- Utilise un prompt système spécialisé développeur
- Permet de discuter directement via terminal


---

## ✅ Lancement du chat

```bash
python devchat.py
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
