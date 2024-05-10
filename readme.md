# Projeto de Testes Automatizados com Behave

## Sobre o Projeto

Este projeto é um mini teste de integração da API Petstore do Swagger, solicitado no desafio técnico da Sulamérica. 

## Tecnologias Utilizadas

- **Python**: Linguagem de programação usada para escrever os testes.
- **Behave**: Framework de BDD utilizado para executar os testes escritos em Gherkin.
- **Faker**: Biblioteca para a geração de dados fictícios para os testes.
- **Requests**: Biblioteca para realizar requisições HTTP nas APIs.
- **JSONSchema**: Utilizado para validar as respostas das APIs de acordo com esquemas predefinidos, garantindo que os dados retornados estejam corretos.

## Como Executar o Projeto

### Pré-Requisitos

Para executar este projeto, você precisará ter instalado:
- Python 3.7 ou superior

### Configuração

1. Clone o repositório do projeto:
   ```bash
   git clone git@github.com:MatheusGeambastiane/Sulamerica-Test---Python.git .
   ```
   
2. Instale todas as dependências

    ```bash
    pip install -r requirements.txt
    ```

3. Execute os testes

    ```bash
    behave
    ```
