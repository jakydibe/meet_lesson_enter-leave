from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from time import sleep
import time
import datetime 
from datetime import time
from selenium.webdriver.chrome.options import Options



opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0, 
    "profile.default_content_setting_values.notifications": 1 
  })

tempo = input('scrivi qui l\' orario in cui entrare (es. 21:32:46)-----> \n')



user = input('immetti qui la tua mail-----> \n')
password = input('immetti qui la password della tua mail-----> \n')

print('una volta entrato in videochiamata ti verra\' chiesto se e con quanti partecipanti vuoi uscire dalla lezione\n')
link_meet = input('incolla qui il link della tua riunione meet-----> \n')

while True:
    orario_attuale = datetime.datetime.now()  
    culo = orario_attuale.strftime("%H:%M:%S")
    if tempo == culo:
        driver = webdriver.Chrome(options=opt, executable_path="C:/path/chromedriver.exe")
        driver.get("https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&_ga=2.204718480.146347229.1613226513-195929435.1613226513&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(user)
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
        sleep(2)
        driver.find_element_by_xpath ('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(password)
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
        sleep(2)
        driver.get(link_meet)
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div").click()
        driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div").click()
        sleep(2)       
        driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span").click() 
        sleep(2)
        break
    else:
        continue

scelta = input('\n\nvuoi uscire automaticamente dalla lezione quando il numero dei partecipanti si abbassa(aka tutti stanno salutando il prof.)? S/N, ATTENZIONE: SE METTI UN NUMERO TROPPO BASSO O COMUNQUE MINORE O UGUALE A QUELLO DEGLI ATTUALI PARTECIPANTI USCIRA\' AUTOMATICAMENTE\n')
while True:
    if scelta == 'S' or scelta == 's':
        richiesta_partecipanti = int(input('con quanti partecipanti rimasti vuoi automaticamente uscire?-----> '))
        while True:
            el_numero_partecipanti = int(driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[8]/div[3]/div[1]/div[3]/div/div[2]/div[1]/span/span/div/div/span[2]").text)
            if el_numero_partecipanti <= richiesta_partecipanti:
                driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div").click()
                break
            else:
                continue
    else:
        scelta_interna = input('ne se proprio sicuro?? S/N')
        if scelta_interna == 'S' or scelta_interna == 's':
            break
        else:
            continue
#aprire browser /// entrare e-mail //// entrare password .//// andare in link meet (https://meet.google.com/lookup/fubtul6aob?authuser=1&hs=179) //// individuare numero partecipanti

# se partecipanti > 10 entra,z\ poi se partecipanti minori di 16, esci.n