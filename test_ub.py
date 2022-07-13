import time


def test_search_example(veb_driver):
    veb_driver.get('https://google.com')

    time.sleep(3)

    search_input = veb_driver.find_element_by_name('q')

    search_input.clear()
    search_input.send_keys('first test')

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # Click Search:
    search_button = veb_driver.find_element_by_name('btnK')
    search_button.submit()

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!

    # Make the screenshot of browser window:
    veb_driver.save_screenshot('result.png')

    veb_driver.close()


#test_search_example(driver)
