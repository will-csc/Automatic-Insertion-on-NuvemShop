from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import base64
import re

# Lê os links do arquivo links.txt
with open('links.txt', 'r') as file:
    links = [linha.strip() for linha in file if linha.strip()]

for link in links:
    driver = webdriver.Chrome()
    driver.get(link)

    # Espera o carregamento da página
    time.sleep(3)

    # Extrai o nome do produto
    produto_element = driver.find_element(By.CSS_SELECTOR, 'span.showalbumheader__gallerytitle')
    nome_produto = produto_element.get_attribute('data-name').strip()
    nome_produto = re.sub(r'[<>:"/\\|?*]', '', nome_produto)

    # Cria a pasta se não existir
    if not os.path.exists(nome_produto):
        os.makedirs(nome_produto)

    # Encontra a div específica que contém as imagens
    galeria_div = driver.find_element(By.CSS_SELECTOR, '.showalbum__imagecardwrap')

    # Dentro dela, pega só os <img>
    imagens = galeria_div.find_elements(By.TAG_NAME, 'img')

    # Faz o download de cada imagem usando o atributo 'data-origin-src'
    for i, img in enumerate(imagens):
        src = img.get_attribute('data-origin-src')  # Pega o valor do 'data-origin-src'
        
        # Certifique-se de que a URL seja válida
        if src and src.startswith("//"):
            src = "https:" + src  # Adiciona o prefixo http://
        
        if src:
            try:
                # Abrir nova aba
                driver.execute_script(f"window.open('{src}', '_blank');")
                time.sleep(1)

                # Alterna para nova aba
                driver.switch_to.window(driver.window_handles[1])

                # Espera a imagem carregar
                time.sleep(1)

                # Usa JS para capturar a imagem da aba atual como base64
                base64_script = """
                    var img = document.querySelector('img');
                    var canvas = document.createElement('canvas');
                    canvas.width = img.naturalWidth;
                    canvas.height = img.naturalHeight;
                    var ctx = canvas.getContext('2d');
                    ctx.drawImage(img, 0, 0);
                    return canvas.toDataURL('image/png').split(',')[1];
                """
                image_data = driver.execute_script(base64_script)

                # Decodifica e salva
                caminho = os.path.join(nome_produto, f'imagem_{i + 1}.png')
                with open(caminho, 'wb') as f:
                    f.write(base64.b64decode(image_data))
                print(f"Imagem {i + 1} salva: {caminho}")

                # Fecha a aba e volta para a principal
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(1)

            except Exception as e:
                print(f"Erro ao baixar imagem {i + 1}: {e}")
    driver.close()


driver.quit()
