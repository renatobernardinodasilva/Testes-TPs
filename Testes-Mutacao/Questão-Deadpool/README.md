# Preparação do ambiente...  

## Na sua máquina: 
```
python -m venv venv
```

| | |    
| --- | --- |
| Windows: | Linux: |    
| .\venv\Scripts\activate | source venv/bin/activate |     

```
pip install mutatest
pip install unittest
```

## Após ter preparado o ambiente na sua máquina...
Você vai entrar no diretório onde está o o código com os testes em que quer realizar o mutatest, nesse caso a pasta "Deadpool", se você estiver utilizando o codespace vai ficar assim:   
<b>seu-user ➜ /workspaces/2tp-2-teste-de-muta-o-tp2-estrutura/Deadpool</b>  

Ja ná pasta Deadpoll, no terminal você vai digitar o seguinte comando:
```
mutatest -s . --testcmd "python -m unittest discover"
```
O resultado dos testes aparece no terminal. 