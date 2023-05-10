import profile
from re import I
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import *
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from time import sleep, time
from colorama import Fore , init
import time
import random
import os
from colorama import init , Fore
import requests


#land rare /html/body/div/div/div[2]/div[2]/div[3]/div/section/div[54]
#land uncommon /html/body/div/div/div[2]/div[2]/div[3]/div/section/div[90]

# profile_path = r'C:\Users\Gastropoda\AppData\Roaming\Mozilla\Firefox\Profiles\o9urgzrk.test bot'
# options=Options()
# options.set_preference('profile', profile_path)
# service = Service(r'C:\Users\Gastropoda\Desktop\Sailors World\geckodriver.exe')
# driver = Firefox(service=service, options=options)

profilepath = r'C:\Users\Gastropoda\AppData\Roaming\Mozilla\Firefox\Profiles\o9urgzrk.test bot'
profile = webdriver.FirefoxProfile(profilepath)
option = webdriver.FirefoxOptions()
option.headless = True
driver = webdriver.Firefox(firefox_profile=profile , options=option )
init(autoreset=True)

token = 'c2mYbYkMhCMm7ymTlRJQdqZinCCxJS8kZ3sL4uIqqVy'   #line token


def clearpromp():
    clear = lambda: os.system('cls')
    clear()

def right_arrow():
    clicktomove = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]/div/div[2]/section/div[1]'))).click()
    
    for i in range(25):
        actions = ActionChains(driver)
        actions.key_down(Keys.ARROW_RIGHT).pause(0.01).key_up(Keys.ARROW_RIGHT)
        actions.perform()
        i += 1

def left_arrow():
    clicktomove = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]/div/div[2]/section/div[1]'))).click()
    
    for i in range(25):
        actions = ActionChains(driver)
        actions.key_down(Keys.ARROW_LEFT).pause(random.uniform(0.01, 0.011)).key_up(Keys.ARROW_LEFT)
        actions.perform()
        i += 1

def refresh():
    driver.refresh()
    time.sleep(7)
    try:
        logingameclick = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div[4]/button[1]'))).click()
    except:
        pass
    wait_game = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div[2]/section/div[1]/div[1]/div[3]/button')))
    Trawlclick = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/ul/li[2]/div'))).click()
    time.sleep(1)

def login():

    Gmail = 'Gastropoda1999@gmail.com'
    GmailPassword = 'M23037oo@'
    Securitypassword = 'Pi9ciB3T49'
    
    # driver.get('https://wallet.wax.io/dashboard')
    # loginGmailwax = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div[4]/div/div/div/div[1]/div[1]/input'))).send_keys(Gmail)
    # loginPasswordwax = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div[4]/div/div/div/div[1]/div[2]/input'))).send_keys(GmailPassword)
    # loginClicked = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div[4]/div/div/div/div[4]/button'))).click()
    # try:
    #     login2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/section/div[2]/div/div[3]/form/div[1]/div/input'))).send_keys(Securitypassword)
    #     login2clicked = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/section/div[2]/div/div[3]/form/div[3]/button/div'))).click()
    # except:
    #     pass
    # Waitlogin = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div[1]/img')))
    # print(Fore.YELLOW + 'Login wax success!')
    # print('')
    driver.get('https://sailorsworld.io/play')
    time.sleep(7)
    try:
        logingameclick = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div[4]/button[1]'))).click()
    except:
        pass
    wait_game = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div[2]/section/div[1]/div[1]/div[3]/button')))
    print(Fore.YELLOW + 'Login game success!')

class ships:
    def __init__(self,ships_position,rarity,land,select_reward):
        self.ships_position = ships_position
        self.rarity = rarity
        self.land = land
        self.select_reward = select_reward

class oilrig:
    def __init__(self,oilrig_button):
        self.oilrig_button = oilrig_button

