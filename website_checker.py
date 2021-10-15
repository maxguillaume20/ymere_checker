from selenium.webdriver import Firefox
from bs4 import BeautifulSoup
from twilio.rest import Client
import time



class WebsiteChecker(object):

    def __init__(self):
        self.id = ''
        self.driver = None
        self.search_url = ''
        self.listings_search = {}
        self.previous_listings_file_name = ''
        self.current_listings = []
        self.previous_listings = []

    def load(self, driver: Firefox):
        self.set_parameters()
        self.load_previous_listings()
        self.driver = driver

    def load_previous_listings(self):
        with open(self.previous_listings_file_name) as in_file:
            for line in in_file.readlines():
                previous_listing = line.rstrip()
                self.previous_listings.append(previous_listing)

    def set_parameters(self):
        pass

    def parse(self):
        self.driver.get(self.search_url)
        time.sleep(2)
        soup = BeautifulSoup(self.driver.page_source, features="lxml")
        listings = soup.find_all(attrs=self.listings_search)
        for listing in listings:
            if listing.text not in self.previous_listings:
                self.current_listings.append(listing.text)

    def exit(self):
        self.write_previous_listings_file()

    def write_previous_listings_file(self):
        with open(self.previous_listings_file_name, 'a') as out_file:
            for listing in self.current_listings:
                out_file.write(f"{listing}\n")

    def run(self, driver):
        try:
            self.load(driver)
            self.parse()
            self.exit()
        except Exception as e:
            return e

    @property
    def has_new_listings(self):
        return len(self.current_listings) > 0