# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)

# account = driver.find_element_by_css_selector("[id='menu-item-50']>a").click()
# email = driver.find_element_by_id("reg_email")
# email.send_keys("ben@mail.ru")
# password = driver.find_element_by_id("reg_password")
# password.send_keys("Benmail2023")
# reg = driver.find_element_by_name("register").click()
# driver.quit()

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# account = driver.find_element_by_css_selector("[id='menu-item-50']>a").click()
# username = driver.find_element_by_id("username")
# username.send_keys("ben@mail.ru")
# pas = driver.find_element_by_id("password")
# pas.send_keys("Benmail2023")
# login = driver.find_element_by_name("login").click()
# logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation-link--customer-logout>a")
# logout_get_text = logout.text
# assert logout_get_text == "Logout"
# driver.quit()