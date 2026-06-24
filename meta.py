from crawlerkit import Spider
from selenium.webdriver.common.by import By


class QuotesSpider(Spider):
    def run(self) -> None:
        with self.driver(headless=True) as d:
            d.get("https://quotes.toscrape.com/")
            quote = d.find_element(By.CLASS_NAME, "quote").text
            self.screenshot("home", d.get_screenshot_as_png(), url=d.current_url)
            self.item({
                "url": d.current_url,
                "quote": quote,
            })
