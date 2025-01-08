import streamlit as st
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--diable-dve-shm-uage')
driver = webdriver.Chrome(options=options)

driver.get("https://community.amd.com/t5/pc-processors/cpu-overheating-mystery/td-p/679185")
st.code(driver.page_source)
