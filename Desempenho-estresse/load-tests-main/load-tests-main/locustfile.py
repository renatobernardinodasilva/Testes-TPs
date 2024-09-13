from locust import HttpUser, task, between

class SimpleLoadTestUser(HttpUser):
    host = "http://localhost:8000" 
    wait_time = between(1, 5)  # Espera entre 1 e 5 segundos entre as tarefas
    
    @task(1)  # A tarefa test_list_items terá uma prioridade de 1
    def test_list_items(self):
        # Faz uma requisição GET para a URL que retorna a lista de itens
        response = self.client.get("http://localhost:8000/items")  # Substitua pela URL correta da sua API
        # Você pode verificar a resposta (opcional)
        if response.status_code == 200:
            print("Lista de itens recebida com sucesso!")
        else:
            print(f"Erro ao acessar a lista de itens: {response.status_code}")
    @task(2)  # Outra tarefa com prioridade maior
    def test_create_item(self):
        # Exemplo de criação de um novo item (POST)
        payload = {"name": "notebook", "description": "Notebook vaio de 250gb"}
        response = self.client.post("http://localhost:8000/items", json=payload)  # Substitua pela URL correta

        if response.status_code == 201:
            print("Item criado com sucesso!")
        else:
            print(f"Erro ao criar item: {response.status_code}")