if __name__ == '__main__':
    #land position
    land_rare = '/html/body/div/div/div[2]/div[2]/div[3]/div/section/div[54]' 
    land_uncommon = '/html/body/div/div/div[2]/div[2]/div[3]/div/section/div[90]'
    #reward
    Mine_Dub = '/html/body/div/div/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/div[1]/button'
    Mine_Wreck = '/html/body/div/div/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/button'

    ships_data_1 = ("/html/body/div/div/div[2]/div[2]/div[3]/div/div[2]/section/div[1]/div[1]/div[3]/button","rare",land_rare,Mine_Dub)
    ships_data_2 = ("/html/body/div/div/div[2]/div[2]/div[3]/div/div[2]/section/div[1]/div[2]/div[3]/button","rare",land_rare,Mine_Dub)
    ships_data_3 = ('/html/body/div/div/div[2]/div[2]/div[3]/div/div[2]/section/div[1]/div[3]/div[3]/button','uncommon',land_uncommon,Mine_Wreck)
    ships_data_4 = ('/html/body/div/div/div[2]/div[2]/div[3]/div/div[2]/section/div[1]/div[4]/div[3]/button','rare',land_rare,Mine_Wreck)
    ships_data_5 = ('/html/body/div/div/div[2]/div[2]/div[3]/div/div[2]/section/div[1]/div[5]/div[3]/button','rare',land_rare,Mine_Wreck)
    ships_data_6 = ('/html/body/div/div/div[2]/div[2]/div[3]/div/div[2]/section/div[1]/div[6]/div[3]/button','rare',land_rare,Mine_Wreck)
    ships_data_7 = ('/html/body/div/div/div[2]/div[2]/div[3]/div/div[2]/section/div[1]/div[7]/div[3]/button','uncommon',land_uncommon,Mine_Dub)
    ships_data_list = (ships_data_1,ships_data_2,ships_data_3,ships_data_4,ships_data_5,ships_data_6,ships_data_7)
    oil_rig_1 = ('/html/body/div/div/div[2]/div[2]/div[2]/div[2]/section/div[1]/div[1]/div[3]/button')
    oil_rig_2 = ('/html/body/div/div/div[2]/div[2]/div[2]/div[2]/section/div[1]/div[2]/div[3]/button')
    oil_rig_list = (oil_rig_1,oil_rig_2)
    Dub_path = '/html/body/div/div/div[2]/div[1]/div/div[1]/div/div'
    Wreck_path = '/html/body/div/div/div[2]/div[1]/div/div[2]/div/div'
    fuel_path = '/html/body/div/div/div[2]/div[1]/div/div[3]/div/div'
    tank_path = '/html/body/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]'

