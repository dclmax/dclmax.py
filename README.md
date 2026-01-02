🔥 DCL MAX
DCL MAX é um painel interativo desenvolvido em Python, projetado para execução direta no Termux (Android).
O projeto utiliza bibliotecas modernas para oferecer uma interface organizada, profissional e intuitiva via terminal.
📌 Informações do Projeto
Nome: DCL MAX
Tipo: Painel interativo em terminal
Linguagem: Python 3
Plataforma: Termux (Android)
Criador: Doctor Coringa Lunático
✨ Funcionalidades
Interface estilizada com caixas e painéis
Menu interativo com múltiplas opções
Exibição organizada de informações
Estrutura simples e fácil de manter
Ideal para automações, painéis ou projetos personalizados
🧰 Requisitos
Antes de iniciar, certifique-se de ter:
Termux atualizado
Python 3 instalado
Git instalado
Conexão com a internet
🚀 Instalação e Execução (Termux)
Execute os comandos na ordem, diretamente no Termux:
Copiar código
Bash
pkg update && pkg upgrade -y
pkg install git python -y
git clone https://github.com/dclmax/dclmax.py.git
cd dclmax.py
pip install pyfiglet rich
python DCL-MAX.py
📖 Explicação dos Comandos
Comando
Função
pkg update && pkg upgrade -y
Atualiza o Termux

pkg install git python -y

Instala dependências básicas
git clone ...
Baixa o projeto do GitHub

cd dclmax.py

Acessa a pasta do projeto

pip install pyfiglet rich

Instala bibliotecas do painel

python DCL-MAX.py

Executa o painel
📂 Estrutura do Projeto
Copiar código
Text

dclmax.py/
├── DCL-MAX.py
├── README.md
└── requirements.txt (opcional)

📦 Dependências
O projeto utiliza as seguintes bibliotecas:
pyfiglet → Estilização de textos no terminal
rich → Painéis, cores, caixas e layout profissional
Instalação alternativa:
Copiar código
Bash
pip install -r requirements.txt
🛠️ Boas Práticas
Sempre mantenha o Termux atualizado
Utilize Python 3
Não modifique o código sem conhecer sua função
Evite executar versões alteradas de fontes desconhecidas
⚠️ Aviso Legal
Este projeto é destinado a uso educacional e demonstrativo.
O autor não se responsabiliza por usos indevidos, ilegais ou que violem termos de terceiros.
👤 Autor
Doctor Coringa Lunático
Projeto independente — DCL MAX
