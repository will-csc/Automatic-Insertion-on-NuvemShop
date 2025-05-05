from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# ------------- Lista de diretórios -------------
pastas = [nome for nome in os.listdir() if os.path.isdir(nome)]

# ------------- Inicia navegador -------------
driver = webdriver.Chrome()
driver.get("https://www.nuvemshop.com.br/login")

# ------------- Login -------------
email = driver.find_element(By.ID, 'user-mail')
email.send_keys("seuemail")

password = driver.find_element(By.ID, 'pass')
password.send_keys("suasenha")

botao = driver.find_element(By.CLASS_NAME, 'js-reset-password-type')
botao.click()
time.sleep(5)

msg = """Mostre sua paixão pelo basquete com estilo e autenticidade! Esta camiseta oficial da NBA traz o nome e número do(a) lendário(a) [Nome do Jogador], representando o [Time] com orgulho.

Confeccionada com tecido de alta qualidade, proporciona conforto, durabilidade e respirabilidade, ideal tanto para jogos quanto para o dia a dia. Com design licenciado pela NBA, você garante um visual moderno, esportivo e cheio de atitude.

Detalhes do Produto:

Produto oficial e licenciado pela NBA

Estampa frontal e traseira com nome e número do jogador

Material: 100% poliéster ou algodão premium (dependendo do modelo)

Tecnologia [Nike Dri-FIT / Adidas Climalite / Outro, se aplicável]

Tamanhos disponíveis: XS ao XXL

Ideal para torcedores, colecionadores ou presentear fãs do esporte"""

# ------------- Adiciona produtos com nomes formatados -------------
for nome in pastas:
    # ------------- Navega para produtos -------------
    botao = driver.find_element(By.ID, 'control-products')
    botao.click()
    time.sleep(3)

    botao = driver.find_element(By.CSS_SELECTOR, 'button.nimbus--button--primary')
    botao.click()
    time.sleep(4)
    
    # Nome da camisa
    input_nome = driver.find_element(By.CSS_SELECTOR, "input[name='name']")
    input_nome.send_keys(nome)
    
    # Descrição
    iframe = driver.find_element(By.CSS_SELECTOR, "iframe.tox-edit-area__iframe")  # Common class for TinyMCE
    driver.switch_to.frame(iframe)
    
    # Ache a area editavel
    editor_body = driver.find_element(By.ID, "tinymce")

    # Insere o texto
    editor_body.send_keys(msg)

    # Volta pro padrão
    driver.switch_to.default_content()
    
    # Volta para o contexto da página principal
    driver.switch_to.default_content()
    time.sleep(2.5)
    
    # Encontra os arquivos na pasta
    arquivos = [os.path.abspath(os.path.join(nome, f)) for f in os.listdir(nome) if os.path.isfile(os.path.join(nome, f))]

    # Envia os arquivos encontrados na pasta
    for arquivo in arquivos:
        # Localiza o campo de upload de arquivo
        input_file = driver.find_element(By.ID, 'input-file')
        input_file.send_keys(arquivo)
        time.sleep(2)  # Aguarda um pouco entre os uploads, se necessário
    
    # Preços
    price = driver.find_element(By.ID, "input_price")
    price.send_keys(200)
    promotional_price = driver.find_element(By.ID, "input_promotionalPrice")
    if "200" in nome or "19" in nome:
        promotional_price.send_keys(230)
    else:
        promotional_price.send_keys(230)
        
    """# Categoria
    botao = driver.find_element(By.LINK_TEXT, "Adicionar categorias") # Adicionar
    botao.click()
    
    time.sleep(1.5)
    botao = driver.find_element(By.XPATH, "//a[contains(text(), 'Criar categoria')]")
    botao.click()
    
    time.sleep(1.5)
    input_name = driver.find_element(By.ID,"input_name")
    input_name.send_keys(f"Brasileirão/{nome}")
    
    botao = driver.find_element(By.XPATH, "//button[text()='Criar categoria']")
    botao.click() #Salva Categoria
    
    botao = driver.find_element(By.CSS_SELECTOR, "button[data-testid='btn-navbar-back']") 
    botao.click() #Voltar
    """
    
    # Variações
    time.sleep(2)
    botao = driver.find_element(By.LINK_TEXT, "Adicionar variações")
    botao.click()
    
    time.sleep(2)
    select_element = driver.find_element(By.ID, "id-select")
    select = Select(select_element)
    select.select_by_visible_text("Tamanho")
    
    time.sleep(2)
    botao = driver.find_element(By.XPATH, "//a[text()='Selecionar tudo']")
    botao.click() # Seleciona todas
    
    time.sleep(2)
    botao = driver.find_element(By.XPATH, "//button[text()='Criar']")
    botao.click() # Criar
    
    botao = driver.find_element(By.CSS_SELECTOR, "button[data-testid='btn-navbar-back']")
    botao.click() # Voltar
    
    time.sleep(3)
    # Ajustar preços das variações
    input_price = driver.find_element(By.ID, "input_price")
    input_price.clear()
    if "200" in nome or "19" in nome:
        input_price.send_keys(150)
        
    else:
        input_price.send_keys(130)

    time.sleep(2)
    botao = driver.find_element(By.XPATH, "//p[text()='Aplicar em todas']")
    botao.click()
    
    time.sleep(3)
    botao = driver.find_element(By.CSS_SELECTOR, "button.nimbus-button_appearance_primary__fymkre1")
    botao.click() #Salvar
    time.sleep(5)


