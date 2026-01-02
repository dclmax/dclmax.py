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
    figlet = Figlet(font="slant")
    dcl = figlet.renderText("DCL")
    max_ = figlet.renderText("MAX")

    art = f"{RED}{dcl}{GREEN} M{YELLOW}A{RED}X{RESET}\n{max_}"

    console.print(
        Panel(
            Align.center(art),
            title="[green]DOCTOR CORINGA LUNÁTICO[/green]",
            border_style="red",
            padding=(0, 1),
        )
    )

# ================= MENU =================
def show_menu():
    clear_screen()
    banner()

    menu = Text.from_markup(
        "[red]1 SPAM[/red]\n"
        "[green]2 DENÚNCIA[/green]\n"
        "[yellow]3 DCLS[/yellow]\n"
        "[blue]4 DCL-MAX[/blue]\n"
        "[red]0 SAIR[/red]"
    )

    console.print(
        Panel(
            Align.left(menu),
            title="MENU",
            border_style="green",
            padding=(0, 2),
            width=40,
        )
    )

    return Prompt.ask("Escolha", choices=["1", "2", "3", "4", "0"], default="0")

# ================= EXECUÇÃO =================
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
            title="EXECUTANDO",
            border_style="yellow",
            padding=(0, 2),
            width=50,
        )
    )

    with Progress(
        TextColumn("[red]{task.description}"),
        BarColumn(bar_width=30),
        TextColumn("[yellow]{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task(option, total=1000)
        for _ in range(1000):
            time.sleep(0.01)
            progress.update(task, advance=1)

# ================= RELATÓRIO =================
def generate_report(option, numero):
    agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    mensagem_debochada = {
        "SPAM": "Spam enviado! O alvo tá chorando agora kkk 😂💀",
        "DENÚNCIA": "Denúncia processada! Adeus WhatsApp pro infeliz! 👋🔥",
        "DCLS": "DCLS ativado! Sistema sobrecarregado, ele que se foda! 🤡",
        "DCL-MAX": "DCL-MAX no talo! Destruição total ativada, LUNÁTICO MODE ON! 😈",
    }

    texto = (
        f"[red]OPÇÃO:[/red] {option}\n"
        f"[yellow]NÚMERO:[/yellow] {numero}\n"
        f"[green]DATA/HORA:[/green] {agora}\n"
        f"[red]PAINEL:[/red] DCL MAX\n"
        f"[green]CRIADOR:[/green] DOCTOR CORINGA LUNÁTICO\n\n"
        f"[green]STATUS:[/green] ✅ CONCLUÍDO!\n\n"
        f"{mensagem_debochada[option]}"
    )

    console.print(
        Panel(
            texto,
            title="RESULTADO",
            border_style="red",
            padding=(1, 2),
            width=60,
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
                    "OBRIGADO POR USAR DCL MAX\nDOCTOR CORINGA LUNÁTICO 👹",
                    border_style="red",
                    padding=(1, 2),
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
        print("\nSaindo...")
