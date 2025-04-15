import subprocess
import mysql.connector
from rich.console import Console
from rich.prompt import Prompt
from llama_index.llms.ollama import Ollama
from dotenv import load_dotenv
import os

load_dotenv()

console = Console()
MODEL_NAME = "deepseek-coder:6.7b"
db_user = os.getenv("DB_USER").capitalize()

# Connexion à la BDD
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return connection
    except mysql.connector.Error as err:
        console.print(f"[bold red]Erreur de connexion à la base de données : {err}[/bold red]")
        return None

# Récupérer l'historique des messages
def get_chat_history():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "SELECT user_message, bot_response FROM messages ORDER BY timestamp ASC"
        cursor.execute(query)
        chat_history = cursor.fetchall()
        cursor.close()
        connection.close()
        return chat_history
    return []

# Enregistrer un message dans la base de données
def save_message_to_db(user_message, bot_response):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO messages (user_message, bot_response) VALUES (%s, %s)"
        
        if isinstance(bot_response, str):
            response_text = bot_response
        else:
            response_text = str(bot_response)

        cursor.execute(query, (user_message, response_text))
        connection.commit()
        cursor.close()
        connection.close()

# Vérifier si le modèle est installé localement
def check_model_installed(model_name):
    try:
        result = subprocess.run(["ollama", "list"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return model_name in result.stdout.decode()
    except Exception:
        return False

# Si le modèle n'est pas installé, tenter de le télécharger
if not check_model_installed(MODEL_NAME):
    console.print(f"[bold red]Le modèle '{MODEL_NAME}' n'a pas été trouvé localement. Tentative de téléchargement...[/bold red]")
    subprocess.run(["ollama", "pull", MODEL_NAME])

# Initialiser le modèle Ollama
llm = Ollama(model=MODEL_NAME)

console.print(f"[bold green]Bienvenue {db_user}. Pose-moi n’importe quelle question, je ferai de mon mieux pour t'aider.[/bold green]")

while True:
    try:
        # Récupérer l'historique des conversations
        chat_history = get_chat_history()

        # Créer un format de messages compatible avec l'IA (récupérer les messages précédents)
        messages = []
        for idx, msg in enumerate(chat_history):
            if idx % 2 == 0:
                messages.append({"role": "user", "content": msg[0]})
            else:
                messages.append({"role": "assistant", "content": msg[1]})

        # Ajouter le dernier message utilisateur à l'historique
        user_input = Prompt.ask("[bold blue]Toi >[/bold blue]")
        if user_input.lower() in ("exit", "quit", "byebye"):
            console.print("[bold yellow]À bientôt ![/bold yellow]")
            try:
                console.print("[bold cyan]Arrêt du modèle Ollama...[/bold cyan]")
                subprocess.run(["ollama", "stop", MODEL_NAME], check=True)
            except subprocess.CalledProcessError as e:
                console.print(f"[bold red]Erreur lors de l'arrêt du modèle : {e}[/bold red]")
            break

        # Ajouter le dernier message utilisateur à l'historique
        messages.append({"role": "user", "content": user_input})

        # Obtenir la réponse du modèle
        response = llm.complete(user_input)

        # Vérifier si la réponse est une instance de CompletionResponse
        if isinstance(response, str):
            console.print(f"[bold magenta]IA :[/bold magenta] {response}")
        else:
            console.print(f"[bold magenta]IA :[/bold magenta] {response.text if hasattr(response, 'text') else str(response)}")

        # Sauvegarder l'échange dans la base de données
        save_message_to_db(user_input, response)

    except KeyboardInterrupt:
        console.print("\n[bold yellow]Sortie.[/bold yellow]")
        break
