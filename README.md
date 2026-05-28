# AUTOMACAO-PROJETO

Projeto desenvolvido para prática de automação de testes utilizando Python.

O projeto contempla testes de API e testes Web automatizados, utilizando Pytest e Selenium WebDriver, além de integração contínua com GitHub Actions.

---

# Tecnologias utilizadas

* Python
* Pytest
* Selenium WebDriver
* Requests
* WebDriver Manager
* GitHub Actions

---

# Estrutura do projeto

```text
AUTOMACAO-PROJETO/
│
├── api_tests/
│   ├── test_pet.py
│   ├── test_store.py
│   └── test_user.py
│
├── web_tests/
│   ├── pages/
│   │   ├── login_page.py
│   │   ├── products_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   │
│   └── test_login.py
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

---

# Automação de API

Os testes de API foram desenvolvidos utilizando a Swagger Petstore API.

Foram criados cenários de validação para:

## User

* Criar usuário
* Buscar usuário
* Excluir usuário

## Pet

* Adicionar pet
* Buscar pet
* Excluir pet

## Store

* Criar pedido
* Buscar pedido
* Excluir pedido

---

# Automação Web

A automação Web foi desenvolvida utilizando Selenium WebDriver no site SauceDemo.

Fluxo automatizado:

* Login no sistema
* Adição de produto ao carrinho
* Acesso ao carrinho
* Checkout da compra
* Finalização da compra

---

# Boas práticas aplicadas

Durante o desenvolvimento foram utilizadas algumas boas práticas para organização e manutenção do projeto:

* Page Object Model (POM)
* Separação entre testes Web e API
* Código modularizado
* Asserções utilizando Pytest
* Uso de waits explícitos no Selenium
* Integração contínua com GitHub Actions

---

# Como executar o projeto

## Clonar o repositório

```bash
git clone https://github.com/Cleiton158/AUTOMACAO-PROJETO.git
```

---

## Acessar a pasta do projeto

```bash
cd AUTOMACAO-PROJETO
```

---

## Criar ambiente virtual

```bash
python -m venv venv
```

---

## Ativar ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

---

## Instalar dependências

```bash
pip install -r requirements.txt
```

---

# Executando os testes

## Todos os testes

```bash
pytest
```

---

## Apenas testes de API

```bash
pytest api_tests
```

---

## Apenas testes Web

```bash
pytest web_tests
```

---

# Integração contínua

O projeto possui integração contínua configurada com GitHub Actions.

Sempre que um novo push é realizado na branch principal, os testes são executados automaticamente.




