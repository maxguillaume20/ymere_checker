from website_checker import WebsiteChecker
from bs4 import BeautifulSoup


class PostcodeChecker(WebsiteChecker):

    postcode_file_name = 'C:\\Users\\maxgu\\projects\\ymere_checker\\applicable_postcodes.txt'

    def __init__(self):
        super(PostcodeChecker, self).__init__()
        self.applicable_postcodes = []

    def load(self, driver):
        super(PostcodeChecker, self).load(driver)
        self.read_postcode_file()

    def read_postcode_file(self):
        with open(PostcodeChecker.postcode_file_name) as in_file:
            for line in in_file.readlines():
                postcode = str(line).rstrip()
                self.applicable_postcodes.append(postcode)

    def get_postcode(self, listing):
        pass

    def listing_is_applicable(self, listing, listing_index):
        listing_in_applicable_postcode = self.get_postcode(listing) in self.applicable_postcodes
        return listing_in_applicable_postcode and super(PostcodeChecker, self).listing_is_applicable(listing, listing_index)


