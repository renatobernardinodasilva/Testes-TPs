
# Sistema de Autenticação Simples em Python

Este projeto implementa um sistema de autenticação simples, com o objetivo de demonstrar conceitos de testabilidade de software. O sistema permite verificar credenciais de usuário e é estruturado de forma a facilitar a criação de testes automatizados.

## Estrutura do Projeto

```
authenticator_project/
│
├── authenticator.py      # Lógica de autenticação
├── main.py               # Script principal (opcional para demonstração)
└── tests/
    └── test_authenticator.py  # Testes automatizados
```

## Passos para Executar o Projeto

### 1. Clone o Repositório

Clone o repositório para a sua máquina local.

```bash
git clone https://github.com/josevilanir/TP---Testabilidade.git
cd authenticator_project
```

### 2. Instale as Dependências

Este projeto utiliza o `pytest` para testes automatizados. Certifique-se de que o `pytest` esteja instalado:

```bash
pip install pytest
```

### 3. Execute os Testes Automatizados

Para garantir que o sistema de autenticação está funcionando conforme esperado, execute os testes automatizados:

```bash
pytest tests/
```

### 4. Execute o Sistema de Autenticação (Opcional)

Se quiser testar o sistema manualmente, você pode rodar o script principal:

```bash
python main.py
```
