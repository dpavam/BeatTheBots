# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 13:27:32 2022

@author: dpava
"""
import sys
import schedule
import winsound
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


gir = 'https://proticketing.com/realmadrid_ligavip/es_ES/entradas/evento/26217/session/1498130/select'

bcn = 'https://proticketing.com/realmadrid_futbol/es_ES/entradas/evento/26217/session/1509865/select?_ga=2.98927902.166602286.1665487877-1652816915.1665487876'



def buscar_boleta(url_partido):
    
    # Select navigator TO DO ==> cache this
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    # Visit direct queue
    driver.get(url_partido)
    
    driver.maximize_window()

    # # Dismiss cookies
    cookie = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/button[1]"))
        )

    cookie.click()
    driver.execute_script("window.scrollTo(0, 300)") 

        # Function to check each zone 
    def boleta_disponible():
        try: 
            localidad = driver.find_element(By.CSS_SELECTOR,'[class="interactive"]')
            localidad.click() 
        except:
            return False
        else:
            return True

    def seccion():
        driver.execute_script("window.scrollTo(0, 400)") 
        seccion = driver.find_element(By.CSS_SELECTOR,'[class="interactive"]')
        seccion.click()
        
    def silla():
        silla = driver.find_element(By.CSS_SELECTOR,'[class="interactive available-seat"]')
        silla.click()
        
    #Time started searching
    start = time.time()
    
    
    #  Trying to loop until it finds an open spot
    hay = boleta_disponible()
    while hay == False:
        time.sleep(2)
        driver.refresh()
        time.sleep(1)
        current = time.time()
        if current > start + 330:
            driver.quit()
            for i in range(0,3):
                winsound.Beep(440, 500)
            sys.exit(0)
        else:
            driver.execute_script("window.scrollTo(0, 650)")
            hay = boleta_disponible()
        
    else:
        winsound.Beep(450, 1000)
        time.sleep(0.8)
        seccion()
        time.sleep(0.8)
        silla()
        return 'Hay'

while True:
    buscar_boleta(bcn)
    time.sleep(1)
    