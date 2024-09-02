# Pedido de Perdão - Um Software de Brincadeira

Este é um software de pedido de perdão de brincadeira desenvolvido em Python utilizando PySide6 para a interface gráfica. O ambiente virtual é gerenciado pelo `pipenv` e o código é compatível com Python 3.12.

### Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado em sua máquina:

- **Python 3.12**: Instale a versão 3.12 do Python.
- **pipenv**: Instale o `pipenv` usando o comando:
  ```bash
  pip install pipenv
  ```

## Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/luciano-zembruzki/Pedido-Perdao-PySide6-or-PyQt6.git
   cd Pedido-Perdao-PySide6-or-PyQt6

   ```

2. **Crie e ative o ambiente virtual**:

   ```bash
   pipenv install
   pipenv shell
   ```

3. **Instale as dependências**:

   As dependências serão instaladas automaticamente ao executar o comando `pipenv install`.

## Executando o Software

Após configurar o ambiente virtual e instalar todas as dependências, você pode executar o software com o seguinte comando:

```bash
python main.py
```

Certifique-se de que o terminal esteja dentro do ambiente virtual criado pelo `pipenv`.

## Estrutura do Projeto

```
├── Pipfile
├── Pipfile.lock
├── end.png
├── end_big.png
├── gui
│   ├── .DS_Store
│   ├── py
│   │   └── ui_widget.py
│   └── ui
│       └── widget.ui
├── main.py
├── question1.png
└── question2.png
```
