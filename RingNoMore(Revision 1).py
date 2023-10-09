# RingNoMore - Designed to Shutoff Ring Cameras
# Source Code: Trentyne Morgan
# Version 1.0 created on July, 08, 2021

# External Files (unused)
configFile = "rnmRouterConfig.cfg"          # Router Portal Settings File
applicationSettings = "rnmPreferences.cfg"  # User Preferences

# Router Portal Info
routerPortalIPAddr = '192.168.0.1'          # Local IP Address for Most Router Login pages  
routerPortalPasswd = 'password'             # Router Password
routerPortalUsername = 'username'           # Router Username

# Ring Camera Info
ringCameraMACAddr = "D4:36:XX:XX:XX:XX"     # MAC Address for Ring Camera 
ringCameraStatus = "Uninitialized"          # Status (leave as uninitialized on first use)

# Import Needed Modules
import time
from selenium import webdriver                          # Webdriver Main Module
from selenium.webdriver.common.keys import Keys         # Used to simulate keypresses
from selenium.webdriver.chrome.options import Options   # Used to run ChromeDriver "Headless"

# TODO:
# 1. ) Start webdriver headlessly (chromedriver)
# 2.) login using hardcoded router info
# 3.) Go to MAC Blacklist menu, and blacklist it

# Disable Ring
def disableRing():
    # Start Webdriver, if successful, move to navigation. if not, throw an error here.
    print("Starting Webdriver...")

    # Arguments/Options for Webdriver
    # chrome_options.add_argument("--disable-extentions")  # Disable Chrome Extentions for Performance
    # chrome_options.add_argument("--disable-gpu")         # Disable GPU Process (no-GUI)
    # chrome_options.add_argument("--headless")            # Run with no Window (same as above, really but slightly different)

    # Start a webdriver, with specified arguments
    try:
        driver = webdriver.Chrome(chromedriver.exe options=chrome_options)
        start_url = "https://192.168.0.1/router.html?wifi_mac"
        time.sleep(10)  # Wait for webpage
    except:
        print("Error: Webdriver did not start.")

    # Load driver with start page
    try:
        driver.get(start_url)
    except:
        print("Router Portal page not reachable..?")

    # Locate Page Elements
    try:
         usernameElement = driver.find_element_by_id("UserName")
         passwordElement = driver.find_element_by_id("Password")
    except:
        print("Login Elements not found.")

    # Send Login Request to webpage
    try:
        usernameElement.send_keys(routerPortalUsername)
        passwordElement.send_keys(routerPortalPassword)
        passwordElement.send_keys(Keys.RETURN)
    except:
        print("Error sending router login information")

    # Wait for 10 seconds before next navigate
    time.sleep(10)

    # Click on Add MAC Address
    try:
        macAddButton = driver.find_element_by_id("Mac_Add")
        macAddbutton.click()
    except:
        print("Error adding MAC Address to Blacklist.")

    # Enter MAC Address into TextBox
    try:
        macAddTextBox = driver.find_element_by_id("MacAddress")
        macAddTextBox.send_keys(ringCameraMACAddr)
        macSubmit = driver.find_element_by_class_name("ui-button-text")
        macSubmit.click()
    except:
        print("Error Sending Blacklist Request")
        

# Disable Ring Menu
def disableRingMenu():
    print("=== Ring Disable Functions ===")
    print("1.) Disable Ring Camera Permenantly  *no worries, you can enable in the main menu later*")
    print("2.) Disable Ring Camera for specified time")
    print("3.) Disable Ring Camera on arrival of Package/Mail")
    menuchoice = input("Type Selection Number:> ")
    if menuchoice == "1":
        disableRing()
    elif menuchoice == "2":
        timeDisableRing()
    elif menuchoice == "3":
        mailDisableRing()
    else:
        print("Invalid Response Entered.")
        disableRingMenu()
        
# Main Menu
def mainMenu():
    print("==== Main Menu ====")
    print("1.) Disable Ring Camera")
    print("2.) Enable Ring Camera")
    menuchoice = input("Type Selection Number:> ")
    if menuchoice == "1":
        disableRingMenu()
    elif menuchoice == "2":
        enableRingMenu()
    else:
        print("Invalid Response Entered.")
        disableRingMenu()

# Program Start
# (startup functions go here)
def programStart():
    print("========RingNoMore========\nVersion 1.0 by Trentyne Morgan\nCurrent Ring Status: "+ ringCameraStatus)
    # Bring up Main Menu
    mainMenu()

programStart()



