// ...existing code...

# BigData — Arquivos da disciplina

Bem-vindo(a)! Este repositório contém notebooks e scripts usados nas aulas da disciplina. O objetivo do README é explicar rapidamente o que há aqui e como preparar o ambiente para rodar os exemplos (incluindo criar um ambiente virtual em Python).

## Estrutura principal

- `main.py` — ponto de entrada simples do projeto.
- `pyproject.toml` — dependências do projeto.
- `etl/rotas.ipynb` — notebook para trabalhar a planilha `rotas.xls`.
- `tce/municipios.ipynb` — notebook com consultas à API do TCE (municípios).
- `tce/unidades_gestoras.ipynb` — notebook com chamadas à API e exportação para banco.
- `.gitignore` — arquivos ignorados pelo Git.

## Como criar um ambiente virtual (recomendado)

1. Navegue até a pasta do projeto:
   - Linux / macOS / WSL:
     ```bash
     cd /Users/henriquemota/Workspace/estacio/bigdata
     ```
2. Crie o ambiente virtual:
   ```bash
   python -m venv .venv
   ```
3. Ative o ambiente:
   - macOS / Linux / WSL:
     ```bash
     source .venv/bin/activate
     ```
   - Windows (PowerShell):
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - Windows (cmd):
     ```cmd
     .venv\Scripts\activate.bat
     ```
4. Atualize o pip e instale dependências:
   ```bash
   python -m pip install --upgrade pip
   # instalar o projeto local e dependências declaradas no pyproject.toml
   pip install -e .
   ```
   Observação: se preferir uma lista explícita, crie um `requirements.txt` e use `pip install -r requirements.txt`.

## Rodando os exemplos

- Script simples:

  ```bash
  python main.py
  ```

  (o script chama a função `main` em [`main.py`](main.py))

- Notebooks:
  - Abra o Jupyter (ou VS Code) e execute os notebooks em `etl/` e `tce/`.
  - Muitos notebooks usam `pandas`, `requests`, `sqlalchemy` e variáveis de ambiente (arquivo `.env`).

## Variáveis de ambiente e banco de dados

- Alguns notebooks (p.ex. `tce/unidades_gestoras.ipynb`) usam um `.env` para credenciais de banco. Exemplo:
  ```
  DB_USER=usuario
  DB_PASS=senha
  DB_HOST=host
  DB_PORT=5432
  DB_NAME=banco
  ```
- Nunca comite credenciais reais — o `.gitignore` já está configurado para excluir `.env` e ambientes virtuais.

## Dicas rápidas

- Use o ambiente virtual para evitar conflitos de pacotes.
- Para trabalhar com notebooks no VS Code, instale a extensão Python/Jupyter e selecione o kernel dentro do `.venv`.
- Para depurar dependências, rode `pip list` dentro do ambiente.

---

Se quiser, posso gerar um `requirements.txt` baseado em `pyproject.toml` ou adicionar instruções para Docker/Poetry.
