from time import sleep
from config import SENHA, USUARIO
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from setup import SeleniumSetup


class Main(SeleniumSetup):
    
    locator_user = (By.CSS_SELECTOR, '#id_username')
    locator_password = (By.CSS_SELECTOR, '#id_password')
    locator_acessar = (By.CSS_SELECTOR, 'body > div.holder > main > div.flex-container > div.form-login.flex-item > form > div.submit-row > input')
    locator_disciplinas = (By.XPATH, '//a[contains(text(),"Minhas Disciplinas")]')
    locator_teste_de_software = (By.XPATH, '//a[contains(text(),"Acessar Disciplina")]')
    locator_verif_prof = (By.XPATH, '//*[@id="content"]/div[4]/div[1]/div/div/div[2]/h4')
    locator_email_prof = (By.XPATH, '//*[@id="content"]/div[4]/div[1]/div/div/div[2]/dl/dd[2]')
    locator_logout = (By.CSS_SELECTOR, '#mainmenu > ul._main_menu > li.menu-logout > a > span.fas.fa-sign-out-alt')

    def open_suap(self, site):
        self.driver.get(site)
    
    def autenticar_suap(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.locator_user)).send_keys(USUARIO)
            self.driver.find_element(*self.locator_password).send_keys(SENHA)
            self.driver.find_element(*self.locator_acessar).click()
            return True
        except TimeoutException:
            print("Erro: Falha na autenticação.")
            return False

    def verificar_autenticacao(self):
        url_atual = self.driver.current_url
        if "https://suap.ifrn.edu.br/" in url_atual:
            print('Usuário autenticado com sucesso!')
        else:
            print('Não foi possível autenticar!')

    def acessar_disciplinas(self):
        try:
            minhas_disciplinas = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.locator_disciplinas))
            minhas_disciplinas.click()
            print("Acessou: 'Minhas Disciplinas' com sucesso!")
        except TimeoutException:
            print("Erro: 'Minhas Disciplinas' não localizado!")

    def acessar_teste_de_software(self):
        try:
            teste_de_software = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.locator_teste_de_software))
            teste_de_software.click()
            print("Acessou: 'Teste de Software' com sucesso!")
        except TimeoutException:
            print("Erro: 'Teste de Software' não localizado!")

    def verificar_pagina_disciplina(self):
        # Verificar se a página atual é a da disciplina "Teste de Software"
        if "Teste de Software" in self.driver.title:
            print('Página de Teste de Software acessada com sucesso!')
        else:
            print('Erro ao acessar a página de Teste de Software!')

    def verificar_professor(self):
        try:
            professor_element = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(self.locator_verif_prof)
            )
            nome_professor = professor_element.text
            print("Nome do professor encontrado: ", nome_professor)
            if "Placido Antonio de Souza Neto" in nome_professor:
                print("O nome do professor corresponde à pesquisa.")
                email_element = WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located(self.locator_email_prof)
                )
                email_professor = email_element.text
                print("E-mail do professor: ", email_professor)
            else:
                print("O nome do professor está incorreto ou não encontrado.")
        except TimeoutException:
            print('Erro ao encontrar o professor ou o e-mail')

    def logout(self):
        try:
            logout = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable(self.locator_logout)
            )
            logout.click()
            print("Logout realizado com sucesso!")
        except TimeoutException:
            print("Erro ao realizar o logout!")

    def verificar_logout(self):
        url_atual = self.driver.current_url
        if "https://suap.ifrn.edu.br/accounts/login/?next=/" in url_atual:
            print('Logout confirmado com sucesso!')
        else:
            print('Erro ao confirmar o logout! Tente novamente:', url_atual)

if __name__ == '__main__':
    main = Main()
    main.open_suap('https://suap.ifrn.edu.br/accounts/login/?next=/')

    if main.autenticar_suap():
        main.verificar_autenticacao()
        main.acessar_disciplinas()
        main.acessar_teste_de_software()
        main.verificar_pagina_disciplina()
        main.verificar_professor()
        main.logout()
        main.verificar_logout()
    input('Pressione uma tecla para sair:')
    main.driver.quit()