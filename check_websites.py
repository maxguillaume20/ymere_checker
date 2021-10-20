import time

from selenium.webdriver import Firefox, FirefoxProfile

from ymere_checker import YmereChecker
from vestada_checker import VestadaChecker
from funda_checker import FundaChecker
from ikwilhuren_checker import IkWilHurenChecker

from notifier import Notifier

if __name__ == "__main__":
    # instantiate error notifier
    error_notifier = Notifier(['maxguillaume20@gmail.com'])

    # instantiate website listings
    checkers = [
        YmereChecker(),
        VestadaChecker(),
        FundaChecker(),
        IkWilHurenChecker()
    ]

    profile = FirefoxProfile()
    driver = Firefox(firefox_profile=profile)
    time.sleep(1)

    # check each of the rental websites
    checkers_with_new_listings = []
    for checker in checkers:
        error = checker.run(driver)
        if error is not None:
            error_notifier.send_email(subject=f"Error checking {checker.id}",
                                      content=str(error))
            continue
        if checker.has_new_listings:
            checkers_with_new_listings.append(checker)
    try:
        driver.close()
    except Exception as error:
        error_notifier.send_email(subject=f"Error closing driver",
                                  content=str(error))

    # if new listings are available, send a notification
    if len(checkers_with_new_listings) > 0:
        new_listing_notifier = Notifier(['maxguillaume20@gmail.com', 'm.simkovicova@uva.nl'])
        subject = f"New listings from: {', '.join([checker.id for checker in checkers_with_new_listings])}"
        content = ''
        for checker in checkers_with_new_listings:
            content += f"{checker.id}:\n"
            for i, new_listing in enumerate(checker.current_listings):
                content += f"\t{new_listing}\n\t{checker.listing_links[i]}\n\n"
        new_listing_notifier.send_email(subject, content)
