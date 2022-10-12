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

# Link for Girona vs RM
gir = 'https://proticketing.com/realmadrid_ligavip/es_ES/entradas/evento/26217/session/1498130/select'

# Link for BCN vs RM
bcn = 'https://proticketing.com/realmadrid_futbol/es_ES/entradas/evento/26217/session/1509865/select?_ga=2.98927902.166602286.1665487877-1652816915.1665487876'


# Creates driver, visits website, tries to click on avaialbe seats
def buscar_boleta(url_partido):
    
    # Select navigator TO DO ==> cache this
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    # Visit direct queue
    driver.get(url_partido)
    
    # Maximises the window
    driver.maximize_window()

    # # Dismiss cookies
    cookie = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/button[1]"))
        )

    cookie.click()
    driver.execute_script("window.scrollTo(0, 300)") 

    # Function to try and click an available zone, returns False if there are not tickets.
    def boleta_disponible():
        try: 
            localidad = driver.find_element(By.CSS_SELECTOR,'[class="interactive"]')
            localidad.click() 
        except:
            return False
        else:
            return True
        
    # Selects stadium section
    def seccion():
        driver.execute_script("window.scrollTo(0, 400)") 
        seccion = driver.find_element(By.CSS_SELECTOR,'[class="interactive"]')
        seccion.click()
        
    # Selects the available seat
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
    # Current time during search
        current = time.time()
    # If more than 310 seconds (5 mins) have passed, close everything.
        if current > start + 310:
            driver.quit()
            for i in range(0,3):
                winsound.Beep(440, 500)
            sys.exit(0)
        else:
            driver.execute_script("window.scrollTo(0, 650)")
            hay = boleta_disponible()
    
    # If a ticket is found, it attempts to click on the empty seat and launches sound feedback.
    else:
        winsound.Beep(450, 1000)
        time.sleep(0.8)
        seccion()
        time.sleep(0.8)
        silla()
        return 'Hay'

# Loops forever or until exit
while True:
    buscar_boleta(bcn)
    time.sleep(1)
    