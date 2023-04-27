# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
import time

# account = driver.find_element_by_css_selector("[id='menu-item-50']>a").click()
# username = driver.find_element_by_id("username")
# username.send_keys("ben@mail.ru")
# pas = driver.find_element_by_id("password")
# pas.send_keys("Benmail2023")
# login = driver.find_element_by_name("login").click()
# shop = driver.find_element_by_css_selector("[id='menu-item-40']>a").click()
# book = driver.find_element_by_css_selector(".post-181 img").click()
# h= driver.find_element_by_css_selector(".product_title.entry-title")
# h_get_text = h.text
# assert h_get_text == "HTML5 Forms"
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
# shop = driver.find_element_by_css_selector("[id='menu-item-40']>a").click()
# html = driver.find_element_by_css_selector(".cat-item.cat-item-19 a").click()
# items_count = driver.find_elements(By.CLASS_NAME,"attachment-shop_catalog")
# if len(items_count) == 3:
#     print("Отображается 3 товара")
# else:
#     print("Ошибка. Количество товаров на странице: " + str(len(items_count)))
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
# shop = driver.find_element_by_css_selector("[id='menu-item-40']>a").click()
# element = driver.find_element_by_css_selector(".orderby")
# element_checked = element.get_attribute("value")
# print("value of selector: ", element_checked)
# if element_checked == "menu_order":
#     print("сортировка по умолчанию")
# else:
#     print("другой вид сортировки")
# select = Select(element)
# select.select_by_value("price-desc")
# element = driver.find_element_by_css_selector(".orderby")
# element_checked = element.get_attribute("value")
# print("value of selector: ", element_checked)
# if element_checked == "price-desc":
#     print("сортировкf по цене от большей к меньшей")
# else:
#     print("другой вид сортировки")
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
#
# account = driver.find_element_by_css_selector("[id='menu-item-50']>a").click()
# username = driver.find_element_by_id("username")
# username.send_keys("ben@mail.ru")
# pas = driver.find_element_by_id("password")
# pas.send_keys("Benmail2023")
# login = driver.find_element_by_name("login").click()
# shop = driver.find_element_by_css_selector("[id='menu-item-40']>a").click()
# book = driver.find_element_by_css_selector(".post-169 img").click()
# price_old = driver.find_element_by_css_selector(".price :nth-child(1) span")
# price_old_get_text = price_old.text
# assert price_old_get_text == "₹600.00"
# price_new = driver.find_element_by_css_selector(".price :nth-child(2) span")
# price_new_get_text = price_new.text
# assert price_new_get_text == "₹450.00"
# book_cover = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_cover.click()
# book_cover_close = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))
# )
# book_cover_close.click()
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
# shop = driver.find_element_by_css_selector("[id='menu-item-40']>a").click()
# book = driver.find_element_by_class_name("post-165").click()
# cart = driver.find_element_by_css_selector(".cart button").click()
# cart_1 = driver.find_element_by_class_name("cartcontents")
# cart_1_get_text = cart_1.text
# assert cart_1_get_text == "1 Item"
# cart_2 = driver.find_element_by_class_name("amount")
# cart_2_get_text = cart_2.text
# assert cart_2_get_text == "₹350.00"
# basket = driver.find_element_by_id("wpmenucartli").click()
# subtotal = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal :nth-child(2) span"), "₹350.00"))
# total = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total :nth-child(2) span"), "₹357.00"))
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
#
# shop = driver.find_element_by_css_selector("[id='menu-item-40']>a").click()
# driver.execute_script("window.scrollBy(0, 300);")
# book = driver.find_element_by_css_selector(".post-165 .button").click()
# time.sleep(3)
# cart = driver.find_element_by_id("wpmenucartli").click()
# book_delete = driver.find_element_by_css_selector(".cart_item .remove").click()
# book_undo = driver.find_element_by_link_text("Undo?").click()
# quantity_clear = driver.find_element_by_css_selector(".quantity input").clear()
# book_quantity = driver.find_element_by_css_selector(".quantity input")
# book_quantity.send_keys(3)
# btn_update = driver.find_element_by_css_selector("[value='Update Basket']").click()
# time.sleep(2)
# btn_coupon = driver.find_element_by_css_selector(".coupon .button").click()
# error_window = driver.find_element_by_css_selector(".woocommerce-error li")
# error_window_get_text = error_window.text
# assert error_window_get_text == "Please enter a coupon code."
#
# driver.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)

shop = driver.find_element_by_css_selector("[id='menu-item-40']>a").click()
driver.execute_script("window.scrollBy(0, 300);")
book = driver.find_element_by_css_selector(".post-165 .button").click()
time.sleep(3)
cart = driver.find_element_by_id("wpmenucartli").click()
checkout_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout a")))
checkout_btn.click()
firstname= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))
firstname.send_keys("Ben")
lastname = driver.find_element_by_id("billing_last_name")
lastname.send_keys("Smith")
email = driver.find_element_by_id("billing_email")
email.send_keys("Ben@mail.ru")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("89118765432")
country_select = driver.find_element_by_id("s2id_billing_country").click()
country_choice = driver.find_element_by_id("s2id_autogen1_search")
country_choice.send_keys("belgium")
country = driver.find_element_by_id("select2-results-1").click()
adress = driver.find_element_by_id("billing_address_1")
adress.send_keys("Street")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("123456")
city = driver.find_element_by_id("billing_city")
city.send_keys("Brussel")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
check_payments = driver.find_element_by_id("payment_method_cheque").click()
placeorder = driver.find_element_by_id("place_order").click()
message = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
payment_method = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method strong"), "Check Payments"))

driver.quit()






