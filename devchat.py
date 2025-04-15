import subprocess
from rich.console import Console
from rich.prompt import Prompt
from llama_index.llms.ollama import Ollama

console = Console()
MODEL_NAME = "deepseek-coder:6.7b"

def check_model_installed(model_name):
    try:
        result = subprocess.run(["ollama", "list"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return model_name in result.stdout.decode()
    except Exception:
        return False

if not check_model_installed(MODEL_NAME):
    console.print(f"[bold red]Le modèle '{MODEL_NAME}' n'a pas été trouvé localement. Tentative de téléchargement...[/bold red]")
    subprocess.run(["ollama", "pull", MODEL_NAME])

llm = Ollama(model=MODEL_NAME)

console.print("[bold green]Bienvenue Amine. Pose-moi n’importe quelle question, je ferai de mon mieux pour t'aider.[/bold green]")

while True:
    try:
        user_input = Prompt.ask("[bold blue]Toi >[/bold blue]")
        if user_input.lower() in ("exit", "quit", "q"):
            console.print("[bold yellow]À bientôt ![/bold yellow]")
            try:
                console.print("[bold cyan]Arrêt du modèle Ollama...[/bold cyan]")
                subprocess.run(["ollama", "stop", MODEL_NAME], check=True)
            except subprocess.CalledProcessError as e:
                console.print(f"[bold red]Erreur lors de l'arrêt du modèle : {e}[/bold red]")
            break

        # Demander une réponse au modèle
        response = llm.complete(user_input)
        console.print(f"[bold magenta]IA :[/bold magenta] {response}")

    except KeyboardInterrupt:
        console.print("\n[bold yellow]Sortie.[/bold yellow]")
        break
