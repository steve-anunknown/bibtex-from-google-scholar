import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def get_pdf_filenames(pdf_dir):
    names = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
    # replace dashes with spaces
    names = [name.replace('-', ' ') for name in names]
    return names


def search_google_scholar(filename, driver):
    search_url = "https://scholar.google.com/"
    driver.get(search_url)
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys(filename)
    search_box.send_keys(Keys.RETURN)


def get_bibtex_from_search_results(driver):
    try:
        # Wait until the search results are loaded
        search_results = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.gs_r.gs_or.gs_scl"))
        )

        if search_results:
            # Locate the first result's "Cite" button using a more specific selector
            cite_button = driver.find_element(By.XPATH, "//a[contains(@class, 'gs_or_cit gs_or_btn gs_nph')]")
            cite_button.click()

            # Wait until the URL changes indicating that the citation modal is open
            WebDriverWait(driver, 10).until(
                EC.url_contains("#d=gs_cit")
            )

            # Wait until the "BibTeX" link is clickable
            bibtex_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "BibTeX"))
            )
            bibtex_link.click()

            # Wait until the BibTeX text is visible
            bibtex_text = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.TAG_NAME, "pre"))
            ).text
            return bibtex_text
        else:
            print("No search results found.")
            return None
    except Exception as e:
        print(f"Error getting BibTeX: {e}")
        return None


def main(pdf_dir):
    pdf_files = get_pdf_filenames(pdf_dir)
    # Initialize the WebDriver
    service = Service(executable_path='/home/stefanos/Downloads/zips/chromedriver-linux64/chromedriver')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    for pdf_file in pdf_files:
        filename_without_extension = os.path.splitext(pdf_file)[0]
        try:
            search_google_scholar(filename_without_extension, driver)
            bibtex = get_bibtex_from_search_results(driver)
            if bibtex:
                print(bibtex)
            else:
                print(f"No BibTeX found for {pdf_file}")
        except Exception as e:
            print(f"Error processing {pdf_file}: {e}")
    driver.quit()


if __name__ == "__main__":
    # for every directory in the present working directory
    for directory in os.listdir(os.getcwd()):
        if os.path.isdir(directory):
            main(directory)
