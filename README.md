## Themis API

<hr>

### SOBRE O PROJETO :file_folder:
Microsserviço em Python utlizando Flask para o desafio "Nork Town"

<hr>

### TECNOLOGIAS QUE ESTÃO SENDO USADAS :space_invader:

:small_blue_diamond: Flask 

:small_blue_diamond: Pydantic

:small_blue_diamond: SqlAlchemy

:small_blue_diamond: Decouple

:small_blue_diamond: Pytest

:small_blue_diamond: Mutatest


<hr>

### ROTAS DISPONIVEIS :telescope:

#### GET

```
{host}:{port}/client - Lista todos os clientes cadastrados
{host}:{port}/client/{id} - Busca um cliente por seu id
{host}:{port}/car - Lista todos os carros cadastrados
{host}:{port}/car/{id} - Busca um carro por seu id
```

#### POST

```
{host}:{port}/client - Cadastra um novo cliente de acordo com o body enviado - {"email": string, "sale_opportunity": boolean}
{host}:{port}/car - Cadastro um novo carro de acordo com o body enviado - {"color": string("YELLOW" || "BLUE" || "GRAY"), "model": string("HATCH" || "SEDAN" || "CONVERTIBLE"), "client_id": integer}
```

#### PUT

```
{host}:{port}/client/{id} - Edita um cliente existente de acordo com o body enviado - {"email": string, "sale_opportunity": boolean}
```

#### DELETE

```
{host}:{port}/client/{id} - Deleta um cliente de acordo com o id enviado na rota
{host}:{port}/car/{id} - Deleta um carro de acordo com o id enviado na rota
```

<hr>

### PARA EXECUTAR O SERVIDOR :calling:
- Crie um arquivo ```.env``` na raiz do projeto de acordo com o ```.env_exemple```
- Crie um novo ambiente virtual com ```python3 -m virtualenv .venv``` ou ```python3 -m venv .venv```
- Ative o seu novo ambiente virtual com ```source ./venv/bin/activate``` ou ```.venv\Scripts\activate.bat```
- Instale as dependências do projeto com ```pip install -r requirements.txt``` ou ```pip install -r requirements-dev.txt``` caso for executar os testes
- Execute o servidor com ```gunicorn --bind localhost:4001 athena:app```

### PARA EXECUTAR OS TESTES :bomb:
- Somente testes unitários: ```pytest```
- Testes de cobertura: ```pytest --cov-report term-missing --cov-config=.coveragerc --cov=src```
- Testes de mutação: ```chmod +x mutation_tests.sh``` e depois ```./mutation_tests.sh``` 