def game_ships():
    Trawlclick = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/ul/li[2]/div'))).click()
    left_arrow()
    print(Fore.LIGHTCYAN_EX +'Trawl Ships')
    print('')
    time.sleep(1)
   
    i = 0

    while i in range(len(ships_data_list)):
        if i in (0,1,2,6):  #ships 1,2,3,7
            ships_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, ships_data_list[i][0]))).text
            if ships_button in ('[Trawl]'):
                driver.find_element(By.XPATH, ships_data_list[i][0]).click()     #click ships botton
                time.sleep(1)
                print('Ship {} : Select land...'.format(i+1))
                Click_land = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, ships_data_list[i][2]))).click()     #select land
                print('Ship {} : Land selected !'.format(i+1))
                print('Ship {} : Select reward...'.format(i+1))
                wait_reward_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, ships_data_list[i][3]))).click()        #select reward
                print('Ship {} : Reward selected !'.format(i+1))
                time.sleep(13)
            elif ships_button in ('[Get reward]'):
                print('Ship {} : Collecting reward...'.format(i+1))
                driver.find_element(By.XPATH,ships_data_list[i][0]).click()
                Reward_ships = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]/div[2]/div/div[1]/p'))).text  #show reward
                if Reward_ships in ('[Refresh the page!]'):
                    print('Ships {} : {}'.format(i+1,Reward_ships))
                    print('Ships {} : Reward error refreshing...'.format(i+1))
                    payload = {'message' : '''
Ships {} : Reward Error , Refreshing...'''.format(i+1)}
                    r = requests.post('https://notify-api.line.me/api/notify'
                        , headers={'Authorization' : 'Bearer {}'.format(token)}
                        , params = payload)

                    refresh()
                    
                    DUB = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Dub_path))).text
                    WRECK = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Wreck_path))).text
                    FUEL = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, fuel_path))).text
                    TANK = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, tank_path))).text
                    
                    payload = {'message' : '''

Ship {} Reward

Balance

DUB 🪙 :  {}

Wreck 🪵 :  {}

Fuel ⛽ :  {}

Tank 🛢️ :  {}
                    '''.format(i+1,DUB,WRECK,FUEL,TANK)}
                    r = requests.post('https://notify-api.line.me/api/notify'
                        , headers={'Authorization' : 'Bearer {}'.format(token)}
                        , params = payload)
                else:
                    print('Ships {} : {}'.format(i+1,Reward_ships))
                    refresh()

                    DUB = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Dub_path))).text
                    WRECK = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Wreck_path))).text
                    FUEL = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, fuel_path))).text
                    TANK = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, tank_path))).text

                    payload = {'message' : 'Ship {} : {}'.format(i+1,Reward_ships)}
                    r = requests.post('https://notify-api.line.me/api/notify'
                        , headers={'Authorization' : 'Bearer {}'.format(token)}
                        , params = payload)
                    payload = {'message' : '''

Balance

DUB 🪙 :  {}

Wreck 🪵 :  {}

Fuel ⛽ :  {}

Tank 🛢️ :  {}
                    '''.format(DUB,WRECK,FUEL,TANK)}
                    r = requests.post('https://notify-api.line.me/api/notify'
                        , headers={'Authorization' : 'Bearer {}'.format(token)}
                        , params = payload)
            else:
                print('Ships {} cd : {}'.format(i+1,ships_button))

            time.sleep(1)
            i += 1
        elif i in (4,5):    #ships 5,6
            ships_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, ships_data_list[i][0]))).text
            if ships_button in ('[Trawl]'):
                driver.find_element(By.XPATH, ships_data_list[i][0]).click()     #click ships botton
                time.sleep(1)
                print('Ship {} : Select land...'.format(i+1))
                Click_land = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, ships_data_list[i][2]))).click()     #select land
                print('Ship {} : Land selected !'.format(i+1))
                print('Ship {} : Select reward...'.format(i+1))
                wait_reward_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, ships_data_list[i][3]))).click()        #select reward
                print('Ship {} : Reward selected !'.format(i+1))
                time.sleep(3)
                print('Refreshing...')
                refresh()
                right_arrow()
            elif ships_button in ('[Get reward]'):
                print('Ship {} : Collecting reward...'.format(i+1))
                driver.find_element(By.XPATH,ships_data_list[i][0]).click()
                Reward_ships = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]/div[2]/div/div[1]/p'))).text  #show reward
                if Reward_ships in ('[Refresh the page!]'):
                    print('Ships {} : {}'.format(i+1,Reward_ships))
                    print('Ships {} : Reward error refreshing...'.format(i+1))
                    payload = {'message' : '''
Ships {} : Reward Error , Refreshing...'''.format(i+1)}
                    r = requests.post('https://notify-api.line.me/api/notify'
                        , headers={'Authorization' : 'Bearer {}'.format(token)}
                        , params = payload)

                    refresh()
                    
                    DUB = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Dub_path))).text
                    WRECK = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Wreck_path))).text
                    FUEL = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, fuel_path))).text
                    TANK = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, tank_path))).text
                    
                    payload = {'message' : '''

Ship {} Reward

Balance

DUB 🪙 :  {}

Wreck 🪵 :  {}

Fuel ⛽ :  {}

Tank 🛢️ :  {}
                    '''.format(i+1,DUB,WRECK,FUEL,TANK)}
                    r = requests.post('https://notify-api.line.me/api/notify'
                        , headers={'Authorization' : 'Bearer {}'.format(token)}
                        , params = payload)
                else:
                    print('Ships {} : {}'.format(i+1,Reward_ships))
                    refresh()

                    DUB = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Dub_path))).text
                    WRECK = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Wreck_path))).text
                    FUEL = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, fuel_path))).text
                    TANK = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, tank_path))).text

                    payload = {'message' : 'Ship {} : {}'.format(i+1,Reward_ships)}
                    r = requests.post('https://notify-api.line.me/api/notify'
                        , headers={'Authorization' : 'Bearer {}'.format(token)}
                        , params = payload)
                    payload = {'message' : '''

Balance

DUB 🪙 :  {}

Wreck 🪵 :  {}

Fuel ⛽ :  {}

Tank 🛢️ :  {}
                    '''.format(DUB,WRECK,FUEL,TANK)}
                    r = requests.post('https://notify-api.line.me/api/notify'
                        , headers={'Authorization' : 'Bearer {}'.format(token)}
                        , params = payload)
                right_arrow()
            else:
                print('Ships {} cd : {}'.format(i+1,ships_button))
            time.sleep(1)
            i += 1
        elif i == 3:    #ship 4
            ships_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, ships_data_list[i][0]))).text
            if ships_button in ('[Trawl]'):
                driver.find_element(By.XPATH, ships_data_list[i][0]).click()     #click ships botton
                time.sleep(1)
                print('Ship {} : Select land...'.format(i+1))
                Click_land = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, ships_data_list[i][2]))).click()     #select land
                print('Ship {} : Land selected !'.format(i+1))
                print('Ship {} : Select reward...'.format(i+1))
                wait_reward_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, ships_data_list[i][3]))).click()        #select reward
                print('Ship {} : Reward selected !'.format(i+1))
                time.sleep(13)
            elif ships_button in ('[Get reward]'):
                print('Ship {} : Collecting reward...'.format(i+1))
                driver.find_element(By.XPATH,ships_data_list[i][0]).click()
                Reward_ships = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]/div[2]/div/div[1]/p'))).text  #show reward
                if Reward_ships in ('[Refresh the page!]'):
                    print('Ships {} : {}'.format(i+1,Reward_ships))
                    print('Ships {} : Reward error refreshing...'.format(i+1))
                    payload = {'message' : '''
Ships {} : Reward Error , Refreshing...'''.format(i+1)}
                    r = requests.post('https://notify-api.line.me/api/notify'
                        , headers={'Authorization' : 'Bearer {}'.format(token)}
                        , params = payload)

                    refresh()
                    
                    DUB = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Dub_path))).text
                    WRECK = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Wreck_path))).text
                    FUEL = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, fuel_path))).text
                    TANK = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, tank_path))).text
                    
                    payload = {'message' : '''

Ship {} Reward

Balance

DUB 🪙 :  {}

Wreck 🪵 :  {}

Fuel ⛽ :  {}

Tank 🛢️ :  {}
                    '''.format(i+1,DUB,WRECK,FUEL,TANK)}
                    r = requests.post('https://notify-api.line.me/api/notify'
                        , headers={'Authorization' : 'Bearer {}'.format(token)}
                        , params = payload)
                else:
                    print('Ships {} : {}'.format(i+1,Reward_ships))
                    refresh()

                    DUB = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Dub_path))).text
                    WRECK = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Wreck_path))).text
                    FUEL = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, fuel_path))).text
                    TANK = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, tank_path))).text

                    payload = {'message' : 'Ship {} : {}'.format(i+1,Reward_ships)}
                    r = requests.post('https://notify-api.line.me/api/notify'
                        , headers={'Authorization' : 'Bearer {}'.format(token)}
                        , params = payload)
                    payload = {'message' : '''

Balance

DUB 🪙 :  {}

Wreck 🪵 :  {}

Fuel ⛽ :  {}

Tank 🛢️ :  {}
                    '''.format(DUB,WRECK,FUEL,TANK)}
                    r = requests.post('https://notify-api.line.me/api/notify'
                        , headers={'Authorization' : 'Bearer {}'.format(token)}
                        , params = payload)
            else:
                print('Ships {} cd : {}'.format(i+1,ships_button))
            time.sleep(1)
            right_arrow()
            i += 1
        else:
            pass

