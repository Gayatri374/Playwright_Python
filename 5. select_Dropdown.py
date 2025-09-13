from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')


    select_dropdow=page.query_selector('//select[@id="Skills"]')
    select_dropdow.select_option('Java')
    page.wait_for_timeout(4000)

    python=page.select_option('//select[@id="Skills"]','Python')
    page.wait_for_timeout(4000)
    print('python:',python)

