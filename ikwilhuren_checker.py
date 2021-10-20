from postcode_checker import PostcodeChecker

import re
from bs4 import BeautifulSoup

import time


class IkWilHurenChecker(PostcodeChecker):

    def __init__(self):
        super(IkWilHurenChecker, self).__init__()
        self.statuses = []

    def set_parameters(self):
        self.id = "IkWilHuren"
        self.search_url = "https://ikwilhuren.nu/?action=epl_search&post_type=rental&property_location%5B0%5D=5570&property_category=Appartement&property_price_to=1500&property_building_area_unit=squareMeter&sortby=status_asc"
        self.listings_search = {"class": "street-name straat"}
        self.previous_listings_file_name = "C:\\Users\\maxgu\\projects\\ymere_checker\\listings\\ikwilhuren_listings.txt"

    def get_listing_link(self, listing):
        return listing.parent.parent.attrs['href']

    def load(self, driver):
        super(IkWilHurenChecker, self).load(driver)
        self.statuses = self.soup.select("div figure span")

    def get_postcode(self, listing):
        postcode = re.search(r'([\d]{4})[\w]{2}', listing.parent.text).group(1)
        return postcode

    def listing_is_applicable(self, listing, listing_index):
        not_onder_optie = self.statuses[listing_index].text != "Onder optie"
        return not_onder_optie and super(IkWilHurenChecker, self).listing_is_applicable(listing, listing_index)



if __name__ == "__main__":
    import time
    from selenium.webdriver import Firefox, FirefoxProfile
    from bs4 import BeautifulSoup
    profile = FirefoxProfile()
    driver = Firefox(firefox_profile=profile)
    time.sleep(1)

    checker = IkWilHurenChecker()
    checker.load(driver)
    checker.driver.get(checker.search_url)
    time.sleep(3)
    soup = BeautifulSoup(checker.driver.page_source)
    listings = soup.find_all(attrs=checker.listings_search)

    poops = soup.select("div figure span")
    print(len(poops), len(listings))
    for i, listing in enumerate(listings):
        address = checker.get_listing_address(listing)
        postcode = checker.get_postcode(listing)
        print(address, postcode, poops[i].text)
    driver.close()