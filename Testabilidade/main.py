from authenticator import Authenticator

def main():
    auth = Authenticator()
    
    # Simulando entrada do usuário
    username = input("Username: ")
    password = input("Password: ")
    
    result = auth.authenticate(username, password)
    print(result)

if __name__ == "__main__":
    main()
