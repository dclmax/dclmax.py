import os
import time
import datetime
from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, BarColumn, TextColumn
from rich.prompt import Prompt
from rich.align import Align

console = Console()

# ================= CORES =================
RED = "\u001B[91m"
GREEN = "\u001B[92m"
YELLOW = "\u001B[93m"
BLUE = "\u001B[94m"
RESET = "\u001B[0m"

# ================= FUNÇÕES =================
def clear_screen():
    os.system("clear")

# ================= BANNER =================
def banner():
    figlet = Figlet(font="standard")

    texto = figlet.renderText("DCL MAX")

    art = f"{RED}{texto}{RESET}"

    console.print(
        Panel(
            Align.center(art),
            title="[green]DOCTOR CORINGA LUNÁTICO[/green]",
            border_style="red",
            padding=(1, 2),
            width=70,
        )
    )

# ================= MENU =================
def show_menu():
    clear_screen()
    banner()

    menu = Text.from_markup(
        "[red]1 • SPAM[/red]\n"
        "[green]2 • DENÚNCIA[/green]\n"
        "[yellow]3 • DCLS[/yellow]\n"
        "[blue]4 • DCL-MAX[/blue]\n"
        "[red]0 • SAIR[/red]"
    )

    console.print(
        Panel(
            Align.left(menu),
            title="[green]MENU[/green]",
            border_style="green",
            padding=(1, 3),
            width=40,
        )
    )

    return Prompt.ask(
        "Escolha",
        choices=["1", "2", "3", "4", "0"],
        default="0"
    )

# ================= LOADING =================
def loading_bar(option, numero):
    clear_screen()
    banner()

    info = (
        f"[red]AÇÃO:[/red] {option}\n"
        f"[yellow]NÚMERO:[/yellow] {numero}"
    )

    console.print(
        Panel(
            info,
            title="[yellow]EXECUTANDO[/yellow]",
            border_style="yellow",
            padding=(1, 3),
            width=50,
        )
    )

    with Progress(
        TextColumn("[red]{task.description}"),
        BarColumn(bar_width=30),
        TextColumn("[yellow]{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task(option, total=100)
        for _ in range(100):
            time.sleep(0.03)
            progress.update(task, advance=1)

# ================= RELATÓRIO =================
def generate_report(option, numero):
    agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    mensagens = {
        "SPAM": "Spam enviado com sucesso 😈",
        "DENÚNCIA": "Denúncia processada com êxito 🔥",
        "DCLS": "DCLS ativado — sistema impactado ⚠️",
        "DCL-MAX": "Modo DCL-MAX ativado 💀",
    }

    texto = (
        f"[red]OPÇÃO:[/red] {option}\n"
        f"[yellow]NÚMERO:[/yellow] {numero}\n"
        f"[green]DATA/HORA:[/green] {agora}\n\n"
        f"[red]PAINEL:[/red] DCL MAX\n"
        f"[green]CRIADOR:[/green] DOCTOR CORINGA LUNÁTICO\n\n"
        f"[green]STATUS:[/green] ✅ CONCLUÍDO\n\n"
        f"{mensagens[option]}"
    )

    console.print(
        Panel(
            texto,
            title="[red]RESULTADO[/red]",
            border_style="red",
            padding=(1, 3),
            width=65,
        )
    )

    Prompt.ask("ENTER para voltar")

# ================= MAIN =================
def main():
    while True:
        op = show_menu()

        if op == "0":
            clear_screen()
            console.print(
                Panel(
                    Align.center(
                        "[red]OBRIGADO POR USAR[/red]\n"
                        "[green]DCL MAX[/green]\n\n"
                        "DOCTOR CORINGA LUNÁTICO 👹"
                    ),
                    border_style="red",
                    padding=(2, 4),
                    width=50,
                )
            )
            break

        numero = Prompt.ask("Digite o número")

        options = {
            "1": "SPAM",
            "2": "DENÚNCIA",
            "3": "DCLS",
            "4": "DCL-MAX",
        }

        opcao = options[op]
        loading_bar(opcao, numero)
        generate_report(opcao, numero)

# ================= START =================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        console.print("[red]Saindo...[/red]")
