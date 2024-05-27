# FakeStoreETL

Projeto exemplo de ETL consumindo dados da API Fake Store, transformando os dados dos usuários e produtos e salvando o resultado em csv

## Configurações

### Pré-requisitos

 - Python 3.7 ou maior
 - Git

### Ajustes

 1. Clonar o repositório

    ``` cmd
    git clone https://github.com/ivesakira/FakeStoreETL.git
    cd FakeStoreETL
    ```

 2. Criar ambiente virtual e dependencias

    ``` cmd
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```

 3. Executa o processo

    ```  cmd
    python src\main.py
    ```

## Estrutura do projeto

 - `src\`: Contem os módulos do projeto
  - `main.py`: Script principal do Projeto
  - `extract.py`: Extração/Consumo da API Fake Store
  - `transform.py`: Transformação dos dados
  - `load.py`: Persistencia dos dados em csv
 - `Resultado\`: Diretório com o resultado do processo de ETL
 - `requirements.txt`: Arquivo com as dependecias do projeto
 - `README.md`: Documentação 

## Dependencias

 - `requests`
 - `pandas`
