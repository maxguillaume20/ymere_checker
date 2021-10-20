from postcode_checker import PostcodeChecker
import re


class FundaChecker(PostcodeChecker):

    def set_parameters(self):
        self.id = "Funda"
        self.search_url = "https://www.funda.nl/huur/amsterdam/0-1500/3-dagen/"
        self.listings_search = {"class": "search-result__header-title fd-m-none"}
        self.previous_listings_file_name = "C:\\Users\\maxgu\\projects\\ymere_checker\\listings\\funda_listings.txt"

    def get_listing_address(self, listing):
        return listing.text[1:].rstrip()

    def get_listing_link(self, listing):
        return listing.parent.attrs['href']

    def get_postcode(self, listing):
        return re.search(r'([\d]{4}) [\w]{2}', listing.parent.parent.text).group(1)



if __name__ == "__main__":
    import time
    from selenium.webdriver import Firefox, FirefoxProfile
    profile = FirefoxProfile()
    driver = Firefox(firefox_profile=profile)
    time.sleep(1)

    checker = FundaChecker()
    checker.load(driver)
    listings = checker.soup.find_all(attrs=checker.listings_search)
    for i, listing in enumerate(listings):
        listing_address = checker.get_listing_address(listing)
        sibling = listing.nextSibling
        checker.current_listings.append(listing_address)

        postcode = re.search(r'([\d]{4}) [\w]{2}', listing.parent.parent.text).group(1)
        print(postcode)
        link = checker.get_listing_link(listing)
        checker.listing_links.append(link)
    driver.close()