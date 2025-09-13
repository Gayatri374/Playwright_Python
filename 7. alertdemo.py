from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')


    # page.wait_for_selector('//div[@id="OKTab"]/button').click()
    # page.wait_for_timeout(3000)

    # In playwright it will automatically click on the Ok button no need to give accept or dismiss as selenium]

    page.wait_for_selector('//a[@href="#CancelTab"]').click()
    page.wait_for_timeout(3000)
    # Control alert
    page.on("dialog", lambda dialog : print(dialog.message))
    page.on("dialog", lambda dialog : dialog.dismiss())
    page.wait_for_selector('//div[@id="CancelTab"]/button').click()
    page.wait_for_timeout(3000)
