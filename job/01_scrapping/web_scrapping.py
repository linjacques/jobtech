import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
# Lancer Chrome
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # adapte si besoin
options.add_argument('--headless')  # facultatif
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

results = []
nb_pages = 5  # Nombre de pages à parcourir
for page in range(1, nb_pages + 1):
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        url = f"https://www.welcometothejungle.com/fr/jobs?query=tech&refinementList%5Boffices.country_code%5D%5B%5D=FR&refinementList%5Bhas_salary_yearly_minimum%5D%5B%5D=1&collections%5B%5D=has_salary&page={page}"
        driver.get(url)
        time.sleep(2)
        SCROLL_PAUSE_TIME = 1
        last_height = driver.execute_script("return document.body.scrollHeight")
        max_scrolls = 3
        for _ in range(max_scrolls):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height: 
                break
            last_height = new_height
        offer_blocks = driver.find_elements(By.CSS_SELECTOR, 'div[data-role="jobs:thumb"]')
        if not offer_blocks:
            driver.quit()
            break
        for block in offer_blocks:
            title = ''
            try:
                h2 = block.find_element(By.XPATH, './/h2')
                div_mark = h2.find_element(By.XPATH, './/div[@role="mark"]')
                title = div_mark.text.strip()
            except Exception:
                try:
                    h2 = block.find_element(By.XPATH, './/h2')
                    title = h2.text.strip()
                except Exception:
                    title = ''
            company = ''
            contract = ''
            remote = ''
            city = ''
            try:
                parent = block.find_element(By.XPATH, './/div[contains(@class, "sc-brzPDJ") and .//span[contains(@class, "wui-text")]]')
                company_span = parent.find_element(By.CSS_SELECTOR, 'span.wui-text')
                company = company_span.text.strip()
                icons = block.find_elements(By.CSS_SELECTOR, 'i.wui-icon-font')
                for icon in icons:
                    name = icon.get_attribute('name')
                    if name == 'contract':
                        contract_span = icon.find_element(By.XPATH, 'following-sibling::span[1]')
                        contract = contract_span.text.strip()
                    if name == 'remote':
                        remote_span = icon.find_element(By.XPATH, 'following-sibling::span[1]')
                        remote = remote_span.text.strip()
                    if name == 'location':
                        try:
                            p = icon.find_element(By.XPATH, 'following-sibling::p[1]')
                            city_span = p.find_element(By.XPATH, './/span[last()]')
                            city = city_span.text.strip()
                        except Exception:
                            pass
            except Exception:
                pass
            salaire = ''
            try:
                # Cherche l'icône salaire et prend le span frère
                salary_icon = block.find_element(By.CSS_SELECTOR, 'i.wui-icon-font[name="salary"]')
                salary_span = salary_icon.find_element(By.XPATH, 'following-sibling::span[1]')
                salaire = salary_span.text.strip()
            except Exception:
                pass
            results.append({
                'titre_metier': title,
                'entreprise': company,
                'salaire': salaire,
                'contract': contract,
                'remote': remote,
                'ville': city
            })
        driver.quit()
    except Exception as e:
        print(f"Erreur sur la page {page}: {e}")
        try:
            driver.quit()
        except:
            pass
        continue

with open('data/raw/offres_tech_wttj.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['titre_metier', 'entreprise', 'salaire', 'contract', 'remote', 'ville']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for r in results:
        writer.writerow(r)

for r in results:
    print(r)

driver.quit()
