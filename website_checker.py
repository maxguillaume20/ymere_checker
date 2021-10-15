from selenium.webdriver import Firefox
from bs4 import BeautifulSoup
import time


class WebsiteChecker(object):

    def __init__(self):
        self.driver = None
        self.search_url = ''
        self.listings_search = {}
        self.previous_listings_file_name = ''
        self.current_listings = []
        self.previous_listings = []

    def load(self):
        self.set_parameters()
        self.load_previous_listings()
        self.driver = Firefox()
        time.sleep(2)
        self.driver.get(self.search_url)
        time.sleep(2)

    def load_previous_listings(self):
        with open(self.previous_listings_file_name) as in_file:
            for line in in_file.readlines():
                previous_listing = line.rstrip()
                self.previous_listings.append(previous_listing)

    def set_parameters(self):
        pass

    def parse(self):
        soup = BeautifulSoup(self.driver.page_source, features="lxml")
        listings = soup.find_all(attrs=self.listings_search)
        for listing in listings:
            if listing.text not in self.previous_listings:
                self.current_listings.append(listing.text)

    def exit(self):
        self.driver.close()
        self.write_previous_listings_file()

    def write_previous_listings_file(self):
        with open(self.previous_listings_file_name, 'a') as out_file:
            for listing in self.current_listings:
                out_file.write(f"{listing}\n")

    def run(self):
        self.load()
        self.parse()
        self.exit()