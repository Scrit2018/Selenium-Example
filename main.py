from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_kitapyurdu_books():
    # Firefox sürücüsünü başlat
    driver = webdriver.Firefox()

    # Kitapyurdu ana sayfasına git
    driver.get("https://www.kitapyurdu.com/")

    # Arama çubuğuna "python" yaz ve enter'a bas
    arama_cubugu = driver.find_element(By.ID, "search-input")
    arama_cubugu.send_keys("python")
    arama_cubugu.submit()

    # Sayfanın yüklenmesini bekle
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.product-list")))

    # Kitapların listesini al
    kitaplar = driver.find_elements(By.CSS_SELECTOR, "ul.product-list li")

    # Her kitap için bilgi yazdır
    for kitap in kitaplar:
        baslik = kitap.find_element(By.CSS_SELECTOR, "h3 a").text
        yazar = kitap.find_element(By.CSS_SELECTOR, "div.author a").text
        fiyat = kitap.find_element(By.CSS_SELECTOR, "span.price").text

        print(f"**Başlık:** {baslik}")
        print(f"**Yazar:** {yazar}")
        print(f"**Fiyat:** {fiyat}")
        print("-" * 20)

    # Sürücüyü kapat
    driver.quit()

# Fonksiyonu çalıştır
get_kitapyurdu_books()