HydroLife – Sistema de Monitoramento de Hidratação

O HydroLife é um aplicativo desktop desenvolvido em Python + Tkinter, com sistema de cadastro, cálculo de meta diária de água, registro de ingestão e armazenamento de dados em banco local (SQLite).

Este guia explica como instalar, configurar e executar o projeto.

🚀 1. Pré-requisitos

Antes de rodar o projeto, instale:

✔ Python 3.10+

Baixe em:
https://www.python.org/downloads/

Durante a instalação, marque a opção:

[✔] Add Python to PATH

✔ Instalar dependências

As bibliotecas usadas são:

Tkinter (já vem com Python)

SQLite3 (já vem com Python)

Outras dependências listadas no requirements.txt

⚙️ 3. Instalando dependências

no arquivo requirements.txt, execute:

pip install -r requirements.txt


▶️ 4. Como rodar o projeto

Navegue até a pasta do projeto:

cd HydroLife/app


E execute:

python main.py


🛠 5. Banco de dados

O sistema usa SQLite, e o banco geralmente é criado automaticamente.


🧪 7. Problemas comuns
❌ "ModuleNotFoundError"

Algum módulo não foi encontrado?

Execute:

pip install pillow


ou verifique se está no diretório correto.


📄 8. Licença

Projeto educacional para fins de estudo.
Desenvolvido por:
Gustavo Sthel, @
Nathaly Pereira, @metataly