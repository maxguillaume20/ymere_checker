from website_checker import WebsiteChecker


class VestadaChecker(WebsiteChecker):

    def set_parameters(self):
        self.id = "Vestada"
        self.search_url = "https://www.vesteda.com/nl/woning-zoeken?s=Amsterdam,%20Nederland&sc=woning&priceFrom=500&priceTo=1500&bedRooms=0&unitTypes=2&unitTypes=1&unitTypes=3&unitTypes=4&radius=5&placeType=1&lng=4.904139&lat=52.3675728&sortType=0"
        self.listings_search = {"class": "h5 u-margin-bottom-none"}
        self.previous_listings_file_name = "C:\\Users\\maxgu\\projects\\ymere_checker\\listings\\vestada_listings.txt"

    def get_listing_address(self, listing):
        return next(listing.children).text

    def get_listing_link(self, listing):
        return next(listing.children).attrs['href']


# if __name__ == "__main__":
#     import time
#     from selenium.webdriver import Firefox, FirefoxProfile
#     profile = FirefoxProfile()
#     driver = Firefox(firefox_profile=profile)
#     time.sleep(1)
#
#     checker = VestadaChecker()
#     checker.load(driver)
#     checker.parse()
#     for i, address in enumerate(checker.current_listings):
#         print(address)
#         print(checker.listing_links[i])
#     driver.close()
