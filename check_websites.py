from selenium.webdriver import Firefox, FirefoxProfile

from ymere_checker import YmereChecker

from notifier import Notifier

if __name__ == "__main__":
    # instantiate error notifier
    error_notifier = Notifier(['maxguillaume20@gmail.com'])

    # instantiate website checkers
    checker_classes = [YmereChecker]
    checkers = [checker_class() for checker_class in checker_classes]

    profile = FirefoxProfile()
    driver = Firefox(firefox_profile=profile)

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
        new_listing_notifier = Notifier(['maxguillaume20@gmail.com'])
        subject = f"New listings from: {','.join([checker.id for checker in checkers_with_new_listings])}"
        content = ''
        for checker in checkers_with_new_listings:
            content += f"{checker.id}:\n"
            for new_listing in checker.current_listings:
                content += f"\t{new_listing}\n"
        new_listing_notifier.send_email(subject, content)
