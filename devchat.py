import os
from rich.console import Console
from rich.prompt import Prompt
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.ollama import Ollama
from llama_index.core.settings import Settings
import subprocess

console = Console()
DATA_DIR = "code_docs"
MODEL_NAME = "deepseek-r1:8b"

if not os.path.exists(DATA_DIR):
    console.print(f"[bold red]Le dossier '{DATA_DIR}' n'existe pas. Crée-le et ajoute tes fichiers de code/doc dedans.[/bold red]")
    exit()

def check_model_installed(model_name):
    try:
        result = subprocess.run(["ollama", "list"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return model_name in result.stdout.decode()
    except Exception as e:
        return False

if not check_model_installed(MODEL_NAME):
    console.print(f"[bold red]Le modèle '{MODEL_NAME}' n'a pas été trouvé localement. Tentative de téléchargement...[/bold red]")
    subprocess.run(["ollama", "pull", MODEL_NAME])

console.print("[bold green]Chargement des fichiers...[/bold green]")
documents = SimpleDirectoryReader(DATA_DIR).load_data()

console.print("[bold cyan]Connexion au modèle local...[/bold cyan]")
llm = Ollama(model=MODEL_NAME)

# Pour ne pas utiliser openai ou hugginface etc...
Settings.embed_model = None

# Création de l’index vectoriel
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine(
    llm=llm,
    system_prompt=(
        "Tu es un expert développeur web, full-stack, backend, frontend et DevOps. "
        "Réponds avec précision, clarté et si possible des extraits de code. Sois concis mais pédagogique."
    )
)

console.print("[bold green]Bienvenue dans DevChat ! Pose-moi des questions sur le développement.[/bold green]")
while True:
    try:
        user_input = Prompt.ask("[bold blue]Dev >[/bold blue]")
        if user_input.lower() in ("exit", "quit", "q"):
            console.print("[bold yellow]À bientôt ![/bold yellow]")
            break

        response = query_engine.query(user_input)
        console.print(f"[bold magenta]Réponse :[/bold magenta] {response}\\n")

    except KeyboardInterrupt:
        console.print("\\n[bold yellow]Sortie.[/bold yellow]")
        break
