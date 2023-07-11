import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Configuracion del Driver de Selenium para el navegador Google Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Ciclo "for" para repetir la transacción 10 veces
for intento in range(10):
    # Acceder a la pagina de inicio de sesion de Tienda Nube
    driver.get("https://finnegansdemo.mitiendanube.com/productos/escritorio-oficina/")
    driver.maximize_window()
    time.sleep(1)

    # Aceptar coockies
    coockie = driver.find_element(By.XPATH, "//*[@id='container']/div[3]/div[2]/div/div[2]/a")
    time.sleep(1)
    driver.execute_script("arguments[0].click();", coockie)
    time.sleep(1)

    # Encontrar campo agregar a carrito
    carrito = driver.find_element(By.XPATH, "//*[@id='product_form']/div[5]/div/div/input")
    time.sleep(1)
    carrito.click()
    time.sleep(1)

    # Clickear en comprar
    comprar = driver.find_element(By.XPATH, "//*[@id='ajax-cart-submit-div']/input")
    time.sleep(1)
    comprar.click()
    time.sleep(1)

    # Encontrar el campo Email
    email = driver.find_element(By.XPATH, "//*[@id='contact.email']")
    time.sleep(1)
    email.clear()
    time.sleep(1)
    email.send_keys("joseggarcia34@gmail.com", Keys.ENTER)
    time.sleep(1)

    # Encontrar codigo postal
    codigop = driver.find_element(By.XPATH, "//*[@id='shippingAddress.zipcode']")
    time.sleep(1)
    codigop.clear()
    time.sleep(1)
    codigop.send_keys("1428", Keys.ENTER)
    time.sleep(1)

    # Continuar con la compra
    continuar = driver.find_element(By.XPATH, "//*[@id='main-column']/div[2]/form/div[2]")
    time.sleep(1)
    continuar.click()
    time.sleep(3)

    # Envio

    # nombre del destinatario
    Nombre_destinatario = driver.find_element(By.XPATH, "//*[@id='shippingAddress.first_name']")
    time.sleep(1)
    Nombre_destinatario.clear()
    Nombre_destinatario.send_keys("JOSE")
    time.sleep(1)

    # Apellido del destinatario
    Apellido_destinatario = driver.find_element(By.XPATH, "//*[@id='shippingAddress.last_name']")
    time.sleep(1)
    Apellido_destinatario.clear()
    Apellido_destinatario.send_keys("GARCIA")
    time.sleep(1)

    # Domicilio destinatario
    calle_destinatario = driver.find_element(By.XPATH, "//*[@id='shippingAddress.address']")
    time.sleep(1)
    calle_destinatario.clear()
    calle_destinatario.send_keys("MOLDES")
    time.sleep(1)

    # Numero de domicilio del destinatario
    numero_domicilio = driver.find_element(By.XPATH, "//*[@id='shippingAddress.number']")
    time.sleep(1)
    numero_domicilio.clear()
    numero_domicilio.send_keys("2000")
    time.sleep(1)

    # Departamento del dom-destinatario
    departamento_destinatario = driver.find_element(By.XPATH, "//*[@id='shippingAddress.floor']")
    time.sleep(1)
    departamento_destinatario.clear()
    departamento_destinatario.send_keys("C")
    time.sleep(1)

    # Barrio destinatario
    barrio_destinatario = driver.find_element(By.XPATH, "//*[@id='shippingAddress.locality']")
    time.sleep(1)
    barrio_destinatario.clear()
    barrio_destinatario.send_keys("BELGRANO")
    time.sleep(1)

    # Datos de facturacion (DNI o CUIL)
    DNI_facturacion = driver.find_element(By.XPATH, "//*[@id='billingAddress.id_number']")
    time.sleep(1)
    DNI_facturacion.clear()
    DNI_facturacion.send_keys("95888999")
    time.sleep(1)

    # Continuar la compra
    continuar_compra = driver.find_element(By.XPATH, "//*[@id='main-column']/div[2]/form/button/span")
    time.sleep(2)
    continuar_compra.click()
    time.sleep(5)

    #Iframe metodos de pago
    driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='iFrameResizer0']"))
    time.sleep(2)
    #Elegir metodo de pago
    Efectivo = driver.find_element(By.ID, "radio-option-custom_payment_wire_transfer_production")
    time.sleep(2)
    Efectivo.click()
    time.sleep(2)
    driver.switch_to.default_content()
    
    #Realizar pedido - Finalizar
    Realizar_P = driver.find_element(By.XPATH, "//*[@id='btnFinishCheckout']/span")
    time.sleep(2)
    Realizar_P.click()
    time.sleep(1)

driver.close()