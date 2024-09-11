from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Firefox(options=options)
driver.implicitly_wait(10)
driver.get("https://es.trustpilot.com/review/sansarushop.com")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "onetrust-reject-all-handler"))).click() # Se espera a que se cierre el pop-up

numeros_pagina = driver.find_elements(By.CLASS_NAME, "pagination-link_item__mkuN3")
ultima_pagina = max([int(button.text) for button in numeros_pagina]) # Se coge el máximo porque es el que indica dice cuál es la última

click = True
pagina_actual = 1
num_resenas = 0
f1 = open("data/reviews.txt", "a")
f2 = open("data/scores.txt", "a")

while pagina_actual < ultima_pagina:
    paginas = driver.find_elements(By.CLASS_NAME, "pagination-link_rel__VElFy") # Contiene los botones que aparecen para pasar a otra página
    siguiente_pagina = paginas[len(paginas)-1] # Es el botón para pasar a la siguiente página
    try:
        if click: # Si se ha podido hacer click en la iteración anterior, se cogen los elementos de la nueva página
            elems = driver.find_elements(By.CLASS_NAME, "styles_reviewCard__9HxJJ")
            for elem in elems:
                try:
                    header = elem.find_element(By.TAG_NAME, "h2").text
                    puntuacion = int(elem.find_element(By.TAG_NAME, "img").get_attribute("alt")[13])
                    parrafos = elem.find_elements(By.TAG_NAME, "p")
                    opinion = parrafos[0].text.replace("\n", " ")
                    # date = paragraphs[1].text[26:]
                    # reviews.append({"header": header, "comment": comment, "date": date, "review": review})
                    if len(parrafos) == 1:  # Si no hay reseña, se guarda solo la cabecera
                        string = header
                    else:
                        string = header + " " + opinion # Se guarda la cabecera y la reseña porque ambos pueden contener información importante
                    num_resenas += 1
                    f1.write(string + "\n")
                    f2.write(str(puntuacion) + "\n")
                except: # Algún campo ha fallado y no se ha guardado la reseña
                    pass
    except: # Si no se ha encontrado el elemento o si el click ha fallado
        pass
    finally: # Ejecución obligatoria
        try:
            siguiente_pagina.click() # Se intenta hacer click para ir a una nueva página
            pagina_actual += 1
            click = True
        except: # Si falla el click, en la siguiente iteración se repetirá
            click = False
            pass

driver.close()
f1.close()
f2.close()

print(num_resenas)
