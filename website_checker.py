from selenium.webdriver import Firefox
from bs4 import BeautifulSoup
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
        self.listing_links = []
        self.soup = None

    def load(self, driver: Firefox):
        self.set_parameters()
        self.load_previous_listings()
        self.driver = driver
        self.driver.get(self.search_url)
        time.sleep(3)
        self.soup = BeautifulSoup(self.driver.page_source)

    def load_previous_listings(self):
        with open(self.previous_listings_file_name) as in_file:
            for line in in_file.readlines():
                previous_listing = line.rstrip()
                self.previous_listings.append(previous_listing)

    def set_parameters(self):
        pass

    def parse(self):
        listings = self.soup.find_all(attrs=self.listings_search)
        for i, listing in enumerate(listings):
            if self.listing_is_applicable(listing, i):
                listing_address = self.get_listing_address(listing)
                self.current_listings.append(listing_address)
                link = self.get_listing_link(listing)
                self.listing_links.append(link)

    def listing_is_applicable(self, listing, listing_index):
        listing_address = self.get_listing_address(listing)
        return listing_address not in self.previous_listings

    def get_listing_address(self, listing):
        return listing.text

    def get_listing_link(self, listing):
        pass

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