def game_oilrig():
    print(Fore.LIGHTGREEN_EX +'Oil Rig')
    print('')
    Oilrigclick = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/ul/li[4]/div'))).click()
    time.sleep(1)
    #oilrig 1
    oil_rig_1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div[2]/section/div[1]/div[1]/div[3]/button'))).text

    if oil_rig_1 in ('[Pump]'):
        driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div[2]/div[2]/section/div[1]/div[1]/div[3]/button').click()     #click oilrig botton
        print('oil rig 1 : mined !')
        DUB = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Dub_path))).text
        WRECK = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Wreck_path))).text
        FUEL = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, fuel_path))).text
        TANK = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, tank_path))).text
        payload = {'message' : 'Oil Rig 1 : Mined !'}
        r = requests.post('https://notify-api.line.me/api/notify'
            , headers={'Authorization' : 'Bearer {}'.format(token)}
            , params = payload)
        payload = {'message' : '''

Balance

DUB 🪙 :  {}

Wreck 🪵 :  {}

Fuel ⛽ :  {}

Tank 🛢️ :  {}
            '''.format(DUB,WRECK,FUEL,TANK)}
        r = requests.post('https://notify-api.line.me/api/notify'
            , headers={'Authorization' : 'Bearer {}'.format(token)}
            , params = payload)
        time.sleep(10)
    else:
        oil_rig_1_split = oil_rig_1.split()
        print('Oil Rig 1 cd :',oil_rig_1_split[1])

    time.sleep(1)

    oil_rig_2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div[2]/section/div[1]/div[2]/div[3]/button'))).text

    if oil_rig_2 in ('[Pump]'):
        driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div[2]/div[2]/section/div[1]/div[2]/div[3]/button').click()     #click oilrig botton
        print('oil rig 2 : mined !')
        DUB = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Dub_path))).text
        WRECK = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Wreck_path))).text
        FUEL = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, fuel_path))).text
        TANK = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, tank_path))).text
        payload = {'message' : 'Oil Rig 2 : Mined !'}
        r = requests.post('https://notify-api.line.me/api/notify'
            , headers={'Authorization' : 'Bearer {}'.format(token)}
            , params = payload)
        payload = {'message' : '''

Balance

DUB 🪙 :  {}

Wreck 🪵 :  {}

Fuel ⛽ :  {}

Tank 🛢️ :  {}
            '''.format(DUB,WRECK,FUEL,TANK)}
        r = requests.post('https://notify-api.line.me/api/notify'
            , headers={'Authorization' : 'Bearer {}'.format(token)}
            , params = payload)
        time.sleep(10)
    else:
        oil_rig_2_split = oil_rig_2.split()
        print('Oil Rig 2 cd :',oil_rig_2_split[1])
        
