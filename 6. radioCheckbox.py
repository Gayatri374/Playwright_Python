from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')

    # Radio button
    radio_button=page.query_selector('//input[@value="FeMale"]')
    # radio_button.click()
    radio_button.check()
    # verification whether it is checked or not
    if radio_button.is_checked():
        print('Radio Button checked')
    else:
        print('it is not checked')


    # Checkbox
    check_box=page.query_selector('//input[@value="Cricket"]')
    check_box.click()
    # verification whether it is checked or not
    if check_box.is_checked():
        print('Passed')
    else:
        print('Failed')
    page.wait_for_timeout(4000)