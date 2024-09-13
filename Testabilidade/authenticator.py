class Authenticator:
    def __init__(self):
        # Simulando uma base de dados com credenciais
        self.users = {"user1": "password123", "user2": "pass456"}
    
    def authenticate(self, username, password):
        if username in self.users and self.users[username] == password:
            return "Access Granted"
        return "Access Denied"
