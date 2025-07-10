from datetime import datetime
current_datetime = str(datetime.now())
b=current_datetime.split("-")
c=b[0]
c=c[2:]
d=b[1]
e=b[2].split(" ")
f=e[0]
g=e[1]
kl=g.split(".")
io=kl[0]
start2=f+'/'+d+'/'+c+' '+io
start2= datetime.strptime(start2, '%d/%m/%y %H:%M:%S')
print(start2)


from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException


driver.set_window_size(1800, 1300) 



driver.get('https://yandex.ru/maps/213/moscow/?ll=37.729452%2C55.689740&z=13')
time.sleep(18)




driver.save_screenshot('screenshot.png')


from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
import time


# Путь к файлу изображения
image_path = 'screenshot.png'

# Настройка драйвера



# Открываем сайт postimages.org
driver.get('https://postimages.org/')

# Находим кнопку "Choose images" или input[type='file']
upload_input = driver.find_element(By.XPATH, '//input[@type="file"]')
upload_input.send_keys(image_path)

# Ждем завершения загрузки (можно подождать появления ссылки)
time.sleep(10)  # подождите, пока изображение загрузится

# Получаем ссылку на изображение
link_element = driver.find_element(By.XPATH, '//input[@id="code_html"]')
image_url = link_element.get_attribute('value')
print('Ссылка на изображение:', image_url)


driver.quit()

