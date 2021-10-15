from website_checker import WebsiteChecker

class YmereChecker(WebsiteChecker):

    def set_parameters(self):
        self.id = 'Ymere'
        self.search_url = "https://aanbod.ymere.nl/aanbod/huurwoningen/#?gesorteerd-op=maxhuurprijs%2B&ik-zoek-een=3&ik-zoek-een=1&huurprijs=0&huurprijs=1500&locatie=Amsterdam%2BCentrum-Amsterdam%2BCentrum&locatie=Amsterdam%2BOost-Amsterdam%2BOost&locatie=Amsterdam%2BZuid-Amsterdam%2BZuid&aantal-slaapkamers=1&aantal-slaapkamers=2"
        self.listings_search = {"class": "address-part", "ng-bind-html": "::object.title"}
        self.previous_listings_file_name = "ymere_listings.txt"
