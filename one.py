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



driver.get('https://yandex.ru/maps/213/moscow/routes/bus_e10/796d617073626d313a2f2f7472616e7369742f6c696e653f69643d32303336393236373633266c6c3d33372e35313934373025324335352e363737353831266e616d653d254430254235313026723d313230303026747970653d627573/?ll=37.513205%2C55.666250&tab=stops&z=15')
time.sleep(18)




driver.save_screenshot('screenshot.png')





driver.quit()

