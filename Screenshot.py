from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://www.redbus.in/')


    page.screenshot(path='redbusoo.png', full_page=True)