def refuel():
    fuel = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]'))).text
    if fuel in ('[500 / 500]'):
        print(fuel)
    else:
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div[4]/div[3]/img').click()
        driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[1]/div[1]/div/div[2]/button').click()

def resource():
    DUB = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Dub_path))).text
    WRECK = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Wreck_path))).text
    FUEL = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, fuel_path))).text
    TANK = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, tank_path))).text
    print(Fore.LIGHTMAGENTA_EX +'Balance')
    print('')
    print(Fore.LIGHTYELLOW_EX +('DUB : '+DUB))
    print(Fore.RED +('Wreck : '+WRECK))
    print(Fore.LIGHTRED_EX +('Fuel : '+FUEL))
    print(Fore.LIGHTBLACK_EX +('Tank : '+TANK))

#call function
clearpromp()
print(Fore.LIGHTRED_EX +'Bot Starting...')
print('')

payload = {'message' : 'Bot Starting...'}
r = requests.post('https://notify-api.line.me/api/notify'
                , headers={'Authorization' : 'Bearer {}'.format(token)}
                , params = payload)

login()

while True:
    game_ships()
    print('')
    # print('--------------------------')
    # print('')
    # game_oilrig()
    # time.sleep(1)
    # print('')
    print('--------------------------')
    print('')
    resource()
    print('')
    print('--------------------------')
    print('')