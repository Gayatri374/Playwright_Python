from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://power-efficiency-506-dev-ed.scratch.my.salesforce-setup.com/lightning/setup/SetupOneHome/home')
    print('chrome opened successfully')
    print(page.title())
    page.wait_for_timeout(3000)
    browser.close()
