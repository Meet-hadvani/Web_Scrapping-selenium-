from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


def extract_top_news():
    """Scrape all top news from the Hacker News website"""
    data = []
    driver = webdriver.Safari()
    driver.get('https://news.ycombinator.com/')

    # Select all news elements with the correct CSS selector for the title links
    element_list = driver.find_elements(By.CSS_SELECTOR, 'span.titleline a')

    for element in element_list:
        try:
            title = element.text
            title_url = element.get_attribute('href')
            data.append((title, title_url))
        except Exception as e:
            print(f"Error processing element: {e}")

    # Define headers
    headers = ['Title', 'Title_URL']

    # Writing to CSV using UTF-8 encoding
    with open('write_data_1.csv', mode='w', newline='', encoding='utf-8') as data_file:
        writer = csv.writer(data_file)
        writer.writerow(headers)
        writer.writerows(data)

    driver.quit()

if __name__ == '__main__':
    extract_top_news()
