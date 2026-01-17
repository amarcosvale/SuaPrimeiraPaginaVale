# SuaPrimeiraPaginaVale

## Descrição
Projeto de blog em Django, com herança de templates, formulários para criar Autor, Categoria e Post, e formulário de busca.

## Como rodar o projeto

1. Clonar o repositório: git clone https://github.com/amarcosvale/SuaPrimeiraPaginaVale.git

2. Entrar na pasta do projeto: cd SuaPrimeiraPaginaVale

3. Criar e ativar o ambiente virtual: 

python -m venv .venv
.venv\Scripts\activate # Windows
source .venv/bin/activate # Linux/Mac

4. Instalar dependências: pip install -r requirements.txt

5. Aplicar migrations: 

python manage.py makemigrations
python manage.py migrate

6. Criar superusuário (opcional, para acessar admin): python manage.py createsuperuser

7. Rodar o servidor: python manage.py runserver

8. Acessar no navegador: http://127.0.0.1:8000/

## Links e funcionalidades

- **Home** → lista todos os posts  
- **Criar Autor** → formulário para adicionar autor  
- **Criar Categoria** → formulário para adicionar categoria  
- **Criar Post** → formulário para adicionar post  
- **Buscar** → busca posts pelo título  

---

