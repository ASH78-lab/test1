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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.set_window_size(1800, 1000) 

driver.set_window_size(1800, 800) 

driver.get("https://www.meteopt.com/modelos/gfs?lat=55.752&lon=37.616&lang=en")
time.sleep(8)
data=[]
button = driver.find_element(By.XPATH,"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[1]/div[3]/button")
driver.execute_script("arguments[0].click();", button)
time.sleep(5)
for i in range(1,9):
    e0 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[1]")
    e=int(e0.text)
    
    e2 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[2]")
    e20=e2.text
    e21=e20.split(', ')
    e22=e21[1]
    e23=e22.split(' ')
    e24=e23[0]
    
    e25=e23[1]
    if e25=="Jan":
        e25='01'
    if e25=="Feb":
        e25='02'
    if e25=="May":
        e25='05'
    e28=e23[2]
    e29=e28[:2]
    e27=e24+'-'+e25+'-'+'2025'+" "+e29+":00:00"

    
    e3 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr[{i}]/td[3]")
    e30=e3.text
    e31=e30.split()
    e32=e31[0]

    
    e4 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr[{i}]/td[3]/span").get_attribute('style')
    e40=e4.split('rotate(')
    e41=e40[1]
    e42=e41.split('deg);')
    e43=e42[0]

    
    e5 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr[{i}]/td[4]")
    e50=e5.text
    e51=e50.split()
    e52=e51[0]
    
    e6 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr[{i}]/td[4]/span").get_attribute('style')
    e60=e6.split('rotate(')
    e61=e60[1]
    e62=e61.split('deg);')
    e63=e62[0]
    
    e7 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[5]")
    e8 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[6]")
    e9 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[7]")
    e10 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[8]")
    e11 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[9]")
    e12 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[10]")
    e13 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[11]")
    e14 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[12]")
    e15 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[13]")
    e16 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[14]")
    e17 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[15]")
    e18 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[16]")
    e19 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[17]")
    e200 = driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div/div/div/div/div/div/div/div/span/div/div[4]/div[2]/table/tbody/tr{[i]}/td[18]")
 

    data.append([e,e27,int(e32),int(e43),int(e52),int(e63),float(e7.text),float(e8.text),int(e9.text),float(e10.text),int(e11.text),int(e12.text),int(e13.text),float(e14.text),int(e15.text),float(e16.text),float(e17.text),float(e18.text),int(e19.text),int(e200.text)])
header = ['Steps',
'Date/Hour',
'W.10m',
'W.10m2',          
'W.850',
'W.8502',
'Prec.',
'PWAT',
'CAPE',
'LI',
'Z500-1000',
'Geop.850',
'Geop.500',
'T.2m',
'RH.2m',
'T.850',
'T.500',
'Pressure',
'Clouds',
'SnowLn']

import pandas as pd
df = pd.DataFrame(data, columns=header)
del df['Date/Hour']

#df.to_excel('/Users/JOHN/Desktop/resurses/weather289.xlsx', sheet_name='Budgets', index=False)
driver.quit